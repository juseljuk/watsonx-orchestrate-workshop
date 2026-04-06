## watsonx Orchestrate Development Rule - Enhanced

When working with IBM watsonx Orchestrate or watsonx Orchestrate ADK projects:

---

## 1. Project Structure & Organization

Follow ADK conventions when creating and saving artifacts:

### Core Directories
- **agents/** - Agent YAML configurations
- **tools/** - Flows and Python tools
- **knowledge_bases/** - Knowledge base configurations
- **models/** - LLM model configurations
- **toolkits/** - MCP toolkit definitions
- **connections/** - API connections and credential configurations
- **channels/** - Deployment channel configurations (Slack, Teams, Web, etc.)
- **plugins/** - Guardrail and custom plugins
- **tests/** or **evaluation/** - Test cases and evaluation datasets

### Essential Files
- **import-all.sh** - Comprehensive deployment script for all artifact types
- **requirements.txt** - Python dependencies (exclude `ibm-watsonx-orchestrate` - it's platform-managed)
- **.env.example** - Environment variable templates (never commit actual .env)
- **README.md** - Architecture diagrams, workflow diagrams, setup instructions
- **.gitignore** - Exclude .env, credentials, and local config files

### Environment Configuration (.env.example)

The `.env.example` file must follow the official watsonx Orchestrate Developer Edition structure:

#### Required: Choose ONE Authentication Method

**Option 1: watsonx Orchestrate Account (SaaS/Trial)**
```bash
WO_DEVELOPER_EDITION_SOURCE=orchestrate
WO_INSTANCE=https://your-instance.watson-orchestrate.ibm.com
WO_API_KEY=your-api-key-here
```

**Option 2: myIBM (On-premises/Purchased)**
```bash
WO_DEVELOPER_EDITION_SOURCE=myibm
WO_ENTITLEMENT_KEY=your-entitlement-key
GROQ_API_KEY=your-groq-api-key
WATSONX_APIKEY=your-watsonx-api-key
WATSONX_SPACE_ID=your-space-id
```

**Option 3: Custom Image Registry**
```bash
WO_DEVELOPER_EDITION_SOURCE=custom
REGISTRY_URL=your-registry-url
REGISTRY_USERNAME=your-username
REGISTRY_PASSWORD=your-password
```

#### Optional: Service Credentials
Developer Edition includes built-in services (Minio, Langfuse, MCP Gateway, etc.). Only override if using external services:
```bash
# MINIO_ROOT_USER=minioadmin
# MINIO_ROOT_PASSWORD=minioadmin
# LANGFUSE_SECRET_KEY=your-secret-key
# MCP_GATEWAY_API_KEY=your-api-key
```

#### Optional: Regional Configuration
For non-us-south regions, configure regional endpoints:
```bash
# ASSISTANT_LLM_API_BASE=https://us-south.ml.cloud.ibm.com
# ASSISTANT_EMBEDDINGS_API_BASE=https://us-south.ml.cloud.ibm.com
# ROUTING_LLM_API_BASE=https://us-south.ml.cloud.ibm.com
# WATSONX_URL=https://us-south.ml.cloud.ibm.com
```

#### Optional: On-Premises Configuration
For on-premises deployments with Docker:
```bash
# DOCKER_IMAGE_PULL_POLICY=IfNotPresent
# DOCKER_SKIP_SSL_VERIFY=false
# DOCKER_ENABLE_LAYER_CACHING=true
```

**IMPORTANT**:
- Never include actual credentials in `.env.example`
- Do NOT use non-standard variables like `ORCHESTRATE_API_KEY`, `ORCHESTRATE_ENVIRONMENT`, or `TIMEOUT_SECONDS`
- Do NOT include Slack, database, or other service-specific configs unless they're official Developer Edition variables
- Always refer to official documentation for the latest environment variable requirements

---

## 2. Development Patterns & Best Practices

### Agent Naming Conventions

**CRITICAL**: Agent names must follow strict naming conventions to ensure proper routing and identification within watsonx Orchestrate.

#### Required Naming Format
- **Use snake_case** - Names must use underscores, not camelCase or spaces
- **No spaces allowed** - Agent names cannot contain spaces
- **No special characters** - Avoid special characters in names
- **Keep names short and descriptive** - Names should be concise yet meaningful
- **Use domain-specific language** - Names should reflect the agent's purpose and domain

#### Naming Examples

✅ **Good Examples:**
- `customer_support_agent`
- `sales_outreach_agent`
- `ibm_historical_knowledge_agent`
- `product_catalog_agent`
- `order_processing_agent`

❌ **Bad Examples:**
- `customerSupportAgent` (camelCase not allowed)
- `customer support agent` (spaces not allowed)
- `agent-123` (special characters not recommended)
- `helper` (too generic)
- `myAgent1` (not descriptive, uses camelCase)

#### Why These Conventions Matter
- **Routing agents** work better with snake_case names
- **User identification** is easier with clear, descriptive names
- **System consistency** is maintained across all agents
- **Avoid generic terms** like "helper" or "assistant" - use domain-specific language instead

### LLM Configuration for Agents
- Use groq/openai/gpt-oss-120b as the default LLM model

### Tool & Flow Development
- Use `@flow` decorator for flows with proper type hints
- Use `@tool` decorator (without parentheses) for Python tools with clear docstrings
- **CRITICAL**: Always import tool decorator as `from ibm_watsonx_orchestrate.agent_builder.tools import tool`
- **CRITICAL**: Use explicit type hints that match docstring descriptions to avoid parameter parsing warnings
- **CRITICAL**: Use Google-style docstrings with type annotations in parentheses (e.g., `param (str):`)
- **CRITICAL**: Return type in docstring must match function return type hint exactly (e.g., `Dict[str, Any]:` not `dict:`)
- Include inline KVP schemas for document processing
- Create native agents for document handling tasks
- Implement proper input validation and schema definitions
- Use async/await patterns for I/O-bound operations in flows

### Type Hints Best Practices

**IMPORTANT**: The watsonx Orchestrate platform relies on type hints to generate proper tool schemas. Incorrect or missing type hints will cause warnings like:
```
[WARNING] - Unable to properly parse parameter descriptions due to missing or incorrect type hints.
```

#### Required Type Hint Standards
1. **All parameters must have explicit type hints** - Never omit parameter types
2. **Return types must be specified** - Always include `-> TypeHint`
3. **Use specific types over generic ones** - Prefer `Dict[str, Any]` over `Dict`
4. **Import necessary typing constructs** - `from typing import Dict, List, Any, Optional`
5. **Type hints must match docstring descriptions** - Consistency is critical

#### Correct Type Hint Examples

```python
from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import Dict, List, Any, Optional

@tool
def check_order_status(order_id: str) -> Dict[str, Any]:
    """
    Check the status of a customer order.
    
    Args:
        order_id (str): The unique order identifier (format: ORD-XXXXX)
        
    Returns:
        Dict[str, Any]: Order status information including status, delivery date, etc.
    """
    # Implementation
    return {"status": "shipped", "order_id": order_id}

@tool
def process_items(items: List[Dict[str, Any]], priority: Optional[int] = None) -> Dict[str, Any]:
    """
    Process a list of items with optional priority.
    
    Args:
        items (List[Dict[str, Any]]): List of item dictionaries with name and quantity
        priority (Optional[int]): Optional priority level (1-5)
        
    Returns:
        Dict[str, Any]: Processing result with status and processed count
    """
    # Implementation
    return {"status": "success", "processed": len(items)}
```

#### Common Type Hint Mistakes

❌ **Wrong - Generic Dict without type parameters:**
```python
def my_tool(data: dict) -> Dict:  # Too generic, causes warnings
```

✅ **Correct - Specific type parameters:**
```python
def my_tool(data: Dict[str, Any]) -> Dict[str, Any]:  # Explicit and clear
```

❌ **Wrong - Missing return type:**
```python
def my_tool(param: str):  # No return type specified
```

✅ **Correct - Explicit return type:**
```python
def my_tool(param: str) -> Dict[str, Any]:  # Clear return type
```

❌ **Wrong - Inconsistent with docstring:**
```python
@tool
def my_tool(count: str) -> dict:  # Docstring says count is int
    """
    Args:
        count (int): Number of items (integer)
    """
```

✅ **Correct - Matches docstring:**
```python
@tool
def my_tool(count: int) -> Dict[str, Any]:  # Matches docstring
    """
    Args:
        count (int): Number of items (integer)
        
    Returns:
        Dict[str, Any]: Processing result
    """
```

### Error Handling
```python
from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import Dict, Any

@tool
def my_tool(param: str) -> Dict[str, Any]:
    """
    Tool with proper error handling.
    
    Args:
        param (str): Input parameter
        
    Returns:
        Dict[str, Any]: Result with status and data or error message
    """
    try:
        # Tool logic
        result = process_data(param)
        return {"status": "success", "data": result}
    except ValueError as e:
        return {"status": "error", "message": f"Invalid input: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"Unexpected error: {str(e)}"}
```

### Logging & Debugging
- Use structured logging with appropriate log levels
- Include context in log messages (agent name, tool name, request ID)
- Log input parameters (sanitize sensitive data)
- Log execution time for performance monitoring

### Connection Binding
- Define connections in YAML for external APIs
- Use environment variables for credentials
- Test connections locally by emulating environment variables
- Handle connection failures gracefully with retries

### Multi-Agent Collaboration
- Design clear agent responsibilities and boundaries
- Use explicit handoff patterns between agents
- Document agent interaction flows
- Test multi-agent scenarios thoroughly

---

## 3. Testing & Quality Assurance

### Testing Python Tools with @tool Decorator

**CRITICAL**: The `@tool` decorator from watsonx Orchestrate wraps functions and changes their return behavior. When creating test files for Python tools:

1. **DO NOT import the decorated function directly** - The decorator expects specific return formats (`content` or `context_updates` keys)
2. **Create standalone test versions** - Copy the tool's business logic into test files WITHOUT the `@tool` decorator
3. **Keep tool and test logic synchronized** - When updating tools, update corresponding tests

#### Example Test File Structure

```python
"""
Test cases for my_tool.

Note: This file contains a copy of the tool logic WITHOUT the @tool decorator
for testing purposes. The actual tool in tools/my_tool.py uses the @tool decorator.
"""

from datetime import datetime
from typing import Dict

def my_tool(param1: str, param2: int) -> Dict:
    """
    Test version of my_tool without @tool decorator.
    Copy the exact business logic from tools/my_tool.py
    """
    try:
        # Business logic here (same as in tools/my_tool.py)
        result = process_data(param1, param2)
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

def test_successful_case():
    """Test successful execution."""
    result = my_tool("test", 42)
    assert result['status'] == 'success'
    print("✓ Test passed")

def test_error_case():
    """Test error handling."""
    result = my_tool("", -1)
    assert result['status'] == 'error'
    print("✓ Test passed")

if __name__ == "__main__":
    test_successful_case()
    test_error_case()
```

#### Why This Approach

- **Decorator Complexity**: The `@tool` decorator is designed for watsonx Orchestrate's agent framework, not local testing
- **Return Format**: Decorated functions return data in a specific format that's incompatible with direct dictionary access
- **Testing Independence**: Test files should test business logic independently of framework decorators
- **Maintainability**: Keep tool logic and test logic in sync manually

#### Alternative: Integration Testing

For testing tools within the watsonx Orchestrate environment:
```bash
# Use orchestrate CLI evaluation tools
orchestrate evaluations quick-eval -p tests/ -o results/ -t tools/
```

### Quick Evaluation
```bash
# Quick evaluation of agent
orchestrate evaluations quick-eval -p tests/ -o results/ -t tools/

# Evaluate specific test cases with config file
orchestrate evaluations quick-eval -c evaluation/config.yaml
```

### Evaluation Datasets
- Create comprehensive test cases covering:
  - Happy path scenarios
  - Edge cases and boundary conditions
  - Error scenarios
  - Multi-turn conversations
- Store test cases in `tests/` or `evaluation/` directory
- Version control your test datasets

### LLM Vulnerability Testing
- Test for prompt injection attacks
- Validate input sanitization
- Check for sensitive data leakage
- Test guardrail effectiveness

### Performance Metrics
- Monitor token usage and costs
- Track response times
- Measure tool execution success rates
- Analyze conversation completion rates

---

## 4. Security & Guardrails

### Guardrail Plugins

**IMPORTANT**: Guardrails must be implemented as plugin files before they can be referenced in agent YAML configurations. Do NOT add guardrail references to agent YAML unless the corresponding plugin files exist in the `plugins/` directory and have been imported.

Only reference guardrails in agent YAML after:
1. Creating the plugin file (e.g., `plugins/content_safety_plugin.py`)
2. Importing the plugin: `orchestrate plugins import -f plugins/content_safety_plugin.py`
3. Verifying the plugin exists: `orchestrate plugins list`

#### Pre-invoke Guardrails
```python
# plugins/content_safety_plugin.py
from ibm_watsonx_orchestrate.agent_builder.plugins import plugin

@plugin(type="pre-invoke")
def content_safety_check(input_text: str) -> dict:
    """Check for inappropriate content before processing."""
    if contains_inappropriate_content(input_text):
        return {
            "block": True,
            "reason": "Content violates safety guidelines"
        }
    return {"block": False}
```

#### Post-invoke Guardrails
```python
from ibm_watsonx_orchestrate.agent_builder.plugins import plugin

@plugin(type="post-invoke")
def pii_detection(response: str) -> dict:
    """Detect and redact PII in responses."""
    if contains_pii(response):
        return {
            "modified_response": redact_pii(response),
            "warning": "PII detected and redacted"
        }
    return {"modified_response": response}
```

### Security Best Practices
- **Never hardcode credentials** - Use connections and environment variables
- **Sanitize all inputs** - Validate and clean user inputs
- **Implement rate limiting** - Protect against abuse
- **Use least privilege** - Grant minimal necessary permissions
- **Audit logging** - Log security-relevant events
- **Regular security testing** - Run vulnerability scans

### Credential Management
```yaml
# connections/api-connection.yaml
name: external-api
type: http
auth:
  type: bearer_token
  token: ${API_TOKEN}  # From environment variable
```

---

## 5. Deployment & Channels

### Channel Configuration

#### Slack Channel
```yaml
# channels/slack-channel.yaml
name: customer-support-slack
type: slack
agent: customer-support-agent
settings:
  workspace_id: ${SLACK_WORKSPACE_ID}
  bot_token: ${SLACK_BOT_TOKEN}
```

#### Web Chat Channel
```yaml
# channels/web-chat.yaml
name: website-chat
type: web
agent: product-assistant
settings:
  theme: light
  welcome_message: "How can I help you today?"
```

### Environment-Specific Configurations
- **Development** - Use test credentials, verbose logging
- **Staging** - Mirror production, use staging APIs
- **Production** - Production credentials, optimized settings

### Deployment Process
```bash
# 1. Import all artifacts
./import-all.sh

# 2. Verify deployment
orchestrate agents list

# 3. Deploy agent (not available in Developer Edition)
orchestrate agents deploy --name <agent-name>

# 4. Deploy to channels
orchestrate channels deploy <channel-name>
```

### Deployment Verification
- Test agent responses in each channel
- Verify connection configurations
- Check guardrail activation
- Monitor initial usage metrics

### Rollback Strategy
- Keep previous versions tagged
- Document rollback procedures
- Test rollback in staging first
- Monitor post-rollback metrics

---

## 6. MCP Server Integration

### MCP Toolkit Patterns

#### Local MCP Server
```yaml
# toolkits/local-mcp-toolkit.yaml
name: product-catalog
type: mcp
transport: stdio
command: python
args:
  - product_catalog_server.py
tools:
  - search_products
  - get_product_details
```

#### Remote MCP Server
```yaml
# toolkits/remote-mcp-toolkit.yaml
name: weather-service
type: mcp
transport: sse
url: https://weather-api.example.com/mcp
tools:
  - get_forecast
  - get_current_weather
```

### Error Handling
- Handle server connection failures gracefully
- Implement timeout mechanisms
- Provide fallback responses when MCP unavailable
- Log MCP errors for debugging

### Resource Management
- Monitor MCP server resource usage
- Implement connection pooling for remote servers
- Set appropriate timeouts
- Clean up resources properly

### Testing MCP Integrations
```bash
# Test MCP server locally
python product_catalog_server.py

# Test toolkit import
orchestrate toolkits import toolkits/product-catalog-toolkit.yaml

# List imported tools
orchestrate tools list
```

### Documentation Requirements
- Use `watsonx-orchestrate-adk-docs` MCP server for API references
- Search documentation when uncertain about features
- Leverage code examples from documentation
- Stay updated with latest ADK best practices

---

## 7. Documentation Standards

### README.md Requirements
```markdown
# Project Name

## Overview
Brief description of the project and its purpose

## Architecture
[Include architecture diagram]

## Workflow
[Include workflow diagram showing agent interactions]

## Setup
1. Prerequisites
2. Installation steps
3. Configuration

## Usage
Examples of how to use the agents

## Testing
How to run tests and evaluations

## Deployment
Deployment instructions for each environment
```

### Agent YAML Documentation
```yaml
spec_version: v1
kind: native
name: customer-support-agent
llm: groq/openai/gpt-oss-120b  # Simple string format: provider/model-id
style: default  # Options: default, react, planner
hide_reasoning: false

description: |
  Handles customer support inquiries including:
  - Order status checks
  - Refund requests
  - Product information
  
instructions: |
  You are a helpful customer support agent.
  Always be polite and professional.
  Escalate complex issues to human agents.

# Guidelines for rule-based behavior control
guidelines:
  - condition: "The customer requests a refund"
    action: "Verify the order ID and process the refund using the process_refund tool"
    tool: "process_refund"
  - condition: "The customer is very upset"
    action: "Acknowledge their frustration and escalate to a supervisor"

tools:
  - check_order_status
  - process_refund

collaborators: []

knowledge_base: []

restrictions: editable  # Options: editable, non_editable

# Only include guardrails section if plugins are implemented and imported
# guardrails:
#   pre_invoke:
#     - content_safety_check
#   post_invoke:
#     - pii_detection
```

### Agent Guidelines

**IMPORTANT**: Guidelines provide rule-based behavior control for agents. They create predictable, consistent responses for specific conditions.

#### Guidelines Structure

Guidelines use a specific YAML format with three fields:

```yaml
guidelines:
  - condition: "When this situation occurs"
    action: "Then perform this action"
    tool: "tool_name"  # Optional: tool to invoke
```

#### Required Fields
- **condition** (required): The trigger condition in natural language (the "when" part)
- **action** (optional): The action to perform when condition is met (the "then" part)
- **tool** (optional): The tool name to invoke (must match a tool in the `tools` list)

**Note**: You must provide at least one of `action` or `tool` for each guideline.

#### Guidelines Best Practices

1. **Write Clear Conditions**: Use natural language that describes the trigger situation
   - ✅ Good: "The customer requests a refund over $10,000"
   - ❌ Bad: "High value refund"

2. **Specify Concrete Actions**: Describe exactly what the agent should do
   - ✅ Good: "Acknowledge the request, explain that high-value refunds require specialist review, and escalate to the escalation agent"
   - ❌ Bad: "Handle it appropriately"

3. **Order Matters**: Guidelines are evaluated in order, so place more specific conditions before general ones
   ```yaml
   guidelines:
     - condition: "The refund amount exceeds $10,000"  # Specific first
       action: "Escalate to specialist"
     - condition: "The customer requests a refund"      # General second
       action: "Process normally"
       tool: "process_refund"
   ```

4. **Tool References**: When specifying a tool, ensure it exists in the `tools` list
   ```yaml
   tools:
     - process_refund_JKJ
     - check_order_status_JKJ
   
   guidelines:
     - condition: "Customer asks about order"
       tool: "check_order_status_JKJ"  # Must match exactly
   ```

5. **Combine with Instructions**: Use guidelines for specific rules, instructions for general behavior
   - **Instructions**: Overall persona, tone, general approach
   - **Guidelines**: Specific "when-then" rules for predictable scenarios

#### Guidelines vs Instructions

| Use Guidelines For | Use Instructions For |
|-------------------|---------------------|
| Specific trigger conditions | General behavior and persona |
| Rule-based responses | Tone and style guidance |
| Tool invocation rules | Context and background |
| Escalation triggers | Overall approach |
| Conditional logic | Flexible decision-making |

#### Example: Complete Agent with Guidelines

```yaml
spec_version: v1
kind: native
name: customer_support_agent
llm: groq/openai/gpt-oss-120b
style: default

description: Handles customer support for orders and refunds

instructions: |
  You are a professional customer support agent.
  Always be empathetic and solution-focused.
  Use the guidelines to handle specific scenarios consistently.

guidelines:
  # Refund processing rules
  - condition: "The customer requests a refund under $500"
    action: "Process immediately and confirm 5-7 day timeline"
    tool: "process_refund"
  
  - condition: "The customer requests a refund over $10,000"
    action: "Acknowledge request and escalate to specialist for review"
  
  # Escalation rules
  - condition: "The customer mentions legal action or lawyers"
    action: "Remain professional and immediately escalate to the escalation agent"
  
  - condition: "The customer is very upset after 2-3 resolution attempts"
    action: "Acknowledge frustration and connect with a specialist"
  
  # Order status rules
  - condition: "The customer asks about their order status"
    action: "Request order ID if not provided, then check status"
    tool: "check_order_status"

tools:
  - check_order_status
  - process_refund

collaborators:
  - escalation_agent
```

#### Common Guideline Patterns

**Escalation Pattern:**
```yaml
- condition: "The [specific trigger condition]"
  action: "Acknowledge [the situation] and escalate to [collaborator agent]"
```

**Tool Invocation Pattern:**
```yaml
- condition: "The customer [requests something]"
  action: "Verify [required info] and use the tool to [accomplish task]"
  tool: "tool_name"
```

**Conditional Processing Pattern:**
```yaml
- condition: "The [metric] is [comparison] [threshold]"
  action: "Process using [specific approach] and inform customer of [outcome]"
  tool: "tool_name"
```

**Error Handling Pattern:**
```yaml
- condition: "The [tool/operation] fails or returns an error"
  action: "Apologize, explain the issue, and [fallback action]"
```

### Tool Documentation
```python
from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import Dict, Any

@tool
def check_order_status(order_id: str) -> Dict[str, Any]:
    """
    Check the status of a customer order.
    
    Args:
        order_id (str): The unique order identifier (format: ORD-XXXXX)
        
    Returns:
        Dict[str, Any]: Order status information including:
            - status: Current order status
            - estimated_delivery: Expected delivery date
            - tracking_number: Shipping tracking number
            
    Example:
        >>> check_order_status("ORD-12345")
        {
            "status": "shipped",
            "estimated_delivery": "2024-01-15",
            "tracking_number": "1Z999AA10123456784"
        }
    """
    # Implementation
```

### Changelog Maintenance
- Document all significant changes
- Include version numbers and dates
- Note breaking changes prominently
- Link to relevant issues or PRs

---

## 8. Troubleshooting & Debugging

### Common Error Patterns

#### Import Errors
```bash
# Error: Tool not found
# Solution: Check tool name matches @tool decorator
orchestrate tools list  # Verify tool is imported

# Error: Connection failed
# Solution: Verify connection exists and is configured
orchestrate connections list  # Check if connection exists
```

#### Runtime Errors
```bash
# Error: Agent timeout
# Solution: Optimize tool execution time
# - Reduce complexity of tool operations
# - Implement caching for repeated operations
# - Use async operations where possible

# Error: Token limit exceeded
# Solution: Reduce context, optimize prompts
# Monitor token usage in logs
```

### Debugging Locally

#### Test Tools Independently
```python
# test_tools.py
from tools.order_status_tool import check_order_status

result = check_order_status("ORD-12345")
print(result)
```

#### Test Flows with Mock Data
```python
# test_flow.py
from tools.customer_flow import customer_support_flow

test_input = {
    "user_message": "Where is my order?",
    "order_id": "ORD-12345"
}

result = customer_support_flow(test_input)
print(result)
```

### Log Analysis
- Check agent execution logs for errors
- Review tool invocation logs
- Analyze token usage patterns
- Monitor response times

### Connection Troubleshooting
```bash
# List all connections
orchestrate connections list

# Import connection from YAML
orchestrate connections import -f connections/my-connection.yaml

# Set credentials for connection
orchestrate connections set-credentials -a <app-id> --env draft -u <username> -p <password>
```

---

## 9. Performance Optimization

### Token Usage Optimization
- Use concise, clear prompts
- Avoid redundant context in multi-turn conversations
- Implement conversation summarization for long sessions
- Choose appropriate model sizes for tasks

### Caching Strategies
- Cache frequently accessed data (product catalogs, FAQs)
- Implement response caching for common queries
- Use knowledge bases for static information
- Cache API responses when appropriate

### Efficient Tool Chaining
```python
import asyncio
from ibm_watsonx_orchestrate.agent_builder.tools import flow

@flow
async def optimized_flow(input_data: dict) -> dict:
    """Efficient flow with parallel tool execution."""
    # Execute independent tools in parallel
    results = await asyncio.gather(
        tool_a(input_data),
        tool_b(input_data),
        tool_c(input_data)
    )
    
    # Process results
    return combine_results(results)
```

### Knowledge Base Optimization
- Structure knowledge bases for efficient retrieval
- Use appropriate chunk sizes
- Implement relevance scoring
- Regular knowledge base updates and pruning

### Model Selection Guidelines
- **Simple tasks** - Use smaller, faster models
- **Complex reasoning** - Use larger, more capable models
- **Cost-sensitive** - Balance performance vs. cost
- **Latency-sensitive** - Prioritize faster models

---

## 10. Quick Reference Commands

### Agent Management
```bash
# List agents
orchestrate agents list

# Import agent
orchestrate agents import -f agents/my-agent.yaml

# Deploy agent (not in Developer Edition)
orchestrate agents deploy --name my-agent

# Undeploy agent (not in Developer Edition)
orchestrate agents undeploy --name my-agent

# Remove agent
orchestrate agents remove --name my-agent
```

### Tool Management
```bash
# List tools
orchestrate tools list

# Import Python tool
orchestrate tools import -k python -f tools/my-tool.py -r requirements.txt

# Remove tool
orchestrate tools remove -n my-tool
```

### Toolkit Management
```bash
# List toolkits
orchestrate toolkits list

# Add MCP toolkit
orchestrate toolkits add --kind mcp --name my-toolkit --description "My toolkit" --package-root /path/to/folder --command '["node", "dist/index.js"]' --tools "*"

# Export toolkit
orchestrate toolkits export -n my-toolkit -o my-toolkit.zip

# Remove toolkit
orchestrate toolkits remove -n my-toolkit
```

### Connection Management
```bash
# List connections
orchestrate connections list

# Import connection from YAML
orchestrate connections import -f connections/my-connection.yaml

# Export connection
orchestrate connections export -a <app-id> -o connection.yaml

# Remove connection
orchestrate connections remove -a <app-id>
```

### Channel Management
```bash
# List supported channel types
orchestrate channels list

# List channels for an agent
orchestrate channels list-channels --agent-name my-agent --env draft

# Import/create channel from file
orchestrate channels import --agent-name my-agent --env draft --file channels/my-channel.yaml

# Export channel
orchestrate channels export --agent-name my-agent --env draft --type webchat --name my-channel -o channel.yaml

# Delete channel
orchestrate channels delete --agent-name my-agent --env draft --type webchat --name my-channel
```

### Evaluation & Testing
```bash
# Quick evaluation (reference-less)
orchestrate evaluations quick-eval -p tests/ -o results/ -t tools/

# Quick evaluation with config file
orchestrate evaluations quick-eval -c evaluation/config.yaml

# Standard evaluation (requires test datasets)
orchestrate evaluations evaluate -c evaluation/eval-config.yaml
```

### Deployment
```bash
# Import all artifacts
./import-all.sh

# Deploy agent (not available in Developer Edition)
orchestrate agents deploy --name my-agent

# Undeploy agent (revert to previous version)
orchestrate agents undeploy --name my-agent

# Export agent with dependencies
orchestrate agents export -k native -n my-agent -o my-agent.zip
```

---

## Best Practices Summary

1. **Always use CLI** for importing agents and tools
2. **Test locally first** before deploying to production
3. **Use connections** for all external API integrations
4. **Implement guardrails** for safety and compliance
5. **Document everything** - code, configurations, workflows
6. **Version control** all artifacts and configurations
7. **Monitor performance** - tokens, latency, success rates
8. **Security first** - never commit credentials, sanitize inputs
9. **Evaluate regularly** - maintain test cases, run evaluations
10. **Leverage MCP servers** - especially `watsonx-orchestrate-adk-docs` for guidance