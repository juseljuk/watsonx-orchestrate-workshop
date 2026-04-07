# Part 3b: AI Gateway and Using Different Models

**Duration:** 25 minutes
**Objective:** Learn how to configure and use different AI models through watsonx Orchestrate's AI Gateway

> 📋 **Quick Reference:** Check out the [Model Selection Guide](model-selection-guide.md) for a quick reference on choosing the right model!

## What You'll Learn

- Understanding the AI Gateway architecture
- How to configure different LLM providers
- Selecting appropriate models for different use cases
- Model performance and cost considerations
- Testing agents with different models
- Best practices for model selection

## Why AI Gateway Matters

The AI Gateway in watsonx Orchestrate provides:
- 🔌 **Unified Interface** - Access multiple LLM providers through a single API
- 🔄 **Model Flexibility** - Switch between models without changing agent code
- 💰 **Cost Optimization** - Choose models based on performance/cost tradeoffs
- 🛡️ **Governance** - Centralized control over model access and usage
- 📊 **Monitoring** - Track model usage, performance, and costs

## Available Model Providers

watsonx Orchestrate supports multiple LLM providers through the AI Gateway. The platform includes preferred models that are optimized and validated for use:

### Preferred Models (Included with Platform)

#### 1. Groq Models
- **groq/openai/gpt-oss-120b** ⭐ - High-performance model optimized for speed, tool calling, and multilingual support. **Recommended default choice.**

#### 2. watsonx.ai Models
- **watsonx/meta-llama/llama-3-2-90b-vision-instruct** ⭐ - Advanced multimodal model supporting both text and vision tasks with 90B parameters
- **watsonx/meta-llama/llama-3-405b-instruct** ⭐ - Meta's largest open-source model with 405B parameters, optimized for the most complex reasoning tasks

### Additional Models via AI Gateway

You can also add custom models from other providers through the AI Gateway:
- **Anthropic Claude** - claude-3-opus, claude-3-sonnet, claude-3-haiku
- **OpenAI** - GPT-4, GPT-3.5-turbo
- **Google Gemini** - gemini-pro, gemini-flash
- **AWS Bedrock** - Various models
- **Azure OpenAI** - Azure-hosted models
- **Ollama** - Locally hosted models

> **Note:** Models marked with ⭐ are preferred models that have been validated and optimized for watsonx Orchestrate.

## Step 1: Understanding Model Selection

Different models excel at different tasks. Here's a guide:

### Task-Based Model Selection

| Task Type | Recommended Model | Why |
|-----------|------------------|-----|
| General purpose, tool calling | groq/openai/gpt-oss-120b | Optimized for speed and tool calling, best default choice |
| Multimodal (text + images) | watsonx/meta-llama/llama-3-2-90b-vision-instruct | Handles both text and vision tasks |
| Complex reasoning | watsonx/meta-llama/llama-3-405b-instruct | Highest capability, 405B parameters |
| Customer support | groq/openai/gpt-oss-120b | Fast, reliable, good tool calling |
| Code generation | groq/openai/gpt-oss-120b | Strong coding capabilities |
| Creative writing | watsonx/meta-llama/llama-3-405b-instruct | Superior creativity and reasoning |
| Document analysis with images | watsonx/meta-llama/llama-3-2-90b-vision-instruct | Vision capabilities |

### Performance vs. Cost Tradeoffs

```
High Performance, High Cost
    ↑
    │  watsonx/meta-llama/llama-3-405b-instruct (405B params)
    │
    │  watsonx/meta-llama/llama-3-2-90b-vision-instruct (90B params + vision)
    │
    │  groq/openai/gpt-oss-120b (optimized for speed)
    ↓
Fast & Efficient
```

## Step 2: Create Agents with Different Models

Let's create three versions of a customer support agent using different models to compare their behavior.

### Agent 1: Standard Support Agent (Groq GPT - Recommended)

📥 **[Download Agent](agents/support-agent-standard.yaml)** | Place it into `agents/` directory of your workspace

