# Part 3b Exercises: AI Gateway and Model Selection

These exercises will help you master model selection and configuration in watsonx Orchestrate.

## Exercise 1: Model Performance Comparison (Easy)

**Objective:** Compare response quality across different models

**Task:**
1. Create three agents with identical instructions but different models:
   - Agent A: `granite-3.0-2b-instruct`
   - Agent B: `groq/openai/gpt-oss-120b`
   - Agent C: `llama-3-70b-instruct`

2. Test each with these queries:
   - "What's 15% of $299.99?"
   - "Explain your return policy in simple terms"
   - "I'm frustrated with my order delay. What can you do?"

3. Document:
   - Response time (approximate)
   - Response quality (1-5 rating)
   - Appropriateness for the query

**Success Criteria:**
- All three agents respond successfully
- You can identify clear differences in response style
- You understand which model is best for each query type

**Ask Bob:**
```
Bob, help me create a comparison test for three agents using different models, testing them with the same queries.
```

---

## Exercise 2: Cost-Optimized Agent Design (Medium)

**Objective:** Design an agent system that balances cost and performance

**Scenario:**
You have a customer support system that handles:
- 5,000 simple FAQ queries per day
- 2,000 standard support requests per day
- 500 complex escalations per day

**Task:**
1. Calculate estimated costs for:
   - Using `llama-3-70b-instruct` for everything
   - Using `granite-3.0-2b-instruct` for everything
   - Using a mixed approach with routing

2. Design a routing strategy that:
   - Minimizes cost
   - Maintains quality
   - Handles all query types appropriately

3. Create the routing agent and test it

**Success Criteria:**
- Cost calculation shows clear differences
- Routing agent correctly categorizes queries
- Quality is maintained for complex queries
- Cost is optimized for simple queries

**Ask Bob:**
```
Bob, help me design a cost-optimized multi-agent system with intelligent routing based on query complexity.
```

---

## Exercise 3: Domain-Specific Model Selection (Medium)

**Objective:** Choose appropriate models for different business domains

**Task:**
Create specialized agents for three different domains:

1. **Technical Support Agent**
   - Handles technical troubleshooting
   - Needs to understand complex technical concepts
   - Must provide detailed, accurate solutions

2. **Sales Agent**
   - Handles product inquiries
   - Needs to be persuasive and creative
   - Must understand customer needs

3. **Billing Agent**
   - Handles payment and billing questions
   - Needs to be precise with numbers
   - Must follow strict policies

For each agent:
- Choose the most appropriate model
- Justify your choice
- Create the agent YAML
- Test with domain-specific queries

**Success Criteria:**
- Each agent uses an appropriate model for its domain
- You can explain why each model was chosen
- Agents perform well in their respective domains
- Model choices are cost-effective

**Ask Bob:**
```
Bob, help me design three domain-specific agents with appropriate model selections for technical support, sales, and billing.
```

---

## Exercise 4: Advanced Router with Context (Hard)

**Objective:** Create an intelligent router that considers multiple factors

**Task:**
Build a sophisticated routing agent that considers:
- Query complexity
- Customer sentiment (frustrated, neutral, happy)
- Query type (question, complaint, request)
- Time sensitivity (urgent vs. routine)

The router should:
1. Analyze the incoming query
2. Determine the best agent/model combination
3. Provide context to the selected agent
4. Handle edge cases gracefully

**Success Criteria:**
- Router correctly analyzes multiple factors
- Routing decisions are logical and documented
- Edge cases are handled appropriately
- System maintains quality while optimizing cost

**Ask Bob:**
```
Bob, create an advanced routing agent that analyzes query complexity, customer sentiment, and urgency to select the optimal support agent.
```

---

## Exercise 5: Model Parameter Tuning (Hard)

**Objective:** Optimize model parameters for specific use cases

**Task:**
Experiment with model parameters to optimize for different scenarios:

1. **Creative Writing Agent**
   - Adjust temperature for creativity
   - Test with product descriptions
   - Find optimal balance

