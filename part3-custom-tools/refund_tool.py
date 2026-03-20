"""
Refund Processing Tool for watsonx Orchestrate
Processes customer refund requests (simulated for workshop)
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from datetime import datetime
import random

@tool
def process_refund(order_id: str, reason: str, amount: float) -> dict:
    """
    Processes a refund request for a customer order.
    Use this when customers request refunds or returns.
    
    Args:
        order_id: The order ID to refund (format: ORD-XXXXX)
        reason: Reason for the refund request (must be at least 10 characters)
        amount: Refund amount in dollars (must be positive and under $10,000)
        
    Returns:
        Refund confirmation details including refund ID, status, and processing time
    """
    # Validation
    if not order_id or not isinstance(order_id, str):
        return {
            "success": False,
            "error": "Order ID is required and must be a string"
        }
    
    if not order_id.startswith("ORD-"):
        return {
            "success": False,
            "error": "Invalid order ID format. Must start with 'ORD-' (e.g., ORD-12345)"
        }
    
    if not reason or not isinstance(reason, str):
        return {
            "success": False,
            "error": "Reason is required and must be a string"
        }
    
    if len(reason.strip()) < 10:
        return {
            "success": False,
            "error": "Please provide a detailed reason (at least 10 characters)"
        }
    
    if not isinstance(amount, (int, float)):
        return {
            "success": False,
            "error": "Amount must be a number"
        }
    
    if amount <= 0:
        return {
            "success": False,
            "error": "Refund amount must be greater than 0"
        }
    
    if amount > 10000:
        return {
            "success": False,
            "error": "Refund amount exceeds maximum ($10,000). Please contact a manager for approval.",
            "requires_approval": True
        }
    
    # Process refund (simulated)
    # Use order_id as seed for consistent refund IDs
    random.seed(order_id + reason)
    refund_id = f"REF-{random.randint(10000, 99999)}"
    
    # Determine processing time based on amount
    if amount < 100:
        processing_time = "1-2 business days"
    elif amount < 500:
        processing_time = "3-5 business days"
    else:
        processing_time = "5-7 business days"
    
    return {
        "success": True,
        "refund_id": refund_id,
        "order_id": order_id,
        "amount": f"${amount:.2f}",
        "reason": reason,
        "status": "Approved",
        "processing_time": processing_time,
        "refund_method": "Original payment method",
        "confirmation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message": f"Your refund of ${amount:.2f} has been approved and will be processed within {processing_time}."
    }

# Made with Bob
