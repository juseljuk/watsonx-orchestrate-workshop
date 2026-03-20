"""
Order Status Tool for watsonx Orchestrate
Checks the status of customer orders (simulated for workshop)
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from datetime import datetime, timedelta
import random

@tool
def check_order_status(order_id: str) -> dict:
    """
    Retrieves the current status and details of a customer order by order ID.
    Use this when customers ask about their order status, delivery date, or order details.
    
    Args:
        order_id: The unique order identifier (e.g., ORD-12345). Must start with 'ORD-' followed by numbers.
        
    Returns:
        Dictionary with order details including status, items, dates, and tracking
    """
    # Validate order ID format
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
    
    # Extract order number
    try:
        order_num = order_id.split("-")[1]
        if not order_num.isdigit():
            raise ValueError("Order number must be numeric")
    except (IndexError, ValueError):
        return {
            "success": False,
            "error": "Invalid order ID format. Expected format: ORD-12345"
        }
    
    # Simulate order lookup with deterministic randomness based on order ID
    random.seed(order_id)
    
    statuses = ["Processing", "Shipped", "Out for Delivery", "Delivered"]
    status = random.choice(statuses)
    
    # Generate mock order data
    order_date = datetime.now() - timedelta(days=random.randint(1, 10))
    delivery_date = order_date + timedelta(days=random.randint(3, 7))
    
    # Sample items
    all_items = [
        {"name": "Laptop", "quantity": 1, "price": 999.99},
        {"name": "Mouse", "quantity": 1, "price": 29.99},
        {"name": "Keyboard", "quantity": 1, "price": 79.99},
        {"name": "Monitor", "quantity": 1, "price": 299.99},
        {"name": "USB Cable", "quantity": 2, "price": 9.99},
        {"name": "Laptop Bag", "quantity": 1, "price": 49.99}
    ]
    
    # Select 2-4 random items
    num_items = random.randint(2, 4)
    items = random.sample(all_items, num_items)
    
    # Calculate total
    total = sum(item["price"] * item["quantity"] for item in items)
    
    # Generate tracking number
    tracking_number = f"TRK{random.randint(100000, 999999)}"
    
    # Build response
    response = {
        "success": True,
        "order_id": order_id,
        "status": status,
        "order_date": order_date.strftime("%Y-%m-%d"),
        "estimated_delivery": delivery_date.strftime("%Y-%m-%d"),
        "items": items,
        "total": f"${total:.2f}",
        "tracking_number": tracking_number,
        "shipping_address": "123 Main St, Anytown, ST 12345"
    }
    
    # Add delivery confirmation if delivered
    if status == "Delivered":
        response["delivered_date"] = (delivery_date - timedelta(days=1)).strftime("%Y-%m-%d")
        response["signed_by"] = "Customer"
    
    return response

# Made with Bob
