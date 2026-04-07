# Bobchestrate Workshop - Building AI Agents with watsonx Orchestrate and IBM Bob

<p align="center">
  <img src="Bobchestrate_Workshop_logo_new.png" alt="Bobchestrate Workshop Logo" width="700">
</p>


## A Hands-On Workshop for Agentic AI Development

Welcome! This workshop will guide you through building AI agents using IBM watsonx Orchestrate. You'll use IBM Bob, an AI coding assistant, to help you along the way.

## Workshop Overview

**Duration:** 165-195 minutes

**Level:** Beginner to Intermediate

**Prerequisites:** 
- Computer with internet access, Windows, macOS, or Linux operating system, at least 8GB RAM and 500 MB of free disk space
- Basic Python knowledge and Python 3.11-3.13 installed (https://www.python.org/downloads/)
- uv installed (https://pypi.org/project/uv/)
- watsonx Orchestrate SaaS access (provided by your instructor or you can use your own)
- IBM Bob IDE installed (trial or one provided by your instructor)

## What You'll Build

Throughout this workshop, you'll build progressively more sophisticated AI agents:

### 1. Hello World Agent (Part 2)
Your first simple agent to understand the basics of agent configuration and behavior.

### 2. Customer Support System (Parts 3-5)
A complete customer support solution featuring:
- **Custom Python tools** for order status checking and refund processing
- **Knowledge base integration** for FAQ handling
- **Specialized escalation agent** for complex issues
- **Safety guidelines and guardrails** for responsible AI

### 3. Product Catalog System (Part 6)
An **MCP server-powered agent** that demonstrates backend integration:
- Product search and details
- Inventory checking
- Product recommendations
- Reusable MCP server architecture

### 4. Travel Planning System (Part 7)
A **multi-agent orchestration** showcasing advanced patterns:
- **Travel Concierge** (orchestrator) - Intelligent routing
- **Flight Specialist** - Flight bookings and search
- **Hotel Specialist** - Accommodation management
- **Activity Planner** - Local activities and attractions
- **Budget Advisor** - Cost analysis and optimization

Each system builds on concepts from previous parts, teaching you to create increasingly sophisticated agentic AI solutions.

## Workshop Structure

### [Part 1: Setup & Environment](./part1-setup/README.md) (15 min)
- Configure watsonx Orchestrate credentials
- Verify Bob is working as your AI development partner
- Understand the project structure
- Set up your development environment

### [Part 2: Building Your First Agent](./part2-first-agent/README.md) (20 min)
- Create a simple "Hello World" agent
- Understand agent instructions and behavior
- Test your agent with the chat interface
- Learn how to use Bob to help debug issues

### [Part 2b: Using Custom Rules with Bob IDE](./part2b-bob-custom-rules/README.md) (10 min)
- Learn how to configure Bob with custom development rules
- Understand the watsonx Orchestrate development rule
- Set up project-specific conventions for Bob
- Create your own custom rules for consistent development

### [Part 3: Adding Custom Tools](./part3-custom-tools/README.md) (30 min)
- Create a Python tool to check order status
- Create a tool to process refund requests
- Import tools into your agent
- Use Bob to help write and debug tool code

### [Part 4: Knowledge Bases & Collaborators](./part4-knowledge/README.md) (25 min)
- Add a knowledge base for FAQs
- Create a specialized escalation agent
- Connect agents as collaborators
- Test the complete customer support flow

### [Part 5: Agent Guidelines & Guardrails](./part5-guidelines-guardrails/README.md) (20 min)
- Write comprehensive agent guidelines
- Implement content safety guardrails
- Create input/output filtering plugins
- Test safety measures and compliance
- Learn responsible AI best practices

### [Part 6: MCP Servers - Connecting to Backend Services](./part6-mcp-servers/README.md) (25 min)
- Understand what MCP servers are and their benefits
- Create an MCP server in Python with multiple tools
- Define tool schemas and implement tool logic
- Import MCP servers into watsonx Orchestrate
- Use MCP server tools in your agents
- Learn MCP best practices and patterns

### [Part 7: Multi-Agent Orchestration & Workflows](./part7-multi-agent-orchestration/README.md) (30 min)
- Understand when and why to use multi-agent systems
- Design focused specialist agents for specific domains
- Create orchestrator agents with intelligent routing
- Manage context and handoffs between agents
- Implement complex multi-agent workflows
- Learn best practices for agent hierarchies

### [Part 8: Testing & Deployment](./part8-deployment/README.md) (20 min)
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
bobchestrate-workshop/
├── README.md (this file)
├── Bobchestrate_Workshop_logo_new.png
├── .bob/                                    # Bob IDE configuration
├── bob-prompts/
│   └── helpful-prompts.md                   # Useful Bob prompts for the workshop
│
├── part1-setup/                             # Setup & Environment (15 min)
│   ├── README.md
│   ├── verify-setup.py
│   ├── files/
│   │   └── wxo-agent-architect-export.yaml  # Pre-configured mode export
│   └── images/                              # Setup screenshots
│
├── part2-first-agent/                       # Building Your First Agent (20 min)
│   ├── README.md
│   ├── hello-agent-EXAMPLE.yaml
│   ├── exercises.md
│   └── images/
│
├── part2b-bob-custom-rules/                 # Using Custom Rules with Bob (10 min)
│   ├── README.md
│   ├── wxo-dev-rule.md
│   └── wxo-dev-rule-enhanced.md
│
├── part3-custom-tools/                      # Adding Custom Tools (30 min)
│   ├── README.md
│   ├── order_status_tool.py                 # Customer support tools
│   ├── refund_tool.py
│   ├── exercises.md
│   └── images/
│
├── part4-knowledge/                         # Knowledge Bases & Collaborators (25 min)
│   ├── README.md
│   ├── customer-support-agent.yaml          # Main support agent
│   ├── escalation-agent.yaml                # Specialized escalation agent
│   ├── faq-knowledge-base.yaml              # FAQ knowledge base
│   ├── FAQ.pdf                              # Sample FAQ document
│   └── images/
│
├── part5-guidelines-guardrails/             # Agent Guidelines & Guardrails (20 min)
│   ├── README.md
│   ├── customer-support-with-guidelines.yaml
│   └── content_safety_plugin.py             # Safety filtering plugin
│
├── part6-mcp-servers/                       # MCP Servers (25 min)
│   ├── README.md
│   ├── product_catalog_server.py            # MCP server implementation
│   ├── product-catalog-toolkit.yaml         # Toolkit configuration
│   ├── product-assistant-agent.yaml         # Agent using MCP tools
│   └── requirements.txt
│
├── part7-multi-agent-orchestration/         # Multi-Agent Orchestration (30 min)
│   ├── README.md
│   ├── travel-concierge-agent.yaml          # Orchestrator agent
│   ├── flight-specialist-agent.yaml         # Specialist agents
│   ├── hotel-specialist-agent.yaml
│   ├── activity-planner-agent.yaml
│   ├── budget-advisor-agent.yaml
│   ├── flight_tools.py                      # Domain-specific tools
│   └── hotel_tools.py
│
└── part8-deployment/                        # Testing & Deployment (20 min)
    ├── README.md
    ├── test-scenarios.md
    └── deployment-checklist.md
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
- ✅ Implement safety guidelines and guardrails
- ✅ Create and use MCP servers for backend integration
- ✅ Design and orchestrate multi-agent systems
- ✅ Build responsible AI agents
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