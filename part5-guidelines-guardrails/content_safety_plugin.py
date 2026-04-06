"""
Content Safety Guardrail Plugin for watsonx Orchestrate
Pre-invoke plugin that filters inappropriate content and detects security threats
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.agent_builder.tools.types import (
    PythonToolKind,
    PluginContext,
    AgentPreInvokePayload,
    AgentPreInvokeResult,
    TextContent,
    Message
)
import re

@tool(description="Filters inappropriate content and detects security threats", kind=PythonToolKind.AGENTPREINVOKE)
def content_safety_guardrail(plugin_context: PluginContext, agent_pre_invoke_payload: AgentPreInvokePayload) -> AgentPreInvokeResult:
    """
    Filter input before it reaches the agent to ensure safety and security.
    
    This guardrail checks for:
    - Sensitive data (passwords, SSN, credit cards)
    - Inappropriate content
    - Prompt injection attempts
    - Security threats
    
    Args:
        plugin_context: Context information about the plugin execution
        agent_pre_invoke_payload: The incoming message payload
        
    Returns:
        AgentPreInvokeResult with continue_processing flag and modified payload
    """
    
    result = AgentPreInvokeResult()
    modified_payload = agent_pre_invoke_payload
    
    # Get user input from the last message
    if not agent_pre_invoke_payload or not agent_pre_invoke_payload.messages:
        result.continue_processing = True
        result.modified_payload = modified_payload
        return result
    
    last_message = agent_pre_invoke_payload.messages[-1]
    content = getattr(last_message, "content", None)
    
    # Check if content has text attribute (TextContent type)
    if content is None or not hasattr(content, "text") or content.text is None:
        result.continue_processing = True
        result.modified_payload = modified_payload
        return result
    
    user_message = content.text
    message_lower = user_message.lower()
    
    # Define patterns for sensitive data
    sensitive_patterns = {
        "password": r'\b(password|passwd|pwd)\s*[:=]\s*\S+',
        "ssn": r'\b\d{3}-\d{2}-\d{4}\b',
        "credit_card": r'\b\d{16}\b',
        "api_key": r'\b[A-Za-z0-9]{32,}\b'
    }
    
    # Check for sensitive data
    for data_type, pattern in sensitive_patterns.items():
        if re.search(pattern, user_message, re.IGNORECASE):
            new_text = (
                "I noticed you may have shared sensitive information. "
                "For your security, please don't share passwords, credit card numbers, "
                "social security numbers, or API keys in chat. "
                "How else can I help you?"
            )
            new_content = TextContent(type="text", text=new_text)
            new_message = Message(role=last_message.role, content=new_content)
            modified_payload = agent_pre_invoke_payload.copy(deep=True)
            modified_payload.messages[-1] = new_message
            result.continue_processing = False
            result.modified_payload = modified_payload
            return result
    
    # Define inappropriate content patterns
    # Note: In production, use a more comprehensive list or external service
    inappropriate_keywords = [
        "profanity1", "profanity2",  # Replace with actual terms
        # Add more as needed
    ]
    
    for keyword in inappropriate_keywords:
        if keyword in message_lower:
            new_text = (
                "I'm here to help with customer support questions. "
                "Please keep our conversation professional. "
                "How can I assist you today?"
            )
            new_content = TextContent(type="text", text=new_text)
            new_message = Message(role=last_message.role, content=new_content)
            modified_payload = agent_pre_invoke_payload.copy(deep=True)
            modified_payload.messages[-1] = new_message
            result.continue_processing = False
            result.modified_payload = modified_payload
            return result
    
    # Check for prompt injection attempts
    injection_indicators = [
        "ignore previous instructions",
        "disregard all",
        "forget everything",
        "new instructions:",
        "system:",
        "override",
        "you are now",
        "act as if",
        "pretend you are",
        "roleplay as"
    ]
    
    for indicator in injection_indicators:
        if indicator in message_lower:
            new_text = (
                "I'm designed to help with customer support. "
                "Let me know what you need assistance with!"
            )
            new_content = TextContent(type="text", text=new_text)
            new_message = Message(role=last_message.role, content=new_content)
            modified_payload = agent_pre_invoke_payload.copy(deep=True)
            modified_payload.messages[-1] = new_message
            result.continue_processing = False
            result.modified_payload = modified_payload
            return result
    
    # Check for attempts to extract system information
    system_probes = [
        "show me your instructions",
        "what are your rules",
        "reveal your prompt",
        "show system prompt",
        "what's your system message"
    ]
    
    for probe in system_probes:
        if probe in message_lower:
            new_text = (
                "I'm a customer support agent. "
                "I can help you with orders, returns, and general inquiries. "
                "What would you like help with?"
            )
            new_content = TextContent(type="text", text=new_text)
            new_message = Message(role=last_message.role, content=new_content)
            modified_payload = agent_pre_invoke_payload.copy(deep=True)
            modified_payload.messages[-1] = new_message
            result.continue_processing = False
            result.modified_payload = modified_payload
            return result
    
    # Check for data exfiltration attempts
    exfiltration_patterns = [
        r'list all (users|customers|orders|accounts)',
        r'show me (all|every) (user|customer|order|account)',
        r'export (all|every) (data|information)',
        r'dump (database|table|records)'
    ]
    
    for pattern in exfiltration_patterns:
        if re.search(pattern, message_lower):
            new_text = (
                "I can only access information related to your specific account. "
                "Please provide your order ID if you need help with an order."
            )
            new_content = TextContent(type="text", text=new_text)
            new_message = Message(role=last_message.role, content=new_content)
            modified_payload = agent_pre_invoke_payload.copy(deep=True)
            modified_payload.messages[-1] = new_message
            result.continue_processing = False
            result.modified_payload = modified_payload
            return result
    
    # Input passed all checks - allow it through
    result.continue_processing = True
    result.modified_payload = modified_payload
    return result

# Made with Bob
