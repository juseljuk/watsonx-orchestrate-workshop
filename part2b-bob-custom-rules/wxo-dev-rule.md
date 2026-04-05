## watsonx Orchestrate Development Rule

When working with IBM watsonx Orchestrate or watsonx Orchestrate ADK projects:

1. **Project Structure and folders**: Follow ADK conventions when creating and saving artefacts:
   - tools/ for flows and Python tools
   - agents/ for YAML configurations
   - knowledge_bases/ for knowledge bases
   - models/ for LLM configurations
   - toolkits/ for MCP toolkits
   - import-all.sh for deployment
   - README.md with architecture + workflow diagrams

2. **Key Patterns**:
   - Use @flow decorator for flows
   - Use @tool decorator for Python tools
   - Include inline KVP schemas for document processing
   - Create native agents for document handling
   - Preferably use Command Line Interface to import the agents and tools

3. **MCP Server Integration**:
   - Use `watsonx-orchestrate-adk-docs` MCP server to search IBM watson Orchestrate ADK documentation
   - Leverage MCP tools for finding API references, code examples, and implementation guides
   - Query the knowledge base when uncertain about ADK features or best practices