```yaml
spec_version: v1
kind: native
name: support_agent_standard_<your_initials_here>
description: Standard customer support agent - recommended for most use cases

instructions: |
  You are a customer support agent providing helpful, efficient responses.
  
  Your approach:
  - Understand customer needs quickly
  - Provide clear, actionable guidance
  - Show empathy and professionalism
  - Handle multi-step requests efficiently
  - Use tools effectively for order and refund management
  
  Balance speed with quality service.

# Using the recommended default model - optimized for tool calling and speed
llm: groq/openai/gpt-oss-120b

tools:
  - check_order_status_<your_initials_here>
  - process_refund_<your_initials_here>

```

### Agent 2: Advanced Support Agent (Llama 3.2 90B Vision)

📥 **[Download Agent](agents/support-agent-advanced.yaml)** | Place it into `agents/` directory of your workspace

```yaml
spec_version: v1
kind: native
name: support_agent_advanced_<your_initials_here>
description: Advanced customer support agent with multimodal capabilities

instructions: |
  You are a senior customer support specialist handling complex situations.
  
  Your capabilities:
  - Deep understanding of customer emotions and context
  - Complex problem-solving and reasoning
  - Ability to analyze images (product photos, receipts, damage reports)
  - Nuanced decision-making
  - Handling difficult or upset customers
  - Multi-step problem resolution
  
  Provide thoughtful, comprehensive support that addresses both
  immediate needs and underlying concerns. When customers share images,
  analyze them carefully to better understand their situation.

# Using advanced multimodal model for complex scenarios
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct

tools:
  - check_order_status_<your_initials_here>
  - process_refund_<your_initials_here>

```

### Agent 3: Expert Support Agent (Llama 3 405B)

📥 **[Download Agent](agents/support-agent-expert.yaml)** | Place it into `agents/` directory of your workspace

```yaml
spec_version: v1
kind: native
name: support_agent_expert_<your_initials_here>
description: Expert-level customer support for the most complex scenarios

instructions: |
  You are an executive-level customer support specialist handling the most
  complex and sensitive customer situations.
  
  Your capabilities:
  - Exceptional reasoning and problem-solving
  - Deep empathy and emotional intelligence
  - Creative solutions for unique situations
  - Authority to make exceptions and special accommodations
  - Handling VIP customers and critical escalations
  
  Provide world-class support that exceeds expectations while maintaining
  company policies and profitability. Think creatively to find win-win solutions.

# Using the most capable model for highest-complexity scenarios
llm: watsonx/meta-llama/llama-3-405b-instruct

tools:
  - check_order_status_<your_initials_here>
  - process_refund_<your_initials_here>

```

## Step 3: Import and Test the Agents

### IMPORTANT: Replace `<your_initials_here>` with your actual initials in all references inside the yaml-files - Agent _name_ and the _tool references_. Make sure that the tools are correctly referenced in the YAML files, your tool files might be named differently. Use the tools you created and imported in the previous part.

Then, import all three agents:

```bash
orchestrate agents import -f agents/support-agent-standard.yaml
orchestrate agents import -f agents/support-agent-advanced.yaml
orchestrate agents import -f agents/support-agent-expert.yaml
```

Verify they were imported:
```bash
orchestrate agents list | grep -E "support_agent.*<your_initials>"
```

## Step 4: Compare Model Performance

Test each agent with the same scenarios to compare their responses.

### Test Scenario 1: Simple Query

Test all three agents with:
```
What's your return policy?
```

**Expected Differences:**
- **Standard Agent**: Quick, clear, well-structured answer
- **Advanced Agent**: Detailed response with context
- **Expert Agent**: Comprehensive answer with nuanced understanding

### Test Scenario 2: Complex Situation

Test with:
```
I ordered a laptop 3 weeks ago (ORD-12345), it arrived damaged, I need it for work tomorrow, and I'm very frustrated. What can you do?
```

