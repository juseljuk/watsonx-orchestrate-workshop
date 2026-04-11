"""
Hotel booking tools for the travel planning system.
Provides mock implementations for hotel search, booking, modification, and cancellation.
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def search_hotels(
    location: str,
    check_in: str,
    check_out: str,
    guests: int = 2,
    max_price: float = None
) -> dict:
    """
    Search for available hotels.
    
    Args:
        location: City or area
        check_in: Check-in date (YYYY-MM-DD)
        check_out: Check-out date (YYYY-MM-DD)
        guests: Number of guests
        max_price: Maximum price per night
    
    Returns:
        Dictionary with hotel options
    """
    hotels = [
        {
            "name": "Grand Plaza Hotel",
            "location": location,
            "rating": 4.5,
            "price_per_night": 180.00,
            "amenities": ["WiFi", "Breakfast", "Pool", "Gym", "Parking"],
            "cancellation": "Free cancellation until 24h before",
            "distance_to_center": "0.5 miles"
        },
        {
            "name": "City Center Inn",
            "location": location,
            "rating": 4.0,
            "price_per_night": 120.00,
            "amenities": ["WiFi", "Breakfast", "Business Center"],
            "cancellation": "Free cancellation until 48h before",
            "distance_to_center": "0.2 miles"
        },
        {
            "name": "Budget Stay",
            "location": location,
            "rating": 3.5,
            "price_per_night": 80.00,
            "amenities": ["WiFi", "24h Reception"],
            "cancellation": "Non-refundable",
            "distance_to_center": "1.5 miles"
        },
        {
            "name": "Luxury Suites",
            "location": location,
            "rating": 5.0,
            "price_per_night": 350.00,
            "amenities": ["WiFi", "Breakfast", "Pool", "Spa", "Gym", "Restaurant", "Parking"],
            "cancellation": "Free cancellation until 72h before",
            "distance_to_center": "0.3 miles"
        }
    ]
    
    # Filter by max price if specified
    if max_price:
        hotels = [h for h in hotels if h["price_per_night"] <= max_price]
    
    # Calculate total cost
    from datetime import datetime
    check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
    check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
    nights = (check_out_date - check_in_date).days
    
    for hotel in hotels:
        hotel["total_cost"] = hotel["price_per_night"] * nights
        hotel["nights"] = nights
    
    return {
        "location": location,
        "check_in": check_in,
        "check_out": check_out,
        "guests": guests,
        "nights": nights,
        "hotels": hotels,
        "count": len(hotels)
    }


@tool
def book_hotel(
    hotel_name: str,
    guest_name: str,
    guest_email: str,
    check_in: str,
    check_out: str,
    room_type: str = "Standard"
) -> dict:
    """
    Book a hotel room.
    
    Args:
        hotel_name: Name of the hotel
        guest_name: Guest full name
        guest_email: Guest email
        check_in: Check-in date
        check_out: Check-out date
        room_type: Type of room (Standard, Deluxe, Suite)
    
    Returns:
        Booking confirmation
    """
    import random
    confirmation = f"HTL{random.randint(100000, 999999)}"
    
    return {
        "status": "confirmed",
        "confirmation_number": confirmation,
        "hotel_name": hotel_name,
        "guest_name": guest_name,
        "check_in": check_in,
        "check_out": check_out,
        "room_type": room_type,
        "email": guest_email,
        "message": f"Hotel booked successfully! Confirmation: {confirmation}",
        "check_in_time": "3:00 PM",
        "check_out_time": "11:00 AM",
        "next_steps": [
            "Confirmation email sent to " + guest_email,
            "Check-in starts at 3:00 PM",
            "Early check-in available upon request"
        ]
    }


@tool
def modify_hotel_booking(
    confirmation_number: str,
    new_check_in: str = None,
    new_check_out: str = None,
    new_room_type: str = None
) -> dict:
    """
    Modify hotel booking dates or room type.
    
    Args:
        confirmation_number: Booking confirmation number
        new_check_in: New check-in date (optional)
        new_check_out: New check-out date (optional)
        new_room_type: New room type (optional)
    
    Returns:
        Modification confirmation
    """
    changes = []
    if new_check_in:
        changes.append(f"Check-in changed to {new_check_in}")
    if new_check_out:
        changes.append(f"Check-out changed to {new_check_out}")
    if new_room_type:
        changes.append(f"Room type changed to {new_room_type}")
    
    return {
        "status": "modified",
        "confirmation_number": confirmation_number,
        "changes": changes,
        "modification_fee": 0.00,
        "message": "Hotel booking modified successfully. No modification fee."
    }


@tool
def cancel_hotel_booking(confirmation_number: str) -> dict:
    """
    Cancel hotel booking.
    
    Args:
        confirmation_number: Booking confirmation number
    
    Returns:
        Cancellation confirmation
    """
    return {
        "status": "cancelled",
        "confirmation_number": confirmation_number,
        "refund_amount": 240.00,
        "cancellation_fee": 0.00,
        "refund_method": "original payment method",
        "processing_time": "3-5 business days",
        "message": "Hotel booking cancelled. Full refund of $240.00 will be processed within 3-5 business days."
    }

# Made with Bob
