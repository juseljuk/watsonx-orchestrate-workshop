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

An agent specification is defined using YAML or JSON format. Here's what you need to know:

### Mandatory Fields

Every agent MUST have these four fields:

- **`spec_version`** (string): The specification version (e.g., "v1")
- **`kind`** (string): The agent type - "native", "external", or "assistant" (default: "native")
- **`name`** (string): Unique identifier for your agent
- **`llm`** (string): The large language model that powers the agent (e.g., "watsonx/ibm/granite-3-8b-instruct" or "groq/openai/gpt-oss-120b")

### Core Optional Fields

These fields define your agent's behavior and capabilities:

- **`description`** (string): Human-readable summary of the agent's purpose. This is visible in the UI and helps other agents understand its role when used as a collaborator
- **`instructions`** (string): Natural language guidance that shapes the agent's behavior, persona, and how it uses tools and collaborators
- **`style`** (string): Prompting structure - "default", "react", or "planner" (default: "default")
- **`hide_reasoning`** (boolean): Whether to hide the agent's reasoning from users (default: false)

### Extending Agent Capabilities

- **`tools`** (list<string>): Names of tools the agent can use to perform actions (OpenAPI definitions, Python functions, agentic workflows, or MCP server tools)
- **`collaborators`** (list<string>): Names of other agents this agent can delegate tasks to for solving complex problems
- **`knowledge_base`** (list<string>): Names of knowledge bases providing domain-specific information from uploaded files or vector data stores

### Advanced Configuration

- **`guidelines`** (list<object>): Rule-based behavior controls with:
  - `condition` (string, required): When to trigger the guideline
  - `action` (string, optional): What action to perform
  - `tool` (string, optional): Which tool to invoke
  
- **`restrictions`** (string): Whether the agent is "editable" or "non_editable" after import (default: "editable")
- **`icon`** (string): SVG icon string for the agent (64-100px square, max 200KB)

### Web Chat Features

- **`welcome_content`** (object): Configure the initial greeting
  - `welcome_message` (string): The welcome message shown to users
  - `description` (string): Subtitle text below the welcome message

- **`starter_prompts`** (object): Predefined prompts to help users start conversations
  - `prompts` (list): Up to 3 prompt tiles with title, subtitle, and prompt text

- **`chat_with_docs`** (object): Enable users to upload documents during chat
  - `enabled` (boolean): Activate document upload feature
  - `citations`: Configure how citations are displayed
  - `generation`: Fine-tune document handling behavior

### Context Variables

- **`context_access_enabled`** (boolean): Enable access to context variables from upstream systems (default: false)
- **`context_variables`** (list<string>): List of context variables the agent can access (e.g., wxo_email_id, wxo_user_name, wxo_tenant_id)

### Key Insight

The `instructions` field is the most critical part of your agent configuration. It defines the agent's personality, capabilities, and behavior patterns. Well-written instructions lead to predictable, helpful agent responses.

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