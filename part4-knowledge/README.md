# Part 4: Knowledge Bases & Collaborators

**Duration:** 25 minutes  
**Objective:** Add knowledge bases for FAQ handling and create specialized collaborator agents

## What You'll Learn

- How to create and configure knowledge bases
- Connecting knowledge bases to agents
- Creating specialized collaborator agents
- Building agent hierarchies for complex workflows

## Knowledge Bases Overview

Knowledge bases allow agents to:
- 📚 Access large amounts of information without including it in instructions
- 🔍 Retrieve relevant information based on user queries
- 📝 Answer questions from documents, FAQs, and knowledge articles
- 🎯 Provide accurate, sourced responses

## Step 1: Create a Knowledge Base

Let's create a simple FAQ knowledge base for our customer support agent.

### Create FAQ Documents

First, create some sample FAQ content. Use the example provided below or create your own using Bob! Bob prompt provided after the example.

```yaml
# faq-knowledge-base.yaml
kind: knowledge_base
name: customer-support-faq
description: Frequently asked questions for customer support

documents:
  - title: "Shipping Policy"
    content: |
      # Shipping Policy
      
      ## Domestic Shipping
      - Standard shipping: 5-7 business days ($5.99)
      - Express shipping: 2-3 business days ($12.99)
      - Overnight shipping: 1 business day ($24.99)
      
      ## International Shipping
      - International standard: 10-15 business days ($19.99)
      - International express: 5-7 business days ($39.99)
      
      ## Free Shipping
      Orders over $50 qualify for free standard shipping within the US.
      
  - title: "Return Policy"
    content: |
      # Return Policy
      
      ## Return Window
      You can return most items within 30 days of delivery for a full refund.
      
      ## Return Process
      1. Contact customer support to initiate a return
      2. Receive a return authorization number
      3. Ship the item back using the provided label
      4. Refund processed within 5-7 business days after receipt
      
      ## Non-Returnable Items
      - Opened software or digital products
      - Personalized items
      - Gift cards
      
  - title: "Payment Methods"
    content: |
      # Payment Methods
      
      We accept:
      - Credit cards (Visa, MasterCard, American Express, Discover)
      - Debit cards
      - PayPal
      - Apple Pay
      - Google Pay
      
      ## Payment Security
      All transactions are encrypted and secure. We never store your full
      credit card information.
      
  - title: "Account Management"
    content: |
      # Account Management
      
      ## Creating an Account
      Click "Sign Up" and provide your email and password.
      
      ## Resetting Password
      Click "Forgot Password" on the login page and follow the email instructions.
      
      ## Updating Profile
      Go to Account Settings to update your name, email, address, and preferences.
      
      ## Deleting Account
      Contact customer support to request account deletion. This process takes
      3-5 business days.

```

### Ask Bob to Help:
```
Bob, create a knowledge base YAML file with FAQs about shipping, returns, payments, and account management
```

## Step 2: Import the Knowledge Base

Import your knowledge base:

```bash
orchestrate knowledge-bases import faq-knowledge-base.yaml
```

Check the status:
```bash
orchestrate knowledge-bases list
orchestrate knowledge-bases status customer-support-faq
```

Wait for the knowledge base to be indexed (status: "ready").

## Step 3: Connect Knowledge Base to Agent

Update your customer support agent to use the knowledge base:

```yaml
# customer-support-agent.yaml
kind: native
name: customer-support-agent
description: A customer support agent that can check orders, process refunds, and answer FAQs

instructions: |
  You are a helpful customer support agent for an e-commerce company.
  
  Your capabilities:
  - Check order status using the check_order_status tool
  - Process refund requests using the process_refund tool
  - Answer questions using the customer-support-faq knowledge base
  
  When answering questions:
  1. First check if the information is in your knowledge base
  2. Provide accurate, helpful answers based on the knowledge base
  3. If the information isn't available, politely say so and offer to escalate
  
  When handling orders and refunds:
  1. Use the appropriate tools
  2. Present information clearly
  3. Be empathetic and professional
  
  Always prioritize customer satisfaction while following company policies.

llm: groq/openai/gpt-oss-120b

# Tools this agent can use
tools:
  - check_order_status
  - process_refund

# Knowledge bases this agent can access
knowledge_base:
  - customer-support-faq

config:
  hidden: false
  enable_cot: false
```