**Expected Differences:**
- **Standard Agent**: Efficient handling with empathy and clear solutions
- **Advanced Agent**: Deep empathy, creative problem-solving, proactive suggestions
- **Expert Agent**: Exceptional empathy, creative win-win solutions, may offer special accommodations

### Test Scenario 3: Multi-Step Request

Test with:
```
I need to check my order status, and if it hasn't shipped yet, I want to change the shipping address and upgrade to express shipping.
```

**Expected Differences:**
- **Standard Agent**: Handles multi-step flow efficiently with good tool usage
- **Advanced Agent**: Smooth orchestration with anticipation of needs
- **Expert Agent**: Seamless handling with proactive suggestions and alternatives

### Test Scenario 4: Image Analysis (Advanced Agent Only)

Test the advanced agent with:
```
I received a damaged product. [Attach image of damaged item]
```

**Expected Behavior:**
- **Advanced Agent**: Can analyze the image to assess damage severity and provide appropriate solutions

## Step 5: Model Configuration Best Practices

### When to Use Each Model Type

#### Use Standard Model (groq/openai/gpt-oss-120b) When:
- ✅ General purpose tasks
- ✅ Tool calling is important
- ✅ Response speed matters
- ✅ Most production use cases
- ✅ Default choice for new agents
- ✅ Cost-effective for high volume

#### Use Advanced Model (llama-3-2-90b-vision) When:
- ✅ Multimodal tasks (text + images)
- ✅ Complex reasoning required
- ✅ Document analysis with visuals
- ✅ Product inspection scenarios
- ✅ Higher quality needed than standard

#### Use Expert Model (llama-3-405b) When:
- ✅ Most complex reasoning required
- ✅ Handling VIP or sensitive situations
- ✅ Quality is paramount
- ✅ Creative problem-solving needed
- ✅ Executive-level interactions
- ✅ Lower volume, high-value scenarios

### Model Configuration Tips

```yaml
# Standard model specification
llm: groq/openai/gpt-oss-120b

# For multimodal tasks
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct

# For highest capability
llm: watsonx/meta-llama/llama-3-405b-instruct
```

**Note:** watsonx Orchestrate does not support setting temperature or other model parameters directly in the agent YAML. Model behavior is controlled through your agent instructions.

## Step 6: Create a Model Router Agent

Let's create an intelligent agent that routes to different models based on complexity.

### Ask Bob:
```
Bob, create a router agent that analyzes the customer query and delegates to either the standard, advanced, or expert support agent based on query complexity.
```

Or create manually:

```yaml
# support-router-agent.yaml
spec_version: v1
kind: native
name: support_router_<your_initials_here>
description: Routes customer queries to appropriate support agent based on complexity

instructions: |
  You are a routing agent that analyzes customer queries and delegates to
  the most appropriate support agent.
  
  Routing Logic:
  
  Route to support_agent_standard_<your_initials_here> for:
  - Standard customer support requests (80% of queries)
  - Order status checks
  - FAQ questions
  - General refund requests
  - Most typical interactions
  
  Route to support_agent_advanced_<your_initials_here> for:
  - Complex problem-solving (15% of queries)
  - Queries involving images or documents
  - Multi-faceted issues
  - Situations requiring deeper analysis
  
  Route to support_agent_expert_<your_initials_here> for:
  - Most complex scenarios (5% of queries)
  - Very upset or frustrated customers
  - VIP customers
  - Situations requiring exceptions or special handling
  - High-value or sensitive matters
  
  Analyze the query, determine complexity, and delegate immediately.
  Do not try to answer yourself - always delegate to a specialist.

llm: groq/openai/gpt-oss-120b  # Fast, efficient model for routing decisions

collaborators:
  - support_agent_standard_<your_initials_here>
  - support_agent_advanced_<your_initials_here>
  - support_agent_expert_<your_initials_here>
```

Import and test:
```bash
orchestrate agents import -f agents/support-router-agent.yaml
orchestrate chat ask -n support_router_<your_initials_here>
```

## Step 7: Monitor Model Performance

