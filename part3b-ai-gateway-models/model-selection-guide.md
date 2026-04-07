# Quick Model Selection Guide

A quick reference for choosing the right model for your watsonx Orchestrate agents.

## Model Comparison Table

| Model | Speed | Cost | Capability | Best For |
|-------|-------|------|------------|----------|
| **groq/openai/gpt-oss-120b** | ⚡⚡⚡ | 💰💰 | ⭐⭐⭐⭐ | General purpose, balanced performance, tool calling |
| **watsonx/meta-llama/llama-3-2-90b-vision-instruct** | ⚡⚡ | 💰💰💰 | ⭐⭐⭐⭐⭐ | Multimodal tasks, vision + text, complex reasoning |
| **watsonx/meta-llama/llama-3-405b-instruct** | ⚡ | 💰💰💰💰 | ⭐⭐⭐⭐⭐ | Most complex reasoning, highest capability |

## Decision Tree

```
Start Here
    |
    ├─ Does it involve images or vision?
    │   └─ YES → watsonx/meta-llama/llama-3-2-90b-vision-instruct
    │
    ├─ Does it require the highest capability reasoning?
    │   └─ YES → watsonx/meta-llama/llama-3-405b-instruct
    │
    └─ General purpose / Standard tasks?
        └─ groq/openai/gpt-oss-120b (recommended default)
```

## Use Case Examples

### Customer Support

```yaml
# Standard support agent (recommended for most queries)
llm: groq/openai/gpt-oss-120b

# Advanced support agent (complex issues, high-value customers)
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct

# Executive escalation agent (most complex scenarios)
llm: watsonx/meta-llama/llama-3-405b-instruct
```

### Content Generation

```yaml
# Product descriptions (creative, high quality)
llm: watsonx/meta-llama/llama-3-405b-instruct

# Technical documentation (precise)
llm: groq/openai/gpt-oss-120b

# Marketing content with images
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
```

### Data Processing

```yaml
# Data extraction and analysis
llm: groq/openai/gpt-oss-120b

# Complex data reasoning and insights
llm: watsonx/meta-llama/llama-3-405b-instruct

# Document analysis with images/charts
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
```

## Cost Optimization Strategies

### Strategy 1: Tiered Approach
- **Tier 1 (80% of queries):** groq/openai/gpt-oss-120b (default for most tasks)
- **Tier 2 (15% of queries):** watsonx/meta-llama/llama-3-2-90b-vision-instruct (complex or multimodal)
- **Tier 3 (5% of queries):** watsonx/meta-llama/llama-3-405b-instruct (highest complexity)

### Strategy 2: Time-Based
- **Peak hours:** Fast models for quick responses
- **Off-peak:** Advanced models for quality

### Strategy 3: User-Based
- **Free tier users:** Standard models
- **Premium users:** Advanced models


## Common Patterns

### Pattern 1: Router + Specialists
```yaml
# Router (fast, efficient)
router_agent:
  llm: groq/openai/gpt-oss-120b

# Specialists (appropriate for domain)
standard_agent:
  llm: groq/openai/gpt-oss-120b

advanced_agent:
  llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct

expert_agent:
  llm: watsonx/meta-llama/llama-3-405b-instruct
```

### Pattern 2: Progressive Enhancement
```yaml
# Start with standard model
initial_agent:
  llm: groq/openai/gpt-oss-120b
  
# Escalate to advanced model if needed
escalation_agent:
  llm: watsonx/meta-llama/llama-3-405b-instruct
```

### Pattern 3: Hybrid Workflow
```yaml
# Stage 1: Initial processing
triage:
  llm: groq/openai/gpt-oss-120b

# Stage 2: Complex analysis
processing:
  llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct

# Stage 3: Final review (highest quality)
quality_check:
  llm: watsonx/meta-llama/llama-3-405b-instruct
```

## Performance Benchmarks

### Response Time (Approximate)
- **groq/openai/gpt-oss-120b:** 1-3 seconds (optimized for speed)
- **watsonx/meta-llama/llama-3-2-90b-vision-instruct:** 2-5 seconds
- **watsonx/meta-llama/llama-3-405b-instruct:** 3-8 seconds

### Token Limits
- **groq/openai/gpt-oss-120b:** Large context window
- **watsonx/meta-llama/llama-3-2-90b-vision-instruct:** 8,192 tokens
- **watsonx/meta-llama/llama-3-405b-instruct:** 8,192 tokens

## Troubleshooting

### Problem: Responses too slow
**Solution:** Switch to a faster model or optimize instructions

### Problem: Poor quality responses
**Solution:** Switch to a more capable model or improve prompts

### Problem: High costs
**Solution:** Implement routing to use cheaper models when possible

### Problem: Inconsistent responses
**Solution:** Use a more deterministic model or refine agent instructions for consistency

## Quick Tips

1. **Start with groq/openai/gpt-oss-120b** - Good default choice
2. **Test with real queries** - Don't assume, measure
3. **Monitor costs** - Track usage and optimize
4. **Use routing** - Don't use expensive models for simple tasks
5. **Consider latency** - Faster models for real-time interactions
7. **Document choices** - Record why you chose each model

## Model Selection Checklist

Before choosing a model, ask:

- [ ] What's the complexity of the task?
- [ ] What's the expected query volume?
- [ ] What's the budget constraint?
- [ ] What's the acceptable response time?
- [ ] Is creativity or consistency more important?
- [ ] What's the cost of errors?
- [ ] Can I use routing to optimize?

## Additional Resources

- [watsonx Orchestrate Documentation](https://developer.watson-orchestrate.ibm.com/)
- [Agent Builder Guide](https://developer.watson-orchestrate.ibm.com/agents/overview)
- [AI Gateway - Managing Custom LLMs](https://developer.watson-orchestrate.ibm.com/llm/managing_llm#managing-custom-llms-with-the-ai-gateway)

---

**Remember:** The best model is the one that meets your requirements at the lowest cost. Always test with your specific use case!

---

> 📚 **Full Tutorial:** For detailed explanations and step-by-step instructions, see the [Part 3b: AI Gateway and Using Different Models](README.md) main guide.