# Part 1: Setup & Environment

**Duration:** 15 minutes  
**Objective:** Get your development environment ready for building watsonx Orchestrate agents

## Prerequisites Check

Before starting, ensure you have:
- [ ] Python 3.11-3.13 installed
- [ ] IBM Bob IDE installed
- [ ] watsonx Orchestrate access (SaaS or Developer Edition)

## Step 1: Verify Python Installation

Open a terminal and run:
```bash
python --version
# or
python3 --version
```

## Step 2: Verify uv Installation

Open a terminal and run:
```bash
uv --version
```

## Step 3: Create Workshop Folder

Create a dedicated folder for your workshop project - you can place it where ever you want:

```bash
mkdir bobchestrate-ws
cd bobchestrate-ws
```

This folder will contain all your workshop files, agents, and tools.

## Step 4: Open Folder in IBM Bob IDE

Open the workshop folder in IBM Bob IDE:
1. Launch IBM Bob IDE
2. Click **File** → **Open Folder**

   <img src="images/image.png" alt="IBM Bob IDE File menu showing Open Folder option" width="30%">


3. Navigate to and select the `bobchestrate-ws` folder
4. Click **Open**
5. Click **Yes, I trust the author** to trust the workspace

   <img src="images/image-1.png" alt="IBM Bob IDE File menu showing Open Folder option" width="40%">

The empty workspace will open.

## Step 5: Install watsonx Orchestrate VSCode Extension

Install the watsonx Orchestrate extension for IBM Bob IDE:

1. Open the Extensions view in IBM Bob IDE (Click the Extensions icon in the Activity Bar or press `Cmd+Shift+X` on Mac / `Ctrl+Shift+X` on Windows/Linux)

   <img src="images/image-2.png" alt="IBM Bob IDE File menu showing Open Folder option" width="10%">

2. Search for "watsonx Orchestrate"

    <img src="images/image-4.png" alt="IBM Bob IDE File menu showing Open Folder option" width="40%">

3. Click **Install** on the "IBM watsonx Orchestrate ADK" extension
4. Wait for the installation to complete
5. Reload VS Code if prompted
6. You should now see the extension icon appear in the Activity Bar:

   <img src="images/image-3.png" alt="IBM Bob IDE File menu showing Open Folder option" width="10%">

The extension provides:
- Syntax highlighting for agent YAML files
- IntelliSense for agent configuration
- Quick access to watsonx Orchestrate commands
- Integration with the Orchestrate CLI

## Step 6: Install watsonx Orchestrate MCP Servers

Install the watsonx Orchestrate MCP servers through the ADK extension:

1. Open the Command Palette in IBM Bob IDE (press `Cmd+Shift+P` on Mac / `Ctrl+Shift+P` on Windows/Linux)
2. Type "watsonx Orchestrate: Install MCP Servers" and select it
3. Wait for the installation to complete
4. You should see a confirmation message that the MCP servers have been installed successfully

**Verify the installation:**

To confirm the MCP servers are installed and working:

1. Open Bob's chat panel in IBM Bob IDE
2. Ask Bob: "What MCP servers are available?"
3. You should see the following watsonx Orchestrate MCP servers listed:
   - `watsonx-orchestrate-adk` - Provides tools for interacting with watsonx Orchestrate (list agents, tools, etc.)
   - `watsonx-orchestrate-adk-docs` - Provides access to watsonx Orchestrate documentation

Alternatively, you can check the MCP servers configuration:
1. Open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
2. Type "MCP Servers" and select it
3. Verify that the watsonx Orchestrate MCP servers are listed in the configuration and both of them marked with a green bullet point

   <img src="images/image-5.png" alt="IBM Bob IDE File menu showing Open Folder option" width="75%">

The MCP servers provide:
- Access to watsonx Orchestrate documentation
- Integration with the watsonx Orchestrate ADK
- Tools for listing agents, tools, and other resources
- Enhanced Bob capabilities for watsonx Orchestrate development

## Step 7: Create Python Virtual Environment

Create a virtual environment for the workshop to keep dependencies isolated using IBM Bob IDE's built-in commands:

1. Open the Command Palette in IBM Bob IDE (press `Cmd+Shift+P` on Mac / `Ctrl+Shift+P` on Windows/Linux)
2. Type "Python: Create Environment" and select it
3. Choose "Venv" as the environment type
4. Select your Python interpreter (Python 3.11-3.13)
5. Wait for the virtual environment to be created

You can now see the .venv folder in your workspace explorer view.

<img src="images/image-6.png" alt="IBM Bob IDE File menu showing Open Folder option" width="50%">

IBM Bob IDE will automatically:
- Create a `.venv` folder in your workspace
- Activate the virtual environment in new terminals
- Show `(.venv)` in your terminal prompt

**Note:** The virtual environment will be automatically activated when you open new terminals in IBM Bob IDE.

**Note2:** If you're wondering about the .bob folder, it was created automatically when you installed the MCP Servers for Orchestrate. This folder contains all the IBM Bob IDE configuration files for the MCP Servers for Orchestrate. It's safe to leave it there.

## Step 8: Install watsonx Orchestrate SDK

Since you have the watsonx Orchestrate ADK extension installed, you will see the ADK informaton in the bottom Status Bar. If you already have the ADK installed, you can see the current version, but otherwise you should see just a red cross stating that you need to install the ADK.

<img src="images/image-7.png" alt="IBM Bob IDE Status Bar showing ADK not installed" width="30%">

## Step 9: Configure Your Credentials

You have two options:

### Option A: Using Cloud watsonx Orchestrate

1. Get your API key from the watsonx Orchestrate console
2. Add your environment configuration:

```bash
orchestrate environment add
```

Follow the prompts to enter:
- **Environment Name**: A name for this environment (e.g., "my-wxo")
- **URL**: Your watsonx Orchestrate URL
- **API Key**: Your watsonx Orchestrate API key

3. Activate the environment:

```bash
orchestrate environment activate <environment-name>
```

### Option B: Using Developer Edition (Local)

If you're running watsonx Orchestrate Developer Edition locally:

```bash
# Add local environment
orchestrate environment add

# When prompted:
# - Name: local-dev
# - URL: http://localhost:4321
# - API Key: (leave empty or use your local key)

# Activate it
orchestrate environment activate local-dev
```

### Option C: Using Environment Variables

You can also configure using environment variables:

```bash
export WO_URL="https://your-orchestrate-url.com"
export WO_API_KEY="your-api-key"
```

## Step 10: Verify Bob is Working

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

## Step 11: Test Your Connection

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
        print("3. Ensure you configured your environment:")
        print("   orchestrate environment add")
        print("   orchestrate environment activate <name>")
        print("4. Or set environment variables:")
        print("   export WO_URL='your-url'")
        print("   export WO_API_KEY='your-key'")
        return False

if __name__ == "__main__":
    verify_setup()
```

Run the script:
```bash
python verify-setup.py
```

## Step 12: Understand the Workshop Structure

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
**Solution:** Check your environment configuration:
```bash
# List environments
orchestrate environment list

# Add/update environment
orchestrate environment add

# Activate environment
orchestrate environment activate <name>
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
# Add environment
orchestrate environment add

# List environments
orchestrate environment list

# Activate environment
orchestrate environment activate <name>

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