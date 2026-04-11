#!/usr/bin/env python3
"""
Verify watsonx Orchestrate Setup
This script tests your connection to watsonx Orchestrate and lists available resources.
"""

from ibm_watsonx_orchestrate import AgentBuilder

def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def verify_setup():
    """Verify watsonx Orchestrate setup"""
    print_section("watsonx Orchestrate Setup Verification")
    
    try:
        # Initialize the agent builder
        print("\n🔌 Connecting to watsonx Orchestrate...")
        builder = AgentBuilder()
        
        print("✅ Successfully connected to watsonx Orchestrate!")
        
        # List agents
        print_section("Available Agents")
        agents = builder.list_agents()
        
        total_agents = (
            len(agents.native_agents) + 
            len(agents.external_agents) + 
            len(agents.assistant_agents)
        )
        
        if total_agents > 0:
            print(f"\n📋 Found {total_agents} agent(s):\n")
            
            if agents.native_agents:
                print("  Native Agents:")
                for agent in agents.native_agents:
                    print(f"    • {agent['name']}")
                    if agent.get('description'):
                        print(f"      └─ {agent['description']}")
            
            if agents.external_agents:
                print("\n  External Agents:")
                for agent in agents.external_agents:
                    print(f"    • {agent['name']}")
                    if agent.get('description'):
                        print(f"      └─ {agent['description']}")
            
            if agents.assistant_agents:
                print("\n  Assistant Agents:")
                for agent in agents.assistant_agents:
                    print(f"    • {agent['name']}")
                    if agent.get('description'):
                        print(f"      └─ {agent['description']}")
        else:
            print("\n📋 No agents found yet")
            print("   (This is normal for a new environment)")
        
        # List tools
        print_section("Available Tools")
        try:
            tools = builder.list_tools()
            if tools:
                print(f"\n🔧 Found {len(tools)} tool(s):\n")
                for tool in tools[:5]:  # Show first 5 tools
                    print(f"    • {tool['name']}")
                    if tool.get('description'):
                        print(f"      └─ {tool['description']}")
                if len(tools) > 5:
                    print(f"\n    ... and {len(tools) - 5} more tools")
            else:
                print("\n🔧 No tools found yet")
        except Exception as e:
            print(f"\n⚠️  Could not list tools: {e}")
        
        # Summary
        print_section("Setup Status")
        print("\n✅ Your watsonx Orchestrate environment is ready!")
        print("\n📚 You can now:")
        print("   • Create agents")
        print("   • Build custom tools")
        print("   • Deploy to production")
        print("\n🚀 Continue to Part 2 to build your first agent!")
        
        return True
        
    except ConnectionError as e:
        print(f"\n❌ Connection Error: {e}")
        print("\n🔧 Troubleshooting tips:")
        print("   1. Check your network connection")
        print("   2. Verify the service endpoint is correct")
        print("   3. If using Developer Edition, ensure it's running:")
        print("      docker ps")
        return False
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n🔧 Troubleshooting tips:")
        print("   1. Check your API key is correct")
        print("   2. Configure your environment:")
        print("      orchestrate environment add")
        print("      orchestrate environment activate <name>")
        print("   3. Or use environment variables:")
        print("      export WO_URL='your-url'")
        print("      export WO_API_KEY='your-key'")
        print("   4. List configured environments:")
        print("      orchestrate environment list")
        return False

if __name__ == "__main__":
    success = verify_setup()
    exit(0 if success else 1)

# Made with Bob