Re-import the agent:
```bash
orchestrate agents import customer-support-agent.yaml
```

## Step 4: Test Knowledge Base Integration

Test the agent with FAQ questions:

```bash
orchestrate chat --agent customer-support-agent
```

Try these questions:
- "What's your shipping policy?"
- "How do I return an item?"
- "What payment methods do you accept?"
- "How long does standard shipping take?"

The agent should retrieve and present information from the knowledge base!

## Step 5: Create a Specialized Escalation Agent

Now let's create a specialized agent for handling complex issues:

```yaml
# escalation-agent.yaml
kind: native
name: escalation-agent
description: Handles complex customer issues that require manager approval or special handling

instructions: |
  You are a senior customer support specialist who handles escalated issues.
  
  Your role:
  - Handle complex refund requests over $10,000
  - Resolve customer complaints
  - Make exceptions to standard policies when appropriate
  - Provide detailed investigation of issues
  
  When handling escalations:
  1. Acknowledge the customer's frustration
  2. Gather all relevant details
  3. Explain what you can do to help
  4. Provide clear next steps and timelines
  5. Follow up to ensure resolution
  
  You have authority to:
  - Approve refunds up to $25,000
  - Offer compensation (discounts, credits)
  - Override standard policies in exceptional cases
  - Expedite shipping at no charge
  
  Always document your decisions and reasoning. Be empathetic but maintain
  professional boundaries.

llm: groq/openai/gpt-oss-120b

# This agent can use the same tools
tools:
  - check_order_status
  - process_refund

# And access the same knowledge base
knowledge_base:
  - customer-support-faq

config:
  hidden: false
  enable_cot: true  # Enable chain-of-thought for complex reasoning
```

Import the escalation agent:
```bash
orchestrate agents import escalation-agent.yaml
```

## Step 6: Create Agent Collaboration

Update the main customer support agent to collaborate with the escalation agent:

```yaml
# customer-support-agent.yaml (updated)
kind: native
name: customer-support-agent
description: A customer support agent that can check orders, process refunds, and answer FAQs

instructions: |
  You are a helpful customer support agent for an e-commerce company.
  
  Your capabilities:
  - Check order status using the check_order_status tool
  - Process refund requests using the process_refund tool (up to $10,000)
  - Answer questions using the customer-support-faq knowledge base
  - Escalate complex issues to the escalation-agent
  
  When to escalate to escalation-agent:
  - Refund requests over $10,000
  - Customer is very upset or threatening legal action
  - Request requires policy exception
  - Issue is beyond your authority
  - Customer specifically requests a manager
  
  When escalating:
  1. Explain to the customer that you're connecting them with a specialist
  2. Summarize the issue for the escalation agent
  3. Let the escalation agent take over
  
  For routine matters, handle them yourself efficiently and professionally.

llm: groq/openai/gpt-oss-120b

tools:
  - check_order_status
  - process_refund

knowledge_base:
  - customer-support-faq

# Add the escalation agent as a collaborator
collaborators:
  - escalation-agent

config:
  hidden: false
  enable_cot: false
```

Re-import:
```bash
orchestrate agents import customer-support-agent.yaml
```

## Step 7: Test Agent Collaboration

Test the collaboration:

```bash
orchestrate chat --agent customer-support-agent
```

Try these scenarios:

**Scenario 1: Routine Question (handled by main agent)**
```
User: What's your return policy?
```

**Scenario 2: Standard Refund (handled by main agent)**
```
User: I need a refund for order ORD-12345. The item was damaged. Amount is $99.99.
```

