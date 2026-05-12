"""
Flight booking tools for the travel planning system.
Provides mock implementations for flight search, booking, modification, and cancellation.
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def search_flights(
    origin: str,
    destination: str,
    departure_date: str,
    return_date: str = None,
    passengers: int = 1
) -> dict:
    """
    Search for available flights.
    
    Args:
        origin: Departure city or airport code
        destination: Arrival city or airport code
        departure_date: Departure date (YYYY-MM-DD)
        return_date: Return date for round trip (YYYY-MM-DD)
        passengers: Number of passengers
    
    Returns:
        Dictionary with flight options
    """
    # Mock flight data
    flights = [
        {
            "flight_number": "AA123",
            "airline": "American Airlines",
            "departure": f"{origin} 08:00",
            "arrival": f"{destination} 14:30",
            "duration": "6h 30m",
            "price": 450.00,
            "stops": 0,
            "class": "Economy"
        },
        {
            "flight_number": "UA456",
            "airline": "United Airlines",
            "departure": f"{origin} 10:30",
            "arrival": f"{destination} 17:15",
            "duration": "6h 45m",
            "price": 425.00,
            "stops": 0,
            "class": "Economy"
        },
        {
            "flight_number": "DL789",
            "airline": "Delta",
            "departure": f"{origin} 14:00",
            "arrival": f"{destination} 22:00",
            "duration": "8h 00m",
            "price": 380.00,
            "stops": 1,
            "class": "Economy"
        }
    ]
    
    result = {
        "origin": origin,
        "destination": destination,
        "departure_date": departure_date,
        "return_date": return_date,
        "passengers": passengers,
        "flights": flights,
        "count": len(flights)
    }
    
    if return_date:
        result["trip_type"] = "round-trip"
        result["total_price_range"] = f"${flights[-1]['price'] * 2} - ${flights[0]['price'] * 2}"
    else:
        result["trip_type"] = "one-way"
        result["total_price_range"] = f"${flights[-1]['price']} - ${flights[0]['price']}"
    
    return result


@tool
def book_flight(
    flight_number: str,
    passenger_name: str,
    passenger_email: str
) -> dict:
    """
    Book a flight.
    
    Args:
        flight_number: Flight number to book
        passenger_name: Passenger full name
        passenger_email: Passenger email
    
    Returns:
        Booking confirmation
    """
    import random
    confirmation = f"CONF{random.randint(100000, 999999)}"
    
    return {
        "status": "confirmed",
        "confirmation_number": confirmation,
        "flight_number": flight_number,
        "passenger_name": passenger_name,
        "email": passenger_email,
        "booking_date": "2024-01-15",
        "message": f"Flight {flight_number} booked successfully! Confirmation: {confirmation}",
        "next_steps": [
            "Check-in opens 24 hours before departure",
            "Confirmation email sent to " + passenger_email,
            "Download boarding pass via airline app"
        ]
    }


@tool
def modify_flight(
    confirmation_number: str,
    new_date: str = None,
    new_flight: str = None
) -> dict:
    """
    Modify an existing flight booking.
    
    Args:
        confirmation_number: Booking confirmation number
        new_date: New departure date (optional)
        new_flight: New flight number (optional)
    
    Returns:
        Modification confirmation
    """
    changes = []
    if new_date:
        changes.append(f"Date changed to {new_date}")
    if new_flight:
        changes.append(f"Flight changed to {new_flight}")
    
    return {
        "status": "modified",
        "confirmation_number": confirmation_number,
        "changes": changes,
        "change_fee": 75.00,
        "fare_difference": 25.00,
        "total_cost": 100.00,
        "message": "Flight modified successfully. Total cost: $100.00 (change fee + fare difference)"
    }


@tool
def cancel_flight(confirmation_number: str) -> dict:
    """
    Cancel a flight booking.
    
    Args:
        confirmation_number: Booking confirmation number
    
    Returns:
        Cancellation confirmation
    """
    return {
        "status": "cancelled",
        "confirmation_number": confirmation_number,
        "cancellation_fee": 100.00,
        "refund_amount": 350.00,
        "refund_method": "original payment method",
        "processing_time": "5-7 business days",
        "message": "Flight cancelled. Refund of $350.00 will be processed within 5-7 business days."
    }

# Made with Bob
