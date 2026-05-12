# Helpful Bob Prompts for watsonx Orchestrate Development

<p align="center">
  <img src="../bobchestrate_helpful_prompts.png" alt="Bobchestrate - Helpful Prompts" width="700">
</p>

This guide contains useful prompts to help you work with Bob throughout the workshop and beyond.

## General Agent Development

### Understanding Concepts
```
Bob, explain what watsonx Orchestrate agents are and how they differ from regular chatbots
```

```
Bob, what are the key components of a watsonx Orchestrate agent?
```

```
Bob, explain the difference between native, external, and assistant agents
```

### Getting Started
```
Bob, help me set up my watsonx Orchestrate development environment
```

```
Bob, show me how to verify my watsonx Orchestrate connection is working
```

```
Bob, what's the basic structure of an agent YAML file?
```

## Creating Agents

### Basic Agent Creation
```
Bob, create a YAML file for a customer service agent that can help with orders and refunds
```

```
Bob, create an agent that acts as a Python programming tutor
```

```
Bob, build an agent specification for a travel booking assistant
```

### Improving Agent Instructions
```
Bob, review these agent instructions and suggest improvements: [paste instructions]
```

```
Bob, make these agent instructions more specific and actionable: [paste instructions]
```

```
Bob, add error handling guidance to these agent instructions: [paste instructions]
```

### Agent Configuration
```
Bob, explain what the 'hide_reasoning' configuration option does
```

```
Bob, help me choose the right LLM model for my agent
```

```
Bob, what's the difference between agent styles (default, react, planner)?
```

## Building Tools

### Tool Creation
```
Bob, create a Python tool that checks order status given an order ID
```

```
Bob, build a tool that validates email addresses and returns detailed feedback
```

```
Bob, create a tool that calls the OpenWeather API to get current weather
```

### Tool Improvement
```
Bob, add input validation to this tool: [paste tool code]
```

```
Bob, improve the error handling in this tool: [paste tool code]
```

```
Bob, add type hints and better documentation to this tool: [paste tool code]
```

### Tool Debugging
```
Bob, why isn't my agent calling this tool? Here's the agent YAML and tool code: [paste both]
```

```
Bob, this tool is returning an error. Can you help debug it? [paste error and code]
```

```
Bob, review this tool for potential issues: [paste tool code]
```

## Working with Knowledge Bases

### Knowledge Base Setup
```
Bob, create a knowledge base YAML file for FAQ documents
```

```
Bob, help me structure my knowledge base for best retrieval performance
```

```
Bob, explain how to connect a knowledge base to my agent
```

### Knowledge Base Optimization
```
Bob, how should I format my documents for optimal knowledge base performance?
```

```
Bob, what's the best way to organize multiple knowledge bases?
```

## Agent Collaboration

### Creating Collaborator Agents
```
Bob, create a specialized escalation agent that handles complex customer issues
```

```
Bob, build a technical support agent that can collaborate with a billing agent
```

```
Bob, design an agent hierarchy for a customer service system
```

### Routing and Delegation
```
Bob, improve the routing logic in these agent instructions: [paste instructions]
```

```
Bob, help me decide when my agent should delegate to a collaborator
```

## Testing and Debugging

### Test Case Generation
```
Bob, generate test cases for this customer support agent
```

```
Bob, create a test script that validates my order status tool
```

```
Bob, write test scenarios that cover edge cases for my refund tool
```

### Debugging
```
Bob, my agent isn't responding correctly. Here's the conversation: [paste conversation]
```

```
Bob, analyze this error message and suggest a fix: [paste error]
```

```
Bob, why is my agent calling the wrong tool? [paste agent YAML and conversation]
```

### Performance Optimization
```
Bob, how can I make my agent respond faster?
```

```
Bob, review my agent's instructions for efficiency: [paste instructions]
```

```
Bob, suggest ways to reduce token usage in my agent
```

## Integration and Deployment

### API Integration
```
Bob, create a tool that calls this REST API: [paste API documentation]
```

```
Bob, add authentication to this API tool: [paste tool code]
```

```
Bob, help me handle rate limiting in this API tool: [paste tool code]
```

### Deployment
```
Bob, create a deployment checklist for my agent
```

```
Bob, help me test my agent before deploying to production
```

```
Bob, generate webchat embed code for my agent
```

## Code Review and Refactoring

### Code Review
```
Bob, review this agent YAML for best practices: [paste YAML]
```

```
Bob, check this tool for security issues: [paste tool code]
```

```
Bob, review my entire agent setup and suggest improvements: [paste all files]
```

