# Part 2 Exercises: Practice Building Agents

Complete these exercises to reinforce your understanding of agent creation. **Remember to use the `WXO Agent Architect` mode to create your agents.**

## Exercise 1: Personality Agent (Easy)

**Goal:** Create an agent with a unique personality

**Task:** Create a pirate-themed customer service agent that helps users but speaks like a pirate.

**Steps Needed:**
1. Create agent yaml file
2. Define the agent with appropriate instructions
3. Import and test the agent

**Ask Bob for help:**
```
Bob, create a YAML file for a pirate-themed customer service agent that speaks like a pirate but is still helpful
```

**Test prompts:**
- "Hello, I need help with my order"
- "What can you do?"
- "Thank you for your help"

>Reminder: Use `orchestrate agents import -f <your_agent_name>.yaml` to import your agent and `orchestrate chat ask --agent-name <your_agent_name>` to test it.

**Success criteria:**
- Agent responds in pirate speak
- Agent is still helpful and professional
- Agent stays in character

---

## Exercise 2: Domain Expert Agent (Medium)

**Goal:** Create an agent that's an expert in a specific domain

**Task:** Create a Python programming expert agent that can answer coding questions.

**Requirements:**
- Agent should introduce itself as a Python expert
- Should provide code examples when relevant
- Should explain concepts clearly
- Should admit when questions are outside Python scope

**Ask Bob for help:**
```
Bob, create an agent that's a Python programming expert. It should provide code examples and explain concepts clearly.
```

**Test prompts:**
- "What's the difference between a list and a tuple?"
- "Show me how to read a CSV file"
- "Explain decorators in Python"
- "How do I deploy a Java application?" (out of scope)

**Success criteria:**
- Provides accurate Python information
- Includes code examples
- Handles out-of-scope questions gracefully

---

## Exercise 3: Multi-lingual Agent (Medium)

**Goal:** Create an agent that can respond in multiple languages

**Task:** Modify the hello-agent to support English, Spanish, and French.

**Requirements:**
- Agent should detect the user's language
- Should respond in the same language
- Should be able to switch languages mid-conversation

**Ask Bob for help:**
```
Bob, modify hello-agent.yaml to support English, Spanish, and French. The agent should detect and respond in the user's language.
```

**Test prompts:**
- "Hello, how are you?"
- "Hola, ¿cómo estás?"
- "Bonjour, comment allez-vous?"
- "Can you switch to Spanish?" (then continue in Spanish)

**Success criteria:**
- Responds correctly in all three languages
- Maintains context when switching languages
- Provides natural translations

---

## Exercise 4: Structured Output Agent (Advanced)

**Goal:** Create an agent that returns responses in a specific format

**Task:** Create a "Product Recommender" agent that always returns recommendations in a structured format.

**Requirements:**
- Agent should ask clarifying questions about user preferences
- Should return recommendations in this format:
  ```
  Product: [name]
  Price: [price]
  Rating: [rating]
  Why: [reason]
  ```
- Should recommend 2-3 products

**Ask Bob for help:**
```
Bob, create an agent that recommends products and always formats responses with Product, Price, Rating, and Why fields
```

**Test prompts:**
- "I need a laptop for programming"
- "Recommend a good book for learning Python"
- "What's a good gift for a tech enthusiast?"

**Success criteria:**
- Always uses the specified format
- Provides relevant recommendations
- Explains reasoning clearly

---

## Exercise 5: Conversational Flow Agent (Advanced)

**Goal:** Create an agent that guides users through a multi-step process

**Task:** Create a "Survey Agent" that collects user feedback through a series of questions.

**Requirements:**
- Agent should introduce itself and explain the survey
- Should ask questions one at a time
- Should remember previous answers
- Should thank the user at the end

**Questions to ask:**
1. "How would you rate your experience? (1-5)"
2. "What did you like most?"
3. "What could be improved?"
4. "Would you recommend us to others? (Yes/No)"

**Ask Bob for help:**
```
Bob, create a survey agent that asks users 4 questions one at a time and remembers their answers
```

**Test prompts:**
- Start the conversation and go through all questions
- Try to skip questions
- Try to go back and change an answer

**Success criteria:**
- Asks questions in order
- Remembers all answers
- Handles edge cases (skipping, changing answers)
- Provides a summary at the end

---

## Bonus Challenge: Debug This Agent

**Goal:** Practice debugging agent issues

**Task:** This agent has several problems. Find and fix them!

```yaml
kind: native
name: broken-agent
description: An agent that doesn't work properly
instructions: |
  You are a helpful assistant.
  
llm: invalid-model-name
config:
  hidden: true
```

**Problems to find:**
1. Instructions are too vague
2. Invalid model name
3. Agent is hidden (won't show in UI)
4. Missing description details

**Ask Bob for help:**
```
Bob, review this agent YAML and identify all the problems: [paste YAML]
```

**Fix the agent and test it!**

---

## Reflection Questions

After completing the exercises, consider:

1. **What makes good agent instructions?**
   - Specific role definition
   - Clear capabilities and limitations
   - Behavior guidelines
   - Output format requirements

2. **How do you test agents effectively?**
   - Use diverse test prompts
   - Test edge cases
   - Verify consistency
   - Check error handling

3. **When should you create a new agent vs. modifying existing ones?**
   - New domain/purpose → new agent
   - Refinement/improvement → modify existing
   - Different personality → could be either

4. **How can Bob help you build better agents?**
   - Generate initial YAML
   - Review and improve instructions
   - Debug issues
   - Suggest test cases

---

## Next Steps

Once you've completed these exercises, you're ready to learn how to customize Bob's behavior with custom rules!

Continue to [Part 2b: Bob Custom Rules](../part2b-bob-custom-rules/README.md) →