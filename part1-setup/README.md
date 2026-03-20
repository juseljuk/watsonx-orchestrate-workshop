# Part 1: Setup & Environment

**Duration:** 15 minutes  
**Objective:** Get your development environment ready for building watsonx Orchestrate agents

## Prerequisites Check

Before starting, ensure you have:
- [ ] Python 3.9 or higher installed
- [ ] VS Code installed
- [ ] Bob extension installed and activated in VS Code
- [ ] watsonx Orchestrate access (cloud or Developer Edition)

## Step 1: Verify Python Installation

Open a terminal and run:
```bash
python --version
# or
python3 --version
```

You should see Python 3.9 or higher. If not, download from [python.org](https://www.python.org/downloads/).

## Step 2: Install watsonx Orchestrate SDK

Install the IBM watsonx Orchestrate SDK:

```bash
pip install ibm-watsonx-orchestrate
```

Verify the installation:
```bash
orchestrate --version
```

## Step 3: Configure Your Credentials

You have two options:

### Option A: Using Cloud watsonx Orchestrate

1. Get your API key from the watsonx Orchestrate console
2. Initialize your configuration:

```bash
orchestrate init
```

Follow the prompts to enter:
- **API Key**: Your watsonx Orchestrate API key
- **Region**: Your service region (e.g., us-south, eu-de)
- **Environment**: Choose `draft` for development

### Option B: Using Developer Edition (Local)

If you're running watsonx Orchestrate Developer Edition locally:

```bash
orchestrate init --local
```

This will configure the SDK to use `http://localhost:4321` as the endpoint.

## Step 4: Verify Bob is Working

Let's test that Bob can help you with watsonx Orchestrate tasks.

1. Open VS Code
2. Open the Bob chat panel (usually on the right side)
3. Try this prompt:

```
Bob, can you help me understand what watsonx Orchestrate agents are?
```

Bob should respond with information about agents. If not, check that:
- Bob extension is installed and enabled
- You're in the correct workspace folder
- Bob has access to the watsonx-orchestrate-adk-docs MCP server

## Step 5: Test Your Connection

Create a simple verification script to test your setup:

**Ask Bob to help you:**
```
Bob, create a Python script called verify-setup.py that tests my watsonx Orchestrate connection by listing available agents
```

Or use the provided script below:

```python
# verify-setup.py
from ibm_watsonx_orchestrate import AgentBuilder

def verify_setup():
    """Verify watsonx Orchestrate setup"""
    try:
        # Initialize the agent builder
        builder = AgentBuilder()
        
        print("✅ Successfully connected to watsonx Orchestrate!")
        print("\nListing available agents...")
        
        # List agents
        agents = builder.list_agents()
        
        if agents.native_agents or agents.external_agents or agents.assistant_agents:
            print(f"\n📋 Found agents:")
            for agent in agents.native_agents:
                print(f"  - {agent['name']} (native)")
            for agent in agents.external_agents:
                print(f"  - {agent['name']} (external)")
            for agent in agents.assistant_agents:
                print(f"  - {agent['name']} (assistant)")
        else:
            print("\n📋 No agents found yet (this is normal for a new environment)")
        
        print("\n✅ Setup verification complete!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nTroubleshooting tips:")
        print("1. Check your API key is correct")
        print("2. Verify your network connection")
        print("3. Ensure you ran 'orchestrate init'")
        print("4. Try running 'orchestrate init' again")
        return False

if __name__ == "__main__":
    verify_setup()
```

Run the script:
```bash
python verify-setup.py
```

## Step 6: Understand the Workshop Structure

Your workshop folder should look like this:

```
workshop/
├── README.md                    # Main workshop guide
├── part1-setup/                 # You are here!
│   ├── README.md
│   └── verify-setup.py
├── part2-first-agent/           # Next: Build your first agent
├── part3-custom-tools/          # Then: Create custom tools
├── part4-advanced/              # Advanced features
├── part5-deployment/            # Deploy your agent
├── solutions/                   # Reference solutions
└── bob-prompts/                 # Helpful Bob prompts
```

## Using Bob Throughout the Workshop

Bob is your AI pair programmer for this workshop. Here's how to use Bob effectively:

### Good Bob Prompts:
✅ "Bob, create a Python tool that checks order status given an order ID"  
✅ "Bob, why is my agent not responding to user messages?"  
✅ "Bob, explain what agent instructions do in watsonx Orchestrate"  
✅ "Bob, refactor this tool to handle errors better"  

### Less Effective Prompts:
❌ "Bob, fix this" (too vague)  
❌ "Bob, make it work" (no context)  
❌ "Bob, do everything for me" (you won't learn!)  

### Bob's Special Powers:
- 🔍 **Search docs**: Bob can search watsonx Orchestrate documentation
- 💻 **Write code**: Bob can create Python tools and agent specs
- 🐛 **Debug**: Bob can analyze errors and suggest fixes
- 📚 **Explain**: Bob can explain concepts and best practices
- 🔧 **Refactor**: Bob can improve your code

## Troubleshooting

### Issue: "orchestrate: command not found"
**Solution:** Make sure you installed the SDK and it's in your PATH:
```bash
pip install --user ibm-watsonx-orchestrate
# Add ~/.local/bin to your PATH if needed
```

### Issue: "Authentication failed"
**Solution:** Re-run the init command with correct credentials:
```bash
orchestrate init
```

### Issue: Bob isn't responding
**Solution:** 
1. Check Bob extension is enabled in VS Code
2. Restart VS Code
3. Check the Bob output panel for errors

### Issue: Connection refused (Developer Edition)
**Solution:** Make sure Developer Edition is running:
```bash
# Check if containers are running
docker ps
# Start Developer Edition if needed
orchestrate server start
```

## Quick Reference

### Useful Commands
```bash
# Initialize configuration
orchestrate init

# List agents
orchestrate agents list

# List tools
orchestrate tools list

# Get help
orchestrate --help

# Check version
orchestrate --version
```

### Environment Variables
```bash
# Override default endpoint
export ORCHESTRATE_URL="https://your-instance.com"

# Set API key
export ORCHESTRATE_API_KEY="your-api-key"
```

## Next Steps

Once your setup is verified:
1. ✅ You can connect to watsonx Orchestrate
2. ✅ Bob is responding to your questions
3. ✅ You understand the workshop structure

**You're ready to build your first agent!**

Continue to [Part 2: Building Your First Agent](../part2-first-agent/README.md) →

## Additional Resources

- [Installation Guide](https://developer.watson-orchestrate.ibm.com/getting_started/installation)
- [Configuration Reference](https://developer.watson-orchestrate.ibm.com/getting_started/configuration)
- [Developer Edition Setup](https://developer.watson-orchestrate.ibm.com/developer_edition/getting_started)

---

**💡 Pro Tip:** Keep Bob's chat panel open throughout the workshop. Whenever you're stuck, just ask Bob for help!