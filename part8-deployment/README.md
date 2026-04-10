# Part 8: Testing & Deployment

**Duration:** 20 minutes  
**Objective:** Test your agent thoroughly and deploy it to production

## What You'll Learn

- Comprehensive testing strategies
- Deployment best practices
- Monitoring and observability
- Generating webchat embed code
- Production readiness checklist

## Testing Your Agent

### Step 1: Unit Testing Tools

Test your tools individually before testing the full agent:

```python
# test_tools.py
from order_status_tool import check_order_status
from refund_tool import process_refund

def test_order_status_valid():
    """Test order status with valid order ID"""
    result = check_order_status("ORD-12345")
    assert result["success"] == True
    assert result["order_id"] == "ORD-12345"
    assert "status" in result
    print("✅ Valid order status test passed")

def test_order_status_invalid():
    """Test order status with invalid order ID"""
    result = check_order_status("INVALID")
    assert result["success"] == False
    assert "error" in result
    print("✅ Invalid order status test passed")

def test_refund_valid():
    """Test refund with valid parameters"""
    result = process_refund(
        order_id="ORD-12345",
        reason="Product was damaged during shipping",
        amount=99.99
    )
    assert result["success"] == True
    assert "refund_id" in result
    print("✅ Valid refund test passed")

def test_refund_too_large():
    """Test refund with amount over limit"""
    result = process_refund(
        order_id="ORD-12345",
        reason="Large order issue",
        amount=15000.00
    )
    assert result["success"] == False
    assert result.get("requires_approval") == True
    print("✅ Large refund test passed")

if __name__ == "__main__":
    test_order_status_valid()
    test_order_status_invalid()
    test_refund_valid()
    test_refund_too_large()
    print("\n✅ All tool tests passed!")
```

Run the tests:
```bash
python test_tools.py
```

### Ask Bob to Help:
```
Bob, create comprehensive unit tests for my order status and refund tools
```

### Step 2: Integration Testing

Test the agent with various scenarios:

```python
# test_agent.py
from ibm_watsonx_orchestrate import AgentBuilder

def test_agent_scenarios():
    """Test agent with various scenarios"""
    builder = AgentBuilder()
    agent_name = "customer-support-agent"
    
    scenarios = [
        {
            "name": "FAQ Question",
            "message": "What's your return policy?",
            "expected_keywords": ["return", "30 days", "refund"]
        },
        {
            "name": "Order Status Check",
            "message": "Check status of order ORD-12345",
            "expected_keywords": ["status", "ORD-12345"]
        },
        {
            "name": "Refund Request",
            "message": "I need a refund for order ORD-12345. The item was damaged. Amount is $99.99",
            "expected_keywords": ["refund", "approved", "REF-"]
        },
        {
            "name": "Escalation Trigger",
            "message": "I need a refund for $15,000 for order ORD-67890",
            "expected_keywords": ["escalat", "specialist", "manager"]
        }
    ]
    
    for scenario in scenarios:
        print(f"\n🧪 Testing: {scenario['name']}")
        print(f"   Message: {scenario['message']}")
        
        response = builder.chat_with_agent(
            agent_name=agent_name,
            message=scenario['message']
        )
        
        response_text = response['message'].lower()
        
        # Check if expected keywords are present
        found_keywords = [kw for kw in scenario['expected_keywords'] 
                         if kw.lower() in response_text]
        
        if len(found_keywords) >= len(scenario['expected_keywords']) // 2:
            print(f"   ✅ Test passed")
        else:
            print(f"   ⚠️  Test needs review")
            print(f"   Expected keywords: {scenario['expected_keywords']}")
            print(f"   Found: {found_keywords}")
        
        print(f"   Response: {response['message'][:100]}...")

if __name__ == "__main__":
    test_agent_scenarios()
```

### Step 3: Test Scenarios Document

Create comprehensive test scenarios:

