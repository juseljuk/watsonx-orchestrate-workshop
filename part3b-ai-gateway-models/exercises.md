# Part 3b Exercises: AI Gateway and Model Policies

These exercises will help you master AI Gateway configuration, external model providers, and model policies in watsonx Orchestrate.

## Exercise 1: Configure AI Gateway (Easy)

**Objective:** Set up and test AI Gateway configuration

**Task:**
1. List currently available models in your environment:
   ```bash
   orchestrate models list
   ```

2. View AI Gateway configuration:
   ```bash
   orchestrate gateway config show
   ```

3. Create a basic agent using the default model:
   ```yaml
   spec_version: v1
   kind: native
   name: test_agent_<your_initials>
   description: Test agent for AI Gateway
   
   instructions: |
     You are a helpful assistant.
   
   llm: groq/openai/gpt-oss-120b
   ```

4. Test the agent with simple queries

**Success Criteria:**
- You can view available models
- You understand the AI Gateway configuration
- Your agent responds successfully
- You can explain the model provider architecture

**Ask Bob:**
```
Bob, help me understand the AI Gateway configuration and create a test agent using the default model.
```

---

## Exercise 2: Create Model Policies (Medium)

**Objective:** Create and apply model policies for load balancing and fallback

**Task:**
1. Create a fallback model policy:
   ```yaml
   # fallback-policy.yaml
   spec_version: v1
   kind: model
   name: dev_resilient_gpt
   description: Fallback policy for development
   display_name: Dev Resilient GPT
   
   policy:
     strategy:
       mode: fallback
     retry:
       attempts: 2
       on_status_codes: [503, 500]
     targets:
       - model_name: groq/openai/gpt-oss-120b
       - model_name: aws-bedrock/gpt-oss-120b
   ```

2. Import the policy:
   ```bash
   orchestrate models policy import --file fallback-policy.yaml
   ```

3. Create an agent that uses this policy:
   ```yaml
   spec_version: v1
   kind: native
   name: test_agent_with_policy
   description: Agent using fallback policy
   
   instructions: |
     You are a helpful assistant.
   
   llm: dev_resilient_gpt  # References the policy
   ```

4. Test the policy by simulating failures

**Success Criteria:**
- Policy is properly created and imported
- Agent successfully uses the policy
- You understand fallback behavior
- You can explain when fallback occurs

**Ask Bob:**
```
Bob, help me create a fallback model policy that automatically switches to a backup model when the primary fails.
```

---

## Exercise 3: External Provider Configuration (Medium)

**Objective:** Configure an external model provider through AI Gateway

**Scenario:**
Your team wants to use OpenAI's GPT-4 for specific high-value use cases while keeping the default model for standard operations.

**Task:**
1. Research the requirements for connecting OpenAI to AI Gateway

2. Create a provider configuration (conceptual):
   ```yaml
   # openai-provider.yaml
   providers:
     - name: openai
       type: openai
       api_key: ${OPENAI_API_KEY}
       models:
         - gpt-4-turbo
         - gpt-3.5-turbo
       default_model: gpt-4-turbo
   ```

3. Create two agents:
   - Standard agent using default model
   - Premium agent using external OpenAI model

4. Compare their capabilities and costs

**Success Criteria:**
- You understand external provider configuration
- You can explain the security considerations
- You know when to use external vs. default models
- You can estimate cost differences

**Ask Bob:**
```
Bob, help me understand how to configure an external model provider like OpenAI through the AI Gateway, including security best practices.
```

---

## Exercise 4: Cost Optimization Strategy (Hard)

**Objective:** Design a cost-effective multi-agent system

**Scenario:**
You're building a customer service system that handles:
- 10,000 simple FAQ queries per day
- 3,000 standard support requests per day
- 500 complex escalations per day

Budget constraint: $100/day

**Task:**
1. Research pricing for:
   - Default model (groq/openai/gpt-oss-120b)
   - External models (if needed)

2. Design a tiered architecture:
   - Tier 1: FAQ bot (simple queries)
   - Tier 2: Standard support (typical requests)
   - Tier 3: Expert support (complex cases)

3. Calculate projected costs for:
   - All queries using default model
   - Tiered approach with routing
   - Mixed approach with external models

4. Implement the most cost-effective solution

5. Create policies to enforce budget limits

**Success Criteria:**
- Cost projections are realistic
- Architecture stays within budget
- Quality is maintained for all tiers
- Policies enforce cost controls
- You can explain the tradeoffs

**Ask Bob:**
```
Bob, help me design a cost-optimized multi-tier customer service system that handles different query complexities while staying within a $100/day budget.
```

---

## Exercise 5: Monitoring and Governance (Hard)

**Objective:** Implement comprehensive monitoring and governance

**Task:**
1. Set up monitoring for:
   - Model usage by agent
   - Cost per agent/model
   - Policy violations
   - Response times
   - Error rates

2. Create alert configurations:
   ```yaml
   # alerts-config.yaml
   alerts:
     - name: high_cost_alert
       condition: daily_cost > 80
       action: email
       recipients:
         - admin@company.com
     
     - name: rate_limit_alert
       condition: rate_limit_exceeded
       action: slack
       channel: "#ai-ops"
     
     - name: policy_violation_alert
       condition: policy_violation
       action: pagerduty
       severity: high
   ```

