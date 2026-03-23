"""
Content Safety Guardrail Plugin for watsonx Orchestrate
Pre-invoke plugin that filters inappropriate content and detects security threats
"""

from ibm_watsonx_orchestrate.agent_builder.plugins import plugin
import re

@plugin(plugin_type="pre_invoke")
def content_safety_guardrail(input_data: dict) -> dict:
    """
    Filter input before it reaches the agent to ensure safety and security.
    
    This guardrail checks for:
    - Sensitive data (passwords, SSN, credit cards)
    - Inappropriate content
    - Prompt injection attempts
    - Security threats
    
    Args:
        input_data: User's message and context
        
    Returns:
        Modified input or blocked response
    """
    user_message = input_data.get("message", "")
    
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
            return {
                "blocked": True,
                "reason": f"sensitive_data_detected_{data_type}",
                "message": (
                    "I noticed you may have shared sensitive information. "
                    "For your security, please don't share passwords, credit card numbers, "
                    "social security numbers, or API keys in chat. "
                    "How else can I help you?"
                )
            }
    
    # Define inappropriate content patterns
    # Note: In production, use a more comprehensive list or external service
    inappropriate_keywords = [
        "profanity1", "profanity2",  # Replace with actual terms
        # Add more as needed
    ]
    
    message_lower = user_message.lower()
    for keyword in inappropriate_keywords:
        if keyword in message_lower:
            return {
                "blocked": True,
                "reason": "inappropriate_content",
                "message": (
                    "I'm here to help with customer support questions. "
                    "Please keep our conversation professional. "
                    "How can I assist you today?"
                )
            }
    
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
            return {
                "blocked": True,
                "reason": "potential_injection",
                "message": (
                    "I'm designed to help with customer support. "
                    "Let me know what you need assistance with!"
                )
            }
    
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
            return {
                "blocked": True,
                "reason": "system_probe",
                "message": (
                    "I'm a customer support agent. "
                    "I can help you with orders, returns, and general inquiries. "
                    "What would you like help with?"
                )
            }
    
    # Check for data exfiltration attempts
    exfiltration_patterns = [
        r'list all (users|customers|orders|accounts)',
        r'show me (all|every) (user|customer|order|account)',
        r'export (all|every) (data|information)',
        r'dump (database|table|records)'
    ]
    
    for pattern in exfiltration_patterns:
        if re.search(pattern, message_lower):
            return {
                "blocked": True,
                "reason": "data_exfiltration_attempt",
                "message": (
                    "I can only access information related to your specific account. "
                    "Please provide your order ID if you need help with an order."
                )
            }
    
    # Input passed all checks - allow it through
    return {
        "blocked": False,
        "input_data": input_data
    }

# Made with Bob
