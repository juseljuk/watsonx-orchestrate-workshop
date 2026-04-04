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

## Step 5: Install watsonx Orchestrate ADK VS Code Extension

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

## Step 7: Import WXO Agent Architect Mode

Import a pre-configured custom mode specialized for building watsonx Orchestrate agents:

1. Download the mode configuration file from GitHub:
   - Visit: https://github.com/juseljuk/bobchestrate-workshop/blob/main/part1-setup/files/wxo-agent-architect-export.yaml
   - Click the **Download raw file** button

      <img src="images/image-10.png" alt="Download the raw file" width="40%">

   - Save the file to your Downloads folder or a location you can easily access

2. Open the Command Palette in IBM Bob IDE (press `Cmd+Shift+P` on Mac / `Ctrl+Shift+P` on Windows/Linux)

3. Type "Modes" and select it

4. Click on **Import** icon in the modes panel

   <img src="images/image-11.png" alt="Import custom mode" width="40%">
   
5. Select the `wxo-agent-architect-export.yaml` file you downloaded and click **Open**

6. You should see a confirmation message that the mode was imported successfully and see the mode appear in the modes panel

The imported "WXO Agent Architect" mode includes:
- **Role Definition**: Specialized for building watsonx Orchestrate agents
- **Custom Instructions**: Guidance on using MCP servers for agent development
- **MCP Server Integration**: Automatically uses both `watsonx-orchestrate-adk` and `watsonx-orchestrate-adk-docs` servers
- **Tool Groups**: Access to read, edit, browser, command, and MCP tools

**Verify the mode:**

1. Open Bob's chat panel if not already open
2. Click on the mode selector (usually shows the current mode like "Code" or "Ask")
3. You should see "WXO Agent Architect" in the list of available modes
4. Select "WXO Agent Architect" mode
5. Ask Bob: "What can you help me with in this mode?"
6. Bob should respond with information about building watsonx Orchestrate agents and mention the available MCP servers

## Step 8: Create Python Virtual Environment

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

> **_Note:_** The virtual environment will be automatically activated when you open new terminals in IBM Bob IDE.

> **_Note2:_** If you're wondering about the .bob folder, it was created automatically when you installed the MCP Servers for Orchestrate. This folder contains all the IBM Bob IDE configuration files for the MCP Servers for Orchestrate. It's safe to leave it there.

## Step 9: Install watsonx Orchestrate SDK

Since you have the watsonx Orchestrate ADK extension installed, you will see the ADK informaton in the bottom Status Bar. Since we just created a fresh Python virtual environment to our workspace, you should see just a red cross stating that you need to install the ADK.

<img src="images/image-7.png" alt="IBM Bob IDE Status Bar showing ADK not installed" width="40%">

Click on the red cross to install the ADK. This will open a couple of commands to the search/command bar. Select the one to install the ADK.

<img src="images/image-8.png" alt="IBM Bob IDE Command Palette showing Install ADK command" width="70%">

Wait for the installation to complete. After a while, you should see a notification and a green checkmark in the Status Bar with the latest version number of the ADK.

<img src="images/image-9.png" alt="IBM Bob IDE Status Bar showing ADK installed" width="40%">

## Step 10: Get Your watsonx Orchestrate API key and API URL

For the workshop, we will use the watsonx Orchestrate ADK to interact with a watsonx Orchestrate SaaS instance. The ADK requires your API key and API URL to authenticate and connect to your watsonx Orchestrate instance.

> **_Note:_** `Your instructor will provide you with the API key and API URL for your watsonx Orchestrate instance.` If you are using your own instance, you can follow the instructions below to get the needed API key and the API URL.

### OPTIONAL: Using your own watsonx Orchestrate SaaS instance

<u>To generate an API key for the ADK:</u>

1. In your watsonx Orchestrate console, click on your **profile icon** in the top-right corner
2. Select **Settings** from the dropdown menu
3. Navigate to the **API details** tab
4. Click **Generate API key** button

   <img src="images/image-12.png" alt="Generate API key button highlighted" width="40%">

5. When the key is generated, click **Copy** to save it to your clipboard
6. **Important**: Copy the API key immediately and _store_ it securely
   - The key will only be shown once
   - If you lose it, you'll need to create a new one

> **Security Best Practice**: Treat your API key like a password. Never commit it to version control or share it publicly.

<u>To get the API URL:</u>

Copy the Service instance URL from the API details information. This is the base URL for your watsonx Orchestrate instance.

   <img src="images/image-13.png" alt="Get the service URL" width="60%">

### Configure the ADK Environment

#### Option A: Using the ADK CLI

1. Open a terminal window within Bob IDE
   - Form the Bob main menu bar, select **Terminal** > **New Terminal**

      <img src="images/image-14.png" alt="Open terminal" width="70%">
   
   - This will open a terminal window in the Bob IDE - notice that your Python environment is already activated

      <img src="images/image-15.png" alt="Terminal window opened in Bob IDE" width="80%">

2. Run the following command in your terminal to add your environment:

   ```bash
   orchestrate env add -n <your-env-name> -u <your-api-url>
   ```
   Where `<your-env-name>` is a name you choose for your environment (e.g., "my-wxo-cloud") and `<your-api-url>` is the URL you got in Step 10.

#### Option B: Using Bob to help you 😃

Now add your environment configuration using the ADK CLI:

```bash
orchestrate environment add
```

When prompted, enter the following information:

- **Environment Name**: A descriptive name for this environment (e.g., "my-wxo-cloud" or "production")
- **URL**: The API URL you copied in Step 1 (e.g., `https://us.watsonx-orchestrate.ibm.com`)
- **API Key**: The API key you generated in Step 2

Example interaction:
```
? Enter environment name: my-wxo-cloud
? Enter URL: https://us.watsonx-orchestrate.ibm.com
? Enter API key: [paste your API key here]
✓ Environment 'my-wxo-cloud' added successfully
```

#### Step 4: Activate the Environment

Activate your newly configured environment:

```bash
orchestrate environment activate my-wxo-cloud
```

You should see a confirmation message:
```
✓ Environment 'my-wxo-cloud' activated
```

#### Step 5: Verify the Configuration

Verify your connection is working:

```bash
orchestrate agents list
```

If configured correctly, this command will list any agents in your environment (or show an empty list if you haven't created any agents yet).

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

## Step 12: Test Your Connection

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

## Step 13: Understand the Workshop Structure

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