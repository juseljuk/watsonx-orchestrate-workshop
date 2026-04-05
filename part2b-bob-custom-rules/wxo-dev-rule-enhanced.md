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
- **requirements.txt** - Python dependencies
- **.env.example** - Environment variable templates (never commit actual .env)
- **README.md** - Architecture diagrams, workflow diagrams, setup instructions
- **.gitignore** - Exclude .env, credentials, and local config files

---

## 2. Development Patterns & Best Practices

### LLM Configuration for Agents
- Use groq/openai/gpt-oss-120b as the default LLM model

### Tool & Flow Development
- Use `@flow` decorator for flows with proper type hints
- Use `@tool` decorator for Python tools with clear docstrings
- Include inline KVP schemas for document processing
- Create native agents for document handling tasks
- Implement proper input validation and schema definitions
- Use async/await patterns for I/O-bound operations in flows

### Error Handling
```python
@tool
def my_tool(param: str) -> dict:
    """Tool with proper error handling."""
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

#### Pre-invoke Guardrails
```python
# plugins/content_safety_plugin.py
from ibm_watsonx_orchestrate import plugin

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
name: customer-support-agent
description: |
  Handles customer support inquiries including:
  - Order status checks
  - Refund requests
  - Product information
  
instructions: |
  You are a helpful customer support agent.
  Always be polite and professional.
  Escalate complex issues to human agents.
  
examples:
  - input: "Where is my order?"
    output: "I'll check your order status. Could you provide your order number?"
```

### Tool Documentation
```python
@tool
def check_order_status(order_id: str) -> dict:
    """
    Check the status of a customer order.
    
    Args:
        order_id: The unique order identifier (format: ORD-XXXXX)
        
    Returns:
        dict: Order status information including:
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
# Solution: Optimize tool execution, increase timeout
# Check agent YAML: timeout: 60

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