**Scenario 3: Large Refund (escalated)**
```
User: I need a refund for order ORD-67890. The entire shipment was wrong. Amount is $15,000.
```

The agent should recognize this needs escalation and delegate to the escalation-agent!

## Step 8: Advanced Knowledge Base Features

### Multiple Knowledge Bases

You can create specialized knowledge bases:

```yaml
# technical-kb.yaml
kind: knowledge_base
name: technical-support-kb
description: Technical troubleshooting guides

documents:
  - title: "Device Setup"
    content: |
      # Device Setup Guide
      [Technical content here]
      
  - title: "Troubleshooting"
    content: |
      # Common Issues
      [Troubleshooting steps here]
```

Then assign different knowledge bases to different agents:

```yaml
# technical-support-agent.yaml
knowledge_base:
  - technical-support-kb
  - customer-support-faq  # Can access multiple KBs
```

### Ask Bob for Help:
```
Bob, create a technical support knowledge base with troubleshooting guides
```

## Best Practices

### Knowledge Base Best Practices

✅ **DO:**
- Organize content into clear, focused documents
- Use descriptive titles
- Include relevant keywords
- Keep documents updated
- Test retrieval with common queries

❌ **DON'T:**
- Create overly large documents
- Mix unrelated topics in one document
- Use vague titles
- Include outdated information
- Forget to re-index after updates

### Collaboration Best Practices

✅ **DO:**
- Define clear escalation criteria
- Provide context when delegating
- Create specialized agents for specific domains
- Test collaboration flows thoroughly
- Document agent responsibilities

❌ **DON'T:**
- Create circular delegation loops
- Make escalation criteria too vague
- Give all agents the same capabilities
- Forget to handle delegation failures
- Create too many layers of agents

## Common Issues

### Issue: Knowledge base not returning relevant results
**Solution:** 
- Check document titles and content
- Verify knowledge base is indexed (status: "ready")
- Try rephrasing the query
- Adjust chunk_size and chunk_overlap

### Issue: Agent not delegating to collaborator
**Solution:**
- Check collaborator is listed in agent YAML
- Review escalation criteria in instructions
- Verify collaborator agent exists
- Test with clear escalation scenarios

### Issue: Collaborator agent not accessible
**Solution:**
```bash
orchestrate agents list
# Verify both agents are imported
```

## Exercises

### Exercise 1: Product Catalog Knowledge Base
Create a knowledge base with product information and connect it to a sales agent.

**Ask Bob:**
```
Bob, create a product catalog knowledge base with 5 products and a sales agent that uses it
```

### Exercise 2: Multi-Agent System
Create a system with 3 agents: front-line support, technical support, and billing support.

**Ask Bob:**
```
Bob, design a multi-agent customer service system with specialized agents for different departments
```

### Exercise 3: Knowledge Base Optimization
Improve the FAQ knowledge base by adding more detailed content and better organization.

**Ask Bob:**
```
Bob, review my knowledge base and suggest improvements for better retrieval
```

## Key Takeaways

✅ Knowledge bases provide agents with access to large information sources  
✅ Agents can collaborate by delegating to specialized agents  
✅ Clear escalation criteria are essential for effective collaboration  
✅ Multiple knowledge bases can be used for different domains  
✅ Bob can help design and optimize agent hierarchies  

## Next Steps

You've built a complete customer support system! Now let's test and deploy it.

Continue to [Part 5: Testing & Deployment](../part5-deployment/README.md) →

## Additional Resources

- [Knowledge Base Guide](https://developer.watson-orchestrate.ibm.com/knowledge_bases/overview)
- [Agent Collaboration Patterns](https://developer.watson-orchestrate.ibm.com/agents/collaboration)
- [Best Practices for Multi-Agent Systems](https://developer.watson-orchestrate.ibm.com/agents/best_practices)

---

**💡 Pro Tip:** Use Bob to help design your agent hierarchy. Ask: "Bob, design an agent system for [your use case]"