3. Create a dashboard showing:
   - Daily/weekly usage trends
   - Cost breakdown by model
   - Policy compliance metrics
   - Performance metrics

4. Document governance procedures

**Success Criteria:**
- Monitoring captures all key metrics
- Alerts are properly configured
- Dashboard provides actionable insights
- Governance procedures are documented
- You can respond to alerts effectively

**Ask Bob:**
```
Bob, help me set up comprehensive monitoring and alerting for AI Gateway usage, costs, and policy compliance.
```

---

## Exercise 6: Multi-Provider Resilience (Advanced)

**Objective:** Design a resilient system with provider failover

**Task:**
1. Design a multi-provider architecture:
   - Primary: Default model (groq/openai/gpt-oss-120b)
   - Fallback 1: AWS Bedrock (gpt-oss-120b)
   - Fallback 2: External OpenAI (gpt-4-turbo)

2. Define failover conditions:
   - Provider unavailability
   - High latency (>5 seconds)
   - Rate limit exceeded
   - Error rate threshold

3. Implement monitoring for:
   - Provider health
   - Failover events
   - Performance by provider

4. Create runbooks for:
   - Provider outages
   - Performance degradation
   - Cost overruns

**Success Criteria:**
- Failover logic is well-defined
- System handles provider failures gracefully
- Monitoring tracks provider health
- Runbooks are comprehensive
- You can explain the resilience strategy

**Ask Bob:**
```
Bob, help me design a resilient multi-provider architecture with automatic failover and comprehensive monitoring.
```

---

## Exercise 7: Compliance and Security (Advanced)

**Objective:** Implement compliance and security controls

**Scenario:**
Your organization operates in a regulated industry with requirements for:
- Data residency (EU only)
- PII protection
- Audit logging
- Access controls
- Encryption in transit and at rest

**Task:**
1. Design a compliance-focused architecture:
   - Model selection based on data residency
   - PII detection and filtering
   - Comprehensive audit logging
   - Role-based access control

2. Create security policies:
   ```yaml
   # security-policy.yaml
   policies:
     - name: compliance_policy
       description: Policy for regulated workloads
       rules:
         - type: data_residency
           allowed_regions:
             - eu-west-1
             - eu-central-1
         
         - type: content_filter
           block_pii: true
           block_sensitive_data: true
           log_violations: true
         
         - type: audit
           log_all_requests: true
           log_all_responses: true
           retention_days: 365
         
         - type: access_control
           require_authentication: true
           allowed_roles:
             - compliance_admin
             - approved_user
   ```

3. Implement audit logging

4. Create compliance reports

**Success Criteria:**
- Architecture meets compliance requirements
- Security policies are comprehensive
- Audit logging captures all necessary data
- You can generate compliance reports
- You understand regulatory implications

**Ask Bob:**
```
Bob, help me design a compliance-focused AI Gateway architecture with comprehensive security controls and audit logging for a regulated industry.
```

---

## Bonus Challenge: Production-Ready System

**Objective:** Build a complete, production-ready AI Gateway implementation

**Requirements:**
- Support 50,000 daily interactions
- 99.9% uptime SLA
- Budget: $500/month
- Compliance: GDPR, SOC 2
- Performance: <2 second average response time

**Task:**
1. Design complete architecture
2. Configure all providers and policies
3. Implement monitoring and alerting
4. Create disaster recovery plan
5. Document everything
6. Conduct load testing
7. Prepare for production deployment

**Success Criteria:**
- System meets all requirements
- Architecture is scalable
- Costs are within budget
- Compliance is verified
- Documentation is complete
- Team is trained
- Deployment plan is ready

**Ask Bob:**
```
Bob, help me design and implement a complete, production-ready AI Gateway system that meets enterprise requirements for scale, reliability, compliance, and cost.
```

---

## Tips for Success

1. **Start Simple:** Begin with basic configurations before tackling complex scenarios
2. **Measure Everything:** Track costs, performance, and usage from day one
3. **Use Bob:** Ask Bob to help analyze results and suggest improvements
4. **Document Decisions:** Keep detailed notes on configuration choices
5. **Test Thoroughly:** Validate all configurations before production use
6. **Monitor Continuously:** Set up alerts and review metrics regularly
7. **Iterate:** Refine your approach based on real-world usage

## Additional Resources

- [AI Gateway Documentation](https://developer.watson-orchestrate.ibm.com/llm/managing_llm)
- [Model Policies Guide](https://developer.watson-orchestrate.ibm.com/llm/policies)
- [External Provider Configuration](https://developer.watson-orchestrate.ibm.com/llm/providers)
- [Security Best Practices](https://developer.watson-orchestrate.ibm.com/security/best_practices)
- [Cost Optimization](https://developer.watson-orchestrate.ibm.com/llm/cost_optimization)

---

**Remember:** AI Gateway is a powerful tool for managing multiple model providers, but it requires careful planning, monitoring, and governance to use effectively in production!