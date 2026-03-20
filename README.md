# Building Your First AI Agent with watsonx Orchestrate
## A Hands-On Workshop with Bob as Your AI Assistant

Welcome! This workshop will guide you through building a practical AI agent using IBM watsonx Orchestrate. You'll use Bob, an AI coding assistant, to help you along the way.

## Workshop Overview

**Duration:** 90-120 minutes  
**Level:** Beginner to Intermediate  
**Prerequisites:** 
- Basic Python knowledge
- watsonx Orchestrate access (or Developer Edition)
- VS Code with Bob extension installed
- Python 3.9+ installed

## What You'll Build

You'll create a **Customer Support Agent** that can:
1. Answer frequently asked questions using a knowledge base
2. Check order status via a custom Python tool
3. Process refund requests with business logic
4. Escalate complex issues to specialized sub-agents

## Workshop Structure

### [Part 1: Setup & Environment](./part1-setup/README.md) (15 min)
- Configure watsonx Orchestrate credentials
- Verify Bob is working as your AI assistant
- Understand the project structure
- Set up your development environment

### [Part 2: Building Your First Agent](./part2-first-agent/README.md) (20 min)
- Create a simple "Hello World" agent
- Understand agent instructions and behavior
- Test your agent with the chat interface
- Learn how to use Bob to help debug issues

### [Part 3: Adding Custom Tools](./part3-custom-tools/README.md) (30 min)
- Create a Python tool to check order status
- Create a tool to process refund requests
- Import tools into your agent
- Use Bob to help write and debug tool code

### [Part 4: Knowledge Bases & Collaborators](./part4-advanced/README.md) (25 min)
- Add a knowledge base for FAQs
- Create a specialized escalation agent
- Connect agents as collaborators
- Test the complete customer support flow

### [Part 5: Testing & Deployment](./part5-deployment/README.md) (20 min)
- Test your agent thoroughly
- Deploy to different environments
- Generate webchat embed code
- Monitor agent performance

## How Bob Helps You

Throughout this workshop, you'll use Bob to:
- **Generate code**: "Bob, create a Python tool that checks order status"
- **Debug issues**: "Bob, why is my agent not calling the refund tool?"
- **Explain concepts**: "Bob, explain how agent instructions work"
- **Refactor code**: "Bob, improve the error handling in my tool"
- **Create tests**: "Bob, write tests for my order status tool"

## Workshop Files

```
workshop/
├── README.md (this file)
├── part1-setup/
│   ├── README.md
│   └── verify-setup.py
├── part2-first-agent/
│   ├── README.md
│   ├── hello-agent.yaml
│   └── exercises.md
├── part3-custom-tools/
│   ├── README.md
│   ├── order_status_tool.py
│   ├── refund_tool.py
│   └── exercises.md
├── part4-advanced/
│   ├── README.md
│   ├── customer-support-agent.yaml
│   ├── escalation-agent.yaml
│   ├── faq-knowledge-base.yaml
│   └── exercises.md
├── part5-deployment/
│   ├── README.md
│   ├── test-scenarios.md
│   └── deployment-checklist.md
├── solutions/
│   └── (completed code for reference)
└── bob-prompts/
    └── helpful-prompts.md
```

## Getting Started

1. Clone or download this workshop repository
2. Open the `workshop` folder in VS Code
3. Make sure Bob is installed and active
4. Start with [Part 1: Setup](./part1-setup/README.md)

## Learning Objectives

By the end of this workshop, you will:
- ✅ Understand watsonx Orchestrate agent architecture
- ✅ Create and configure agents using YAML specifications
- ✅ Build custom Python tools for specific business logic
- ✅ Integrate knowledge bases for FAQ handling
- ✅ Use agent collaborators for complex workflows
- ✅ Leverage Bob as an AI pair programmer
- ✅ Test and deploy agents to production

## Tips for Success

1. **Ask Bob for help**: Don't hesitate to ask Bob questions throughout the workshop
2. **Experiment**: Try modifying the examples to see what happens
3. **Read error messages**: They often tell you exactly what's wrong
4. **Test incrementally**: Build and test one feature at a time
5. **Use the documentation**: Bob can search the watsonx Orchestrate docs for you

## Additional Resources

- [watsonx Orchestrate Documentation](https://developer.watson-orchestrate.ibm.com/)
- [Python Tools Guide](https://developer.watson-orchestrate.ibm.com/tools/create_tool)
- [Agent Builder API Reference](https://developer.watson-orchestrate.ibm.com/apis/agents/)
- [Community Forum](https://community.ibm.com/community/user/watsonai/communities/community-home?CommunityKey=7a3dc5ba-3018-452d-9a43-a49dc6819633)

## Need Help?

- Ask Bob: "Bob, I'm stuck on [specific issue]"
- Check the solutions folder for reference implementations
- Review the bob-prompts guide for helpful prompts
- Consult the watsonx Orchestrate documentation

Let's get started! Head to [Part 1: Setup](./part1-setup/README.md) →