```markdown
# Test Scenarios for Customer Support Agent

## Scenario 1: Simple FAQ
**User:** "What payment methods do you accept?"
**Expected:** Agent retrieves info from knowledge base about payment methods
**Pass Criteria:** Response includes credit cards, PayPal, Apple Pay, Google Pay

## Scenario 2: Order Status Check
**User:** "Can you check the status of order ORD-12345?"
**Expected:** Agent calls check_order_status tool
**Pass Criteria:** Response includes order status, items, delivery date

## Scenario 3: Simple Refund
**User:** "I need a refund for order ORD-12345. The item was damaged. Amount is $99.99"
**Expected:** Agent calls process_refund tool
**Pass Criteria:** Response includes refund ID and confirmation

## Scenario 4: Large Refund (Escalation)
**User:** "I need a refund for $15,000"
**Expected:** Agent recognizes need for escalation
**Pass Criteria:** Agent mentions escalation or specialist

## Scenario 5: Multi-turn Conversation
**Turn 1:** "Hello"
**Expected:** Friendly greeting
**Turn 2:** "What's your shipping policy?"
**Expected:** Info from knowledge base
**Turn 3:** "How long for express shipping?"
**Expected:** Specific info about express shipping (2-3 days)
**Pass Criteria:** Agent maintains context across turns

## Scenario 6: Out of Scope
**User:** "What's the weather today?"
**Expected:** Agent politely declines and redirects
**Pass Criteria:** Agent explains it can't help with weather

## Scenario 7: Error Handling
**User:** "Check order ABC123"
**Expected:** Agent handles invalid order ID
**Pass Criteria:** Agent explains order ID format and asks for correct ID

## Scenario 8: Tool Chaining
**User:** "Check order ORD-12345 and if it's delivered, I want a refund"
**Expected:** Agent checks status first, then processes refund if applicable
**Pass Criteria:** Agent uses both tools appropriately
```

### Ask Bob to Help:
```
Bob, create comprehensive test scenarios for my customer support agent including edge cases
```

## Deployment

### Step 1: Pre-Deployment Checklist

Before deploying to production, verify:

```markdown
## Pre-Deployment Checklist

### Agent Configuration
- [ ] Agent instructions are clear and comprehensive
- [ ] All required tools are imported and working
- [ ] Knowledge bases are indexed and accessible
- [ ] Collaborator agents are configured correctly
- [ ] LLM model is appropriate for production
- [ ] Agent configuration (hidden, enable_cot) is correct

### Tools
- [ ] All tools have proper input validation
- [ ] Error handling is comprehensive
- [ ] Tools return consistent response formats
- [ ] External API calls have timeout handling
- [ ] Rate limiting is implemented where needed
- [ ] Credentials are properly configured

### Knowledge Bases
- [ ] All documents are up to date
- [ ] Knowledge base is fully indexed
- [ ] Retrieval quality is tested
- [ ] Chunk size and overlap are optimized

### Testing
- [ ] Unit tests pass for all tools
- [ ] Integration tests pass for agent
- [ ] All test scenarios pass
- [ ] Edge cases are handled
- [ ] Error scenarios are tested

### Security
- [ ] No sensitive data in agent instructions
- [ ] API keys are stored securely
- [ ] Input validation prevents injection attacks
- [ ] Rate limiting is configured

### Performance
- [ ] Response times are acceptable
- [ ] Agent doesn't hit rate limits
- [ ] Knowledge base queries are fast
- [ ] Tool execution is efficient

### Documentation
- [ ] Agent purpose is documented
- [ ] Tool usage is documented
- [ ] Deployment process is documented
- [ ] Troubleshooting guide exists
```

### Step 2: Deploy to Draft Environment

First, deploy to the draft environment for testing:

```bash
# Ensure you're in draft environment
orchestrate environment set draft

# Import all components
orchestrate tools import -k python order_status_tool.py
orchestrate tools import -k python refund_tool.py
orchestrate knowledge-bases import faq-knowledge-base.yaml
orchestrate agents import escalation-agent.yaml
orchestrate agents import customer-support-agent.yaml

# Verify deployment
orchestrate agents list
orchestrate tools list
orchestrate knowledge-bases list
```

### Step 3: Deploy to Live Environment

Once testing is complete, deploy to production:

```bash
# Switch to live environment
orchestrate environment set live

# Import all components
orchestrate tools import -k python order_status_tool.py
orchestrate tools import -k python refund_tool.py
orchestrate knowledge-bases import faq-knowledge-base.yaml
orchestrate agents import escalation-agent.yaml
orchestrate agents import customer-support-agent.yaml

# Verify live deployment
orchestrate agents list --environment live
```

### Step 4: Generate Webchat Embed Code

Generate the webchat embed code for your website:

```bash
orchestrate channels webchat generate-embed --agent customer-support-agent --environment live
```

This will output HTML/JavaScript code like:

```html
<script>
  window.watsonxOrchestrate = {
    integrationID: "your-integration-id",
    region: "us-south",
    serviceInstanceID: "your-instance-id",
    onLoad: function(instance) {
      instance.render();
    }
  };
</script>
<script src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/latest/WatsonxOrchestrate.js"></script>
```

Add this to your website's HTML.

### Ask Bob to Help:
```
Bob, help me generate and customize the webchat embed code for my agent
```

## Monitoring and Observability

### Step 1: Enable Tracing

Monitor your agent's performance:

```bash
# View recent traces
orchestrate traces list --agent customer-support-agent --limit 10

# View specific trace details
orchestrate traces get <trace-id>

# Export traces for analysis
orchestrate traces export --agent customer-support-agent --output traces.json
```