### Using Bob to Analyze Performance

Ask Bob to help analyze your agent's performance:

```
Bob, analyze the response times and quality of my three support agents and recommend which model to use for production.
```

### Key Metrics to Consider

1. **Response Time**
   - How quickly does the agent respond?
   - Is speed acceptable for your use case?

2. **Response Quality**
   - Does it understand complex queries?
   - Are responses accurate and helpful?
   - Does it handle edge cases well?

3. **Cost**
   - What's the cost per interaction?
   - What's the monthly projected cost?

4. **User Satisfaction**
   - Do users get their questions answered?
   - Do they need to rephrase or repeat?
   - Is the tone appropriate?

## Best Practices

### ✅ DO:

- Start with balanced models and adjust based on needs
- Test multiple models with your specific use cases
- Consider cost vs. performance tradeoffs
- Use lightweight models for high-volume, simple tasks
- Reserve advanced models for complex scenarios
- Monitor and optimize model usage over time
- Document why you chose specific models

### ❌ DON'T:

- Use advanced models for everything (unnecessary cost)
- Use lightweight models for complex reasoning
- Forget to test with real user scenarios
- Ignore response time requirements
- Overlook cost implications at scale
- Change models without testing impact

## Advanced: Dynamic Model Selection

You can create agents that dynamically select models based on context:

```yaml
# adaptive-agent.yaml
spec_version: v1
kind: native
name: adaptive_support_<your_initials_here>
description: Adapts model selection based on query complexity

instructions: |
  You are an adaptive support agent that adjusts your approach based on
  the complexity of the customer's needs.
  
  For simple queries, provide quick, efficient responses.
  For complex situations, engage in deeper analysis and problem-solving.
  
  Always prioritize customer satisfaction while being cost-effective.

# Start with balanced model
llm: groq/openai/gpt-oss-120b

tools:
  - check_order_status_<your_initials_here>
  - process_refund_<your_initials_here>

knowledge_base:
  - customer-support-faq-<your_initials_here>

# Can delegate to advanced agent when needed
collaborators:
  - support_agent_advanced_<your_initials_here>
```

## Exercises

Ready to practice? We've prepared comprehensive exercises to help you master model selection and optimization!

📝 **[View All Exercises](exercises.md)** - Complete exercises ranging from easy to advanced

The exercises cover:
- Model performance comparison
- Cost optimization strategies
- Domain-specific model selection
- Advanced routing with context
- Model parameter tuning
- Multi-model workflows
- Fallback strategies

We recommend working through at least the first 2-3 exercises to solidify your understanding before moving to the next part.

## Common Issues

### Issue: Agent using wrong model
**Solution:** Check the `llm` field in your agent YAML. Re-import after changes.

### Issue: Model not available
**Solution:** Verify model name is correct. Check available models:
```bash
orchestrate models list
```

### Issue: Slow responses
**Solution:** Consider using a faster model or optimizing agent instructions.

### Issue: Poor quality responses
**Solution:** Try a more capable model or improve agent instructions.

## Key Takeaways

✅ Different models have different strengths and costs  
✅ Match model capability to task complexity  
✅ Test multiple models with your specific use cases  
✅ Balance performance, cost, and quality  
✅ Use routing agents for intelligent model selection  
✅ Monitor and optimize model usage over time  

## Next Steps

Now that you understand model selection, let's add knowledge bases and collaborators!

Continue to [Part 4: Knowledge Bases & Collaborators](../part4-knowledge/README.md) →

## Additional Resources

- [watsonx Orchestrate Model Guide](https://developer.watson-orchestrate.ibm.com/models/overview)
- [LLM Selection Best Practices](https://developer.watson-orchestrate.ibm.com/models/selection)
- [Cost Optimization Strategies](https://developer.watson-orchestrate.ibm.com/models/cost_optimization)

---

**💡 Pro Tip:** Start with the balanced model (groq/openai/gpt-oss-120b) for most use cases, then optimize based on actual performance data!