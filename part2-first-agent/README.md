# Part 2: Building Your First Agent

**Duration:** 20 minutes  
**Objective:** Create a simple agent and understand the basics of agent configuration

## What You'll Learn

- How to create an agent using YAML specification
- Understanding agent instructions and behavior
- Testing your agent with the chat interface
- Using Bob to help debug and improve your agent

## Agent Basics

A watsonx Orchestrate agent is an AI assistant that can:
- Understand natural language
- Execute tasks using tools
- Collaborate with other agents
- Access knowledge bases
- Follow specific instructions

## Step 1: Understanding Agent Structure

An agent specification includes:
- **name**: Unique identifier for your agent
- **description**: What the agent does (used for routing)
- **instructions**: How the agent should behave
- **tools**: Functions the agent can call
- **collaborators**: Other agents it can delegate to
- **knowledge_base**: Information sources it can query

## Step 2: Create Your First Agent

Let's create a simple "Hello World" agent.

### Ask Bob to Help:
```
Bob, create a YAML file called hello-agent.yaml that defines a simple watsonx Orchestrate agent that greets users and tells them about itself
```

Or create it manually:

```yaml
# hello-agent.yaml
kind: native
name: hello-world-agent
description: A friendly agent that greets users and introduces itself
instructions: |
  You are a friendly AI assistant named HelloBot. Your role is to:
  
  1. Greet users warmly when they first interact with you
  2. Introduce yourself and explain what you can do
  3. Answer questions about watsonx Orchestrate
  4. Be helpful, concise, and friendly
  
  When greeting users, mention that you're a demo agent created in a workshop.
  Keep your responses brief and engaging.

# Optional: Specify the LLM model to use
llm: groq/openai/gpt-oss-120b

# Optional: Agent configuration
config:
  hidden: false
  enable_cot: false
```

## Step 3: Import Your Agent

Use the watsonx Orchestrate CLI to import your agent:

```bash
orchestrate agents import hello-agent.yaml
```

You should see:
```
✅ Successfully imported agent: hello-world-agent
```

### Using Bob:
```
Bob, help me import the hello-agent.yaml file into watsonx Orchestrate
```

## Step 4: Test Your Agent

### Option A: Using the CLI Chat Interface

```bash
orchestrate chat --agent hello-world-agent
```

Try these test messages:
- "Hello!"
- "What can you do?"
- "Tell me about watsonx Orchestrate"

Type `exit` or press Ctrl+C to quit.

### Option B: Using Python

Create a test script:

```python
# test-hello-agent.py
from ibm_watsonx_orchestrate import AgentBuilder

def test_agent():
    builder = AgentBuilder()
    
    # Start a conversation
    response = builder.chat_with_agent(
        agent_name="hello-world-agent",
        message="Hello! What can you do?"
    )
    
    print(f"Agent: {response['message']}")
    print(f"Thread ID: {response['thread_id']}")
    
    # Continue the conversation
    response = builder.chat_with_agent(
        agent_name="hello-world-agent",
        message="Tell me more about watsonx Orchestrate",
        thread_id=response['thread_id']
    )
    
    print(f"\nAgent: {response['message']}")

if __name__ == "__main__":
    test_agent()
```

Run it:
```bash
python test-hello-agent.py
```

## Step 5: Understanding Agent Instructions

The `instructions` field is crucial - it defines your agent's behavior.

### Good Instructions Include:
✅ **Role definition**: "You are a customer support agent..."  
✅ **Capabilities**: "You can check orders, process refunds..."  
✅ **Behavior guidelines**: "Be professional and empathetic..."  
✅ **Output format**: "Provide answers in bullet points..."  
✅ **Limitations**: "If you can't help, escalate to..."  

### Example: Improving Instructions

**Ask Bob:**
```
Bob, improve the instructions in hello-agent.yaml to make the agent more helpful and specific about what it can do in this workshop context
```

Bob might suggest something like:

```yaml
instructions: |
  You are HelloBot, a friendly AI assistant created as part of a watsonx Orchestrate workshop.
  
  Your purpose is to:
  - Welcome users to the workshop
  - Explain what watsonx Orchestrate agents can do
  - Answer questions about agent capabilities
  - Provide examples of how agents work
  
  When users ask what you can do, explain that you're a simple demonstration agent
  showing the basics of agent creation. Mention that more advanced agents can:
  - Call custom tools to perform actions
  - Access knowledge bases for information
  - Collaborate with other specialized agents
  - Integrate with external systems
  
  Keep responses concise (2-3 sentences) and encouraging. If asked about topics
  outside your scope, politely explain your limitations and suggest they'll learn
  more in later workshop sections.
```

## Step 6: Update Your Agent

After modifying the YAML file, re-import it:

```bash
orchestrate agents import hello-agent.yaml
```

The agent will be updated with your new instructions. Test it again to see the difference!

## Step 7: View Your Agent Details

List all agents:
```bash
orchestrate agents list
```

Get detailed information about your agent:
```bash
orchestrate agents get hello-world-agent
```

## Common Issues and Solutions

### Issue: "Agent not found"
**Solution:** Check the agent name is correct:
```bash
orchestrate agents list
```

### Issue: Agent gives unexpected responses
**Solution:** Review and refine your instructions. Ask Bob:
```
Bob, why might my agent be giving unexpected responses? Here are the instructions: [paste instructions]
```

### Issue: Import fails with validation error
**Solution:** Check your YAML syntax:
```
Bob, check this YAML file for syntax errors: [paste YAML]
```

## Exercises

Try these exercises to practice:

### Exercise 1: Personality Agent
Create an agent with a specific personality (e.g., pirate, Shakespeare, tech guru).

**Ask Bob:**
```
Bob, create an agent YAML file for a pirate-themed customer service agent
```

### Exercise 2: Domain Expert
Create an agent that's an expert in a specific domain (e.g., Python programming, cooking, fitness).

**Ask Bob:**
```
Bob, create an agent that's a Python programming expert who can answer coding questions
```

### Exercise 3: Multi-lingual Agent
Create an agent that can respond in multiple languages.

**Ask Bob:**
```
Bob, modify hello-agent.yaml to support English, Spanish, and French
```

## Key Takeaways

✅ Agents are defined using YAML specifications  
✅ Instructions are the most important part of agent configuration  
✅ Agents can be tested via CLI or Python  
✅ Bob can help you create, debug, and improve agents  
✅ Agents can be updated by re-importing the YAML file  

## Next Steps

Now that you understand basic agents, you're ready to make them more powerful by adding custom tools!

Continue to [Part 3: Adding Custom Tools](../part3-custom-tools/README.md) →

## Additional Resources

- [Agent Configuration Reference](https://developer.watson-orchestrate.ibm.com/agents/configuration)
- [Writing Effective Instructions](https://developer.watson-orchestrate.ibm.com/agents/instructions)
- [Agent Styles Guide](https://developer.watson-orchestrate.ibm.com/agents/styles)

---

**💡 Pro Tip:** Use Bob to iterate on your agent instructions. Ask Bob to review and improve them based on your specific use case!