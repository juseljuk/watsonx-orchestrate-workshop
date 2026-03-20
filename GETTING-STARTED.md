# Getting Started with the watsonx Orchestrate Workshop

Welcome to the hands-on workshop for building AI agents with watsonx Orchestrate and Bob!

## Quick Start

1. **Open the workshop folder in VS Code**
   ```bash
   cd workshop
   code .
   ```

2. **Make sure Bob is active**
   - Check that the Bob extension is installed and enabled
   - Open the Bob chat panel (usually on the right side)

3. **Start with Part 1**
   - Open [`part1-setup/README.md`](./part1-setup/README.md)
   - Follow the setup instructions
   - Run the verification script

4. **Progress through the workshop**
   - Complete each part in order
   - Use Bob to help you along the way
   - Try the exercises to reinforce learning

## Workshop Structure

```
workshop/
├── README.md                          # Workshop overview
├── GETTING-STARTED.md                 # This file
│
├── part1-setup/                       # 15 min - Setup & Environment
│   ├── README.md                      # Setup instructions
│   └── verify-setup.py                # Verification script
│
├── part2-first-agent/                 # 20 min - Building Your First Agent
│   ├── README.md                      # Agent creation guide
│   ├── hello-agent.yaml               # Sample agent
│   └── exercises.md                   # Practice exercises
│
├── part3-custom-tools/                # 30 min - Adding Custom Tools
│   ├── README.md                      # Tool creation guide
│   ├── order_status_tool.py           # Sample tool 1
│   ├── refund_tool.py                 # Sample tool 2
│   └── exercises.md                   # Practice exercises
│
├── part4-advanced/                    # 25 min - Knowledge Bases & Collaborators
│   ├── README.md                      # Advanced features guide
│   ├── customer-support-agent.yaml    # Complete agent example
│   ├── escalation-agent.yaml          # Collaborator agent
│   └── faq-knowledge-base.yaml        # Knowledge base example
│
├── part5-deployment/                  # 20 min - Testing & Deployment
│   └── README.md                      # Deployment guide
│
└── bob-prompts/                       # Bob Helper Guide
    └── helpful-prompts.md             # Useful Bob prompts
```

## What You'll Build

By the end of this workshop, you'll have created a complete **Customer Support Agent** that can:

✅ Answer FAQs using a knowledge base  
✅ Check order status using a custom tool  
✅ Process refund requests with validation  
✅ Escalate complex issues to a specialist agent  
✅ Handle multi-turn conversations  
✅ Provide helpful, accurate responses  

## Time Commitment

- **Minimum**: 90 minutes (following the main path)
- **Recommended**: 120 minutes (including exercises)
- **Extended**: 180+ minutes (completing all exercises and experiments)

## Prerequisites

Before starting, ensure you have:

- [ ] Python 3.9 or higher installed
- [ ] VS Code installed
- [ ] Bob extension installed and activated
- [ ] watsonx Orchestrate access (cloud or Developer Edition)
- [ ] Basic Python knowledge
- [ ] Enthusiasm to learn! 🚀

## Learning Path

### Beginner Path (90 min)
Follow the main README in each part, skip exercises:
1. Part 1: Setup (15 min)
2. Part 2: First Agent (20 min)
3. Part 3: Custom Tools (30 min)
4. Part 4: Advanced Features (25 min)
5. Part 5: Deployment (20 min)

### Intermediate Path (120 min)
Complete main content plus selected exercises:
1. All main content (90 min)
2. Part 2: Exercises 1-2 (10 min)
3. Part 3: Exercises 1-3 (20 min)

### Advanced Path (180+ min)
Complete everything including all exercises and experiments:
1. All main content (90 min)
2. All exercises (60+ min)
3. Bonus challenges (30+ min)

## Using Bob Effectively

Bob is your AI pair programmer throughout this workshop. Here's how to get the most out of Bob:

### When to Ask Bob

✅ **Creating code**: "Bob, create a Python tool that..."  
✅ **Debugging**: "Bob, why isn't my agent calling this tool?"  
✅ **Understanding**: "Bob, explain how agent instructions work"  
✅ **Improving**: "Bob, review this code and suggest improvements"  
✅ **Testing**: "Bob, generate test cases for my agent"  

### Bob Best Practices

1. **Be specific**: Include relevant code and context
2. **State your goal**: Explain what you're trying to achieve
3. **Provide examples**: Show what you've tried
4. **Ask follow-ups**: Build on Bob's responses
5. **Request explanations**: Ask Bob to explain the reasoning

See [`bob-prompts/helpful-prompts.md`](./bob-prompts/helpful-prompts.md) for more examples!

## Common Issues

### Setup Issues

**Issue**: "orchestrate: command not found"  
**Solution**: Install the SDK: `pip install ibm-watsonx-orchestrate`

**Issue**: "Authentication failed"  
**Solution**: Run `orchestrate init` with correct credentials

**Issue**: Bob isn't responding  
**Solution**: Check Bob extension is enabled, restart VS Code if needed

### Workshop Issues

**Issue**: Can't find a file mentioned in the guide  
**Solution**: Make sure you're in the `workshop/` directory

**Issue**: Code examples don't work  
**Solution**: Check you've completed previous steps, ask Bob for help

**Issue**: Stuck on an exercise  
**Solution**: Check the solutions folder (but try yourself first!)

## Getting Help

1. **Ask Bob**: Your first resource for questions
2. **Check the docs**: Links provided throughout the workshop
3. **Review examples**: Sample code is provided in each part
4. **Solutions folder**: Reference implementations (coming soon)

## Tips for Success

💡 **Take breaks**: This is a lot of information - pace yourself  
💡 **Experiment**: Try modifying examples to see what happens  
💡 **Ask questions**: Use Bob liberally - that's what it's for!  
💡 **Document**: Take notes on what you learn  
💡 **Share**: Discuss with others doing the workshop  

## After the Workshop

Once you complete the workshop:

1. **Build your own agent**: Apply what you learned to your use case
2. **Explore advanced features**: MCP servers, custom models, etc.
3. **Join the community**: Share your creations and learn from others
4. **Keep using Bob**: Bob can help with ongoing development

## Resources

- [watsonx Orchestrate Documentation](https://developer.watson-orchestrate.ibm.com/)
- [Python Tools Guide](https://developer.watson-orchestrate.ibm.com/tools/create_tool)
- [Agent Builder API](https://developer.watson-orchestrate.ibm.com/apis/agents/)
- [Community Forum](https://community.ibm.com/community/user/watsonai/communities/community-home?CommunityKey=7a3dc5ba-3018-452d-9a43-a49dc6819633)

## Feedback

We'd love to hear about your experience! After completing the workshop:

- What worked well?
- What was confusing?
- What would you like to see added?
- How did Bob help you?

## Ready to Start?

Great! Head over to [Part 1: Setup & Environment](./part1-setup/README.md) to begin! 🚀

---

**Remember**: The goal isn't just to complete the workshop, but to understand how to build AI agents. Take your time, experiment, and most importantly - have fun! 🎉