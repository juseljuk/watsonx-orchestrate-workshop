# Part 2 Exercises: Practice Building Agents

<p align="center">
  <img src="bobchestrate_exercises.png" alt="Bobchestrate - Exercises" width="700">
</p>

Complete these exercises to reinforce your understanding of agent creation. **Remember to use the `WXO Agent Architect` mode to create your agents.**

## Exercise 1: Personality Agent (Easy)

**Goal:** Create an agent with a unique personality

**Task:** Create a pirate-themed customer service agent that helps users but speaks like a pirate.

**Steps Needed:**<br>
1. Create agent yaml file<br>
2. Define the agent with appropriate instructions<br>
3. Import and test the agent

**Ask Bob for help:**
```
Bob, create a YAML file for a pirate-themed customer service agent that speaks like a pirate but is still helpful
```

**Test prompts:**<br>
- "Hello, I need help with my order"<br>
- "What can you do?"<br>
- "Thank you for your help"

>Reminder: Use `orchestrate agents import -f <your_agent_name>.yaml` to import your agent and `orchestrate chat ask --agent-name <your_agent_name>` to test it.

**Success criteria:**<br>
- Agent responds in pirate speak<br>
- Agent is still helpful and professional<br>
- Agent stays in character

---

## Exercise 2: Domain Expert Agent (Medium)

**Goal:** Create an agent that's an expert in a specific domain

**Task:** Create a Python programming expert agent that can answer coding questions.

**Requirements:**<br>
- Agent should introduce itself as a Python expert<br>
- Should provide code examples when relevant<br>
- Should explain concepts clearly<br>
- Should admit when questions are outside Python scope

**Ask Bob for help:**
```
Bob, create an agent that's a Python programming expert. It should provide code examples and explain concepts clearly.
```

**Test prompts:**<br>
- "What's the difference between a list and a tuple?"<br>
- "Show me how to read a CSV file"<br>
- "Explain decorators in Python"<br>
- "How do I deploy a Java application?" (out of scope)

**Success criteria:**<br>
- Provides accurate Python information<br>
- Includes code examples<br>
- Handles out-of-scope questions gracefully

---

## Exercise 3: Multi-lingual Agent (Medium)

**Goal:** Create an agent that can respond in multiple languages

**Task:** Modify the hello-agent to support English, Spanish, and French.

**Requirements:**<br>
- Agent should detect the user's language<br>
- Should respond in the same language<br>
- Should be able to switch languages mid-conversation

**Ask Bob for help:**
```
Bob, modify hello-agent.yaml to support English, Spanish, and French. The agent should detect and respond in the user's language.
```

**Test prompts:**<br>
- "Hello, how are you?"<br>
- "Hola, ¿cómo estás?"<br>
- "Bonjour, comment allez-vous?"<br>
- "Can you switch to Spanish?" (then continue in Spanish)

**Success criteria:**<br>
- Responds correctly in all three languages<br>
- Maintains context when switching languages<br>
- Provides natural translations

---

## Exercise 4: Structured Output Agent (Advanced)

**Goal:** Create an agent that returns responses in a specific format

**Task:** Create a "Product Recommender" agent that always returns recommendations in a structured format.

**Requirements:**<br>
- Agent should ask clarifying questions about user preferences<br>
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

**Test prompts:**<br>
- "I need a laptop for programming"<br>
- "Recommend a good book for learning Python"<br>
- "What's a good gift for a tech enthusiast?"

**Success criteria:**<br>
- Always uses the specified format<br>
- Provides relevant recommendations<br>
- Explains reasoning clearly

---

## Exercise 5: Conversational Flow Agent (Advanced)

**Goal:** Create an agent that guides users through a multi-step process

**Task:** Create a "Survey Agent" that collects user feedback through a series of questions.

**Requirements:**<br>
- Agent should introduce itself and explain the survey<br>
- Should ask questions one at a time<br>
- Should remember previous answers<br>
- Should thank the user at the end

**Questions to ask:**<br>
1. "How would you rate your experience? (1-5)"<br>
2. "What did you like most?"<br>
3. "What could be improved?"<br>
4. "Would you recommend us to others? (Yes/No)"

**Ask Bob for help:**
```
Bob, create a survey agent that asks users 4 questions one at a time and remembers their answers
```

**Test prompts:**<br>
- Start the conversation and go through all questions<br>
- Try to skip questions<br>
- Try to go back and change an answer

**Success criteria:**<br>
- Asks questions in order<br>
- Remembers all answers<br>
- Handles edge cases (skipping, changing answers)<br>
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

**Problems to find:**<br>
1. Instructions are too vague<br>
2. Invalid model name<br>
3. Agent is hidden (won't show in UI)<br>
4. Missing description details

**Ask Bob for help:**
```
Bob, review this agent YAML and identify all the problems: [paste YAML]
```

**Fix the agent and test it!**

---

## Reflection Questions

After completing the exercises, consider:

1. **What makes good agent instructions?**<br>
   - Specific role definition<br>
   - Clear capabilities and limitations<br>
   - Behavior guidelines<br>
   - Output format requirements

2. **How do you test agents effectively?**<br>
   - Use diverse test prompts<br>
   - Test edge cases<br>
   - Verify consistency<br>
   - Check error handling

3. **When should you create a new agent vs. modifying existing ones?**<br>
   - New domain/purpose → new agent<br>
   - Refinement/improvement → modify existing<br>
   - Different personality → could be either<br>

4. **How can Bob help you build better agents?**<br>
   - Generate initial YAML<br>
   - Review and improve instructions<br>
   - Debug issues<br>
   - Suggest test cases

---

## Next Steps

Once you've completed these exercises, you're ready to learn how to customize Bob's behavior with custom rules!

Continue to [Part 2b: Bob Custom Rules](../part2b-bob-custom-rules/README.md) →