2. **Data Extraction Agent**
   - Adjust temperature for consistency
   - Test with structured data extraction
   - Minimize hallucinations

3. **Conversational Agent**
   - Balance creativity and accuracy
   - Test with customer conversations
   - Optimize for natural dialogue

For each:
- Test different temperature settings (0.0, 0.3, 0.7, 1.0)
- Document the impact on responses
- Choose optimal settings

**Success Criteria:**
- You understand how temperature affects responses
- Each agent has optimized parameters
- You can explain the tradeoffs
- Agents perform better with tuned parameters

**Ask Bob:**
```
Bob, help me create test agents with different temperature settings to understand how parameters affect model behavior.
```

---

## Exercise 6: Multi-Model Workflow (Advanced)

**Objective:** Design a workflow that uses different models at different stages

**Scenario:**
Create a customer support workflow that:
1. Uses a fast model for initial triage
2. Uses a balanced model for standard handling
3. Uses an advanced model for complex resolution
4. Uses a fast model for follow-up confirmation

**Task:**
1. Design the workflow architecture
2. Create all necessary agents
3. Implement handoffs between stages
4. Test the complete flow
5. Measure performance and cost

**Success Criteria:**
- Workflow uses appropriate models at each stage
- Handoffs are smooth and maintain context
- Overall cost is optimized
- Quality is maintained throughout
- You can explain the design decisions

**Ask Bob:**
```
Bob, design a multi-stage customer support workflow that uses different models at different stages, optimizing for both cost and quality.
```

---

## Exercise 7: Model Fallback Strategy (Advanced)

**Objective:** Implement robust error handling with model fallbacks

**Task:**
Create an agent system with fallback strategies:

1. **Primary Model:** `llama-3-70b-instruct`
   - High quality, but may be slow or unavailable

2. **Fallback Model:** `groq/openai/gpt-oss-120b`
   - Good balance, reliable

3. **Emergency Fallback:** `granite-3.0-8b-instruct`
   - Always available, fast

Implement:
- Automatic fallback on errors
- Timeout handling
- Quality monitoring
- Graceful degradation

**Success Criteria:**
- System handles model failures gracefully
- Fallback logic is clear and documented
- User experience remains good even with fallbacks
- System logs fallback events for monitoring

**Ask Bob:**
```
Bob, help me implement a robust agent system with automatic fallback to alternative models when the primary model fails or times out.
```

---

## Bonus Challenge: Real-World Optimization

**Objective:** Apply everything you've learned to a real scenario

**Scenario:**
You're building a customer service system for an e-commerce company with:
- 50,000 daily interactions
- Budget of $500/month for AI models
- Quality requirements: 95% customer satisfaction
- Response time requirement: < 3 seconds average

**Task:**
1. Design the complete agent architecture
2. Select models for each component
3. Calculate projected costs
4. Implement the system
5. Test and optimize
6. Document your decisions

**Success Criteria:**
- System meets all requirements
- Stays within budget
- Maintains quality standards
- Response times are acceptable
- Design is scalable and maintainable

**Ask Bob:**
```
Bob, help me design and implement a complete, production-ready customer service system that meets specific budget, quality, and performance requirements.
```

---

## Tips for Success

1. **Start Simple:** Begin with basic model comparisons before tackling complex routing
2. **Measure Everything:** Track response time, quality, and cost for all experiments
3. **Use Bob:** Ask Bob to help analyze results and suggest improvements
4. **Document Decisions:** Keep notes on why you chose specific models
5. **Test Thoroughly:** Use realistic queries and scenarios
6. **Iterate:** Refine your approach based on test results

## Additional Resources

- [Model Selection Guide](https://developer.watson-orchestrate.ibm.com/models/selection)
- [Cost Optimization Best Practices](https://developer.watson-orchestrate.ibm.com/models/cost_optimization)
- [Performance Tuning](https://developer.watson-orchestrate.ibm.com/models/performance)

---

**Remember:** The best model choice depends on your specific use case, budget, and quality requirements. There's no one-size-fits-all solution!