### Step 2: Analyze Performance

Create a monitoring script:

```python
# monitor_agent.py
from ibm_watsonx_orchestrate import AgentBuilder
from datetime import datetime, timedelta

def analyze_agent_performance(agent_name, days=7):
    """Analyze agent performance over the last N days"""
    builder = AgentBuilder()
    
    # Get traces (this is a simplified example)
    print(f"📊 Performance Analysis for {agent_name}")
    print(f"   Period: Last {days} days")
    print(f"   Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n" + "="*60)
    
    # In a real implementation, you would:
    # 1. Fetch traces from the observability API
    # 2. Calculate metrics (response time, success rate, etc.)
    # 3. Identify common issues
    # 4. Generate recommendations
    
    print("\n📈 Key Metrics:")
    print("   • Total conversations: [from traces]")
    print("   • Average response time: [from traces]")
    print("   • Tool usage: [from traces]")
    print("   • Error rate: [from traces]")
    
    print("\n🎯 Recommendations:")
    print("   • Review slow responses")
    print("   • Optimize frequently used tools")
    print("   • Update knowledge base based on common questions")

if __name__ == "__main__":
    analyze_agent_performance("customer-support-agent")
```

### Ask Bob to Help:
```
Bob, create a monitoring script that analyzes my agent's performance and identifies issues
```

## Production Best Practices

### 1. Version Control
- Keep all agent YAML files in version control
- Tag releases
- Document changes in each version

### 2. Environment Strategy
- Use draft for development and testing
- Use live for production
- Never test directly in live

### 3. Rollback Plan
- Keep previous versions of agents
- Document rollback procedure
- Test rollback process

### 4. Monitoring
- Set up alerts for errors
- Monitor response times
- Track tool usage
- Review traces regularly

### 5. Maintenance
- Update knowledge bases regularly
- Review and improve agent instructions
- Optimize slow tools
- Add new capabilities based on user needs

## Troubleshooting Production Issues

### Issue: Agent is slow
**Diagnosis:**
```bash
orchestrate traces list --agent customer-support-agent --limit 20
# Look for slow tool calls or knowledge base queries
```

**Solutions:**
- Optimize tool code
- Reduce knowledge base chunk size
- Use faster LLM model
- Add caching

### Issue: Agent gives wrong answers
**Diagnosis:**
- Review recent conversations
- Check knowledge base content
- Verify tool outputs

**Solutions:**
- Update agent instructions
- Improve knowledge base documents
- Fix tool logic
- Add more test scenarios

### Issue: Tools failing
**Diagnosis:**
```bash
orchestrate traces get <trace-id>
# Check tool error messages
```

**Solutions:**
- Check API credentials
- Verify network connectivity
- Review tool error handling
- Check rate limits

## Continuous Improvement

### 1. Collect Feedback
- Monitor user satisfaction
- Track common questions
- Identify gaps in knowledge base

### 2. Iterate
- Update agent instructions based on feedback
- Add new tools for common requests
- Expand knowledge base
- Improve error handling

### 3. Measure Success
- Response accuracy
- User satisfaction
- Resolution time
- Escalation rate

### Ask Bob to Help:
```
Bob, analyze these conversation logs and suggest improvements to my agent: [paste logs]
```

## Key Takeaways

✅ Comprehensive testing prevents production issues  
✅ Use draft environment for testing, live for production  
✅ Monitor agent performance continuously  
✅ Have a rollback plan ready  
✅ Iterate based on user feedback  

## Congratulations! 🎉

You've completed the workshop and built a production-ready customer support agent!

### What You've Learned:
- ✅ Setting up watsonx Orchestrate
- ✅ Creating and configuring agents
- ✅ Building custom Python tools
- ✅ Integrating knowledge bases
- ✅ Creating agent collaborators
- ✅ Testing and deployment
- ✅ Using Bob as your AI assistant

### Next Steps:
1. Build your own agent for your use case
2. Explore advanced features (MCP servers, custom models)
3. Join the watsonx Orchestrate community
4. Share your creations!

## Additional Resources

- [Production Deployment Guide](https://developer.watson-orchestrate.ibm.com/deployment/production)
- [Monitoring and Observability](https://developer.watson-orchestrate.ibm.com/observability/overview)
- [Best Practices](https://developer.watson-orchestrate.ibm.com/best_practices)
- [Community Forum](https://community.ibm.com/community/user/watsonai/communities/community-home?CommunityKey=7a3dc5ba-3018-452d-9a43-a49dc6819633)

---

**💡 Pro Tip:** Keep using Bob for your ongoing development. Bob can help you maintain, improve, and extend your agents!

**🚀 Ready to build something amazing? Go for it!**