### Refactoring
```
Bob, refactor this tool to be more modular: [paste tool code]
```

```
Bob, split this complex agent into multiple specialized agents: [paste agent YAML]
```

```
Bob, improve the code organization in my tool: [paste tool code]
```

## Documentation

### Generating Documentation
```
Bob, create documentation for this tool: [paste tool code]
```

```
Bob, write a README for my agent project
```

```
Bob, generate API documentation for my custom tools
```

### User Guides
```
Bob, create a user guide for interacting with my customer service agent
```

```
Bob, write instructions for deploying this agent
```

## Advanced Topics

### Custom Workflows
```
Bob, design a multi-step workflow using agent collaborators
```

```
Bob, create a planner-style agent with structured output
```

```
Bob, build an agent that uses chain-of-thought reasoning
```

### MCP Servers
```
Bob, help me create an MCP server for my custom tools
```

```
Bob, explain how to connect an MCP server to watsonx Orchestrate
```

### Model Configuration
```
Bob, create a custom model configuration for Azure OpenAI
```

```
Bob, set up a model policy with fallback models
```

## Troubleshooting Common Issues

### Connection Issues
```
Bob, I'm getting a connection refused error. How do I fix it?
```

```
Bob, my API key isn't working. What should I check?
```

### Agent Not Responding
```
Bob, my agent isn't responding to user messages. Help me debug this.
```

```
Bob, the agent is giving generic responses instead of using tools. Why?
```

### Tool Issues
```
Bob, my tool isn't being imported. What could be wrong?
```

```
Bob, the agent sees my tool but never calls it. How do I fix this?
```

### Performance Issues
```
Bob, my agent is slow. How can I improve response time?
```

```
Bob, I'm hitting rate limits. What's the best approach?
```

## Best Practices

### Ask Bob for Best Practices
```
Bob, what are the best practices for writing agent instructions?
```

```
Bob, how should I structure my tools for maintainability?
```

```
Bob, what's the recommended way to handle errors in agents?
```

```
Bob, how do I make my agents more reliable in production?
```

## Learning and Exploration

### Exploring Features
```
Bob, what are some advanced features of watsonx Orchestrate I should know about?
```

```
Bob, show me examples of creative ways to use agent collaborators
```

```
Bob, what are some real-world use cases for watsonx Orchestrate agents?
```

### Staying Updated
```
Bob, what's new in the latest version of watsonx Orchestrate?
```

```
Bob, are there any deprecated features I should be aware of?
```

## Tips for Effective Bob Prompts

### ✅ DO:
- **Be specific**: Include relevant code, error messages, or context
- **State your goal**: Explain what you're trying to achieve
- **Provide examples**: Show what you've tried or what you want
- **Ask follow-ups**: Build on Bob's responses with clarifying questions
- **Request explanations**: Ask Bob to explain the reasoning behind suggestions

### ❌ DON'T:
- **Be vague**: "Bob, fix this" without context
- **Skip context**: Not providing relevant code or configuration
- **Expect mind-reading**: Bob needs information about your specific situation
- **Ignore suggestions**: Bob's recommendations are based on best practices
- **Ask multiple unrelated questions**: Focus on one topic at a time

## Example Conversation Flow

Here's an example of an effective conversation with Bob:

```
You: Bob, I need to create a customer support agent that can check order status and process refunds.

Bob: [Provides initial agent structure]

You: Thanks! Can you also add a tool that checks order status? It should take an order ID and return the status, items, and delivery date.

Bob: [Creates order status tool]

You: Great! Now I'm getting an error when I import the tool. Here's the error: [paste error]

Bob: [Analyzes error and provides fix]

You: Perfect! Can you now update the agent YAML to use this tool?

Bob: [Updates agent configuration]

You: Excellent! Can you generate some test cases for this agent?

Bob: [Provides test scenarios]
```

## Quick Reference

### Most Common Prompts

1. **Create**: "Bob, create a [type] that does [function]"
2. **Debug**: "Bob, why is [thing] not working? Here's the [code/error]"
3. **Improve**: "Bob, improve [code/config] by [specific improvement]"
4. **Explain**: "Bob, explain [concept] in the context of [use case]"
5. **Review**: "Bob, review [code/config] for [issues/best practices]"

---

**💡 Pro Tip:** The more context you provide to Bob, the better the responses will be. Include relevant code, error messages, and explain what you're trying to achieve!

**🎯 Remember:** Bob is your AI pair programmer. Use Bob to learn, not just to get answers. Ask Bob to explain the reasoning behind suggestions!