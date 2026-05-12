"""
Activity planning tools for the travel planning system.
Provides mock implementations for activity search, details, restaurants, and itinerary creation.
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def search_activities(
    location: str,
    interests: list | None = None,
    date: str | None = None,
    duration: str | None = None
) -> dict:
    """
    Search for activities and attractions in a location.
    
    Args:
        location: City or area to search
        interests: List of interests (e.g., ["culture", "adventure", "food"])
        date: Date for the activity (YYYY-MM-DD)
        duration: Preferred duration (e.g., "half-day", "full-day")
    
    Returns:
        Dictionary with activity options
    """
    # Mock activity data
    activities = [
        {
            "name": "Historic City Walking Tour",
            "type": "culture",
            "duration": "3 hours",
            "price": 45.00,
            "rating": 4.8,
            "description": "Explore the historic downtown with an expert guide",
            "best_time": "Morning (9 AM - 12 PM)",
            "booking_required": True,
            "group_size": "Up to 15 people"
        },
        {
            "name": "Food Market Experience",
            "type": "food",
            "duration": "2.5 hours",
            "price": 65.00,
            "rating": 4.9,
            "description": "Taste local specialties and learn about regional cuisine",
            "best_time": "Morning (10 AM - 12:30 PM)",
            "booking_required": True,
            "group_size": "Up to 12 people"
        },
        {
            "name": "Adventure Park & Zip Line",
            "type": "adventure",
            "duration": "4 hours",
            "price": 85.00,
            "rating": 4.7,
            "description": "Thrilling outdoor activities including zip lines and rope courses",
            "best_time": "Afternoon (1 PM - 5 PM)",
            "booking_required": True,
            "group_size": "Up to 20 people"
        },
        {
            "name": "Museum of Modern Art",
            "type": "culture",
            "duration": "2 hours",
            "price": 25.00,
            "rating": 4.6,
            "description": "World-class collection of contemporary art",
            "best_time": "Any time (10 AM - 6 PM)",
            "booking_required": False,
            "group_size": "No limit"
        },
        {
            "name": "Sunset Harbor Cruise",
            "type": "leisure",
            "duration": "2 hours",
            "price": 55.00,
            "rating": 4.8,
            "description": "Scenic cruise with stunning sunset views",
            "best_time": "Evening (6 PM - 8 PM)",
            "booking_required": True,
            "group_size": "Up to 50 people"
        }
    ]
    
    # Filter by interests if provided
    if interests:
        filtered = [a for a in activities if a["type"] in interests]
        if filtered:
            activities = filtered
    
    return {
        "location": location,
        "date": date,
        "interests": interests,
        "activities": activities,
        "count": len(activities),
        "total_price_range": f"${min(a['price'] for a in activities)} - ${max(a['price'] for a in activities)}"
    }


@tool
def get_activity_details(activity_name: str) -> dict:
    """
    Get detailed information about a specific activity.
    
    Args:
        activity_name: Name of the activity
    
    Returns:
        Detailed activity information
    """
    # Mock detailed data
    details = {
        "name": activity_name,
        "full_description": f"Comprehensive experience of {activity_name} with expert guidance and all necessary equipment included.",
        "duration": "3 hours",
        "price": 45.00,
        "rating": 4.8,
        "reviews_count": 342,
        "included": [
            "Professional guide",
            "All equipment",
            "Hotel pickup (optional)",
            "Refreshments"
        ],
        "not_included": [
            "Meals",
            "Personal expenses",
            "Gratuities"
        ],
        "requirements": [
            "Comfortable walking shoes",
            "Weather-appropriate clothing",
            "Minimum age: 12 years"
        ],
        "cancellation_policy": "Free cancellation up to 24 hours before",
        "meeting_point": "Main entrance of City Hall",
        "languages": ["English", "Spanish", "French"],
        "accessibility": "Wheelchair accessible",
        "max_group_size": 15
    }
    
    return details


@tool
def search_restaurants(
    location: str,
    cuisine: str | None = None,
    price_range: str | None = None,
    meal_type: str | None = None
) -> dict:
    """
    Search for restaurants in a location.
    
    Args:
        location: City or area
        cuisine: Type of cuisine (e.g., "Italian", "Japanese", "Local")
        price_range: Budget level ("$", "$$", "$$$", "$$$$")
        meal_type: Type of meal ("breakfast", "lunch", "dinner")
    
    Returns:
        Dictionary with restaurant options
    """
    restaurants = [
        {
            "name": "La Bella Vista",
            "cuisine": "Italian",
            "price_range": "$$$",
            "rating": 4.7,
            "specialties": ["Pasta", "Seafood", "Wine"],
            "average_cost": 65.00,
            "atmosphere": "Romantic, Fine Dining",
            "reservation_required": True,
            "dress_code": "Smart Casual",
            "hours": "5 PM - 11 PM"
        },
        {
            "name": "Sushi Master",
            "cuisine": "Japanese",
            "price_range": "$$$$",
            "rating": 4.9,
            "specialties": ["Omakase", "Sashimi", "Sake"],
            "average_cost": 120.00,
            "atmosphere": "Intimate, Traditional",
            "reservation_required": True,
            "dress_code": "Business Casual",
            "hours": "6 PM - 10 PM"
        },
        {
            "name": "Local Flavors Bistro",
            "cuisine": "Local",
            "price_range": "$$",
            "rating": 4.5,
            "specialties": ["Regional dishes", "Farm-to-table", "Craft beer"],
            "average_cost": 35.00,
            "atmosphere": "Casual, Friendly",
            "reservation_required": False,
            "dress_code": "Casual",
            "hours": "11 AM - 10 PM"
        },
        {
            "name": "The Morning Spot",
            "cuisine": "American",
            "price_range": "$",
            "rating": 4.4,
            "specialties": ["Breakfast", "Brunch", "Coffee"],
            "average_cost": 18.00,
            "atmosphere": "Cozy, Casual",
            "reservation_required": False,
            "dress_code": "Casual",
            "hours": "7 AM - 3 PM"
        },
        {
            "name": "Spice Route",
            "cuisine": "Indian",
            "price_range": "$$",
            "rating": 4.6,
            "specialties": ["Curry", "Tandoori", "Vegetarian"],
            "average_cost": 40.00,
            "atmosphere": "Vibrant, Family-friendly",
            "reservation_required": False,
            "dress_code": "Casual",
            "hours": "12 PM - 10 PM"
        }
    ]
    
    # Filter by cuisine if provided
    if cuisine:
        filtered = [r for r in restaurants if r["cuisine"].lower() == cuisine.lower()]
        if filtered:
            restaurants = filtered
    
    # Filter by price range if provided
    if price_range:
        filtered = [r for r in restaurants if r["price_range"] == price_range]
        if filtered:
            restaurants = filtered
    
    return {
        "location": location,
        "cuisine": cuisine,
        "price_range": price_range,
        "meal_type": meal_type,
        "restaurants": restaurants,
        "count": len(restaurants)
    }


@tool
def create_itinerary(
    location: str,
    duration_days: int,
    interests: list | None = None,
    pace: str = "moderate"
) -> dict:
    """
    Create a day-by-day itinerary for a trip.
    
    Args:
        location: Destination city or area
        duration_days: Number of days for the trip
        interests: List of interests to focus on
        pace: Trip pace ("relaxed", "moderate", "packed")
    
    Returns:
        Detailed day-by-day itinerary
    """
    # Mock itinerary based on duration
    daily_plans = []
    
    activities_per_day = {
        "relaxed": 2,
        "moderate": 3,
        "packed": 4
    }
    
    num_activities = activities_per_day.get(pace, 3)
    
    sample_activities = [
        {"time": "9:00 AM", "activity": "Historic City Walking Tour", "duration": "3 hours"},
        {"time": "1:00 PM", "activity": "Lunch at Local Flavors Bistro", "duration": "1.5 hours"},
        {"time": "3:00 PM", "activity": "Museum of Modern Art", "duration": "2 hours"},
        {"time": "6:00 PM", "activity": "Sunset Harbor Cruise", "duration": "2 hours"},
        {"time": "8:30 PM", "activity": "Dinner at La Bella Vista", "duration": "2 hours"}
    ]
    
    for day in range(1, duration_days + 1):
        day_plan = {
            "day": day,
            "date": f"Day {day}",
            "theme": f"Exploring {location}",
            "activities": sample_activities[:num_activities],
            "meals": {
                "breakfast": "Hotel breakfast or The Morning Spot",
                "lunch": "Local Flavors Bistro",
                "dinner": "La Bella Vista or Spice Route"
            },
            "estimated_cost": 150.00 + (num_activities * 45.00),
            "notes": [
                "Book activities in advance",
                "Wear comfortable shoes",
                "Bring camera for scenic spots"
            ]
        }
        daily_plans.append(day_plan)
    
    total_cost = sum(day["estimated_cost"] for day in daily_plans)
    
    return {
        "location": location,
        "duration_days": duration_days,
        "pace": pace,
        "interests": interests,
        "itinerary": daily_plans,
        "total_estimated_cost": total_cost,
        "summary": {
            "total_activities": len(daily_plans) * num_activities,
            "total_meals": duration_days * 3,
            "recommended_budget": total_cost,
            "best_for": f"{pace.capitalize()} travelers interested in {', '.join(interests) if interests else 'general sightseeing'}"
        },
        "tips": [
            "Book popular activities 2-3 days in advance",
            "Consider purchasing a city pass for attractions",
            "Download offline maps before your trip",
            "Keep some flexibility for spontaneous discoveries"
        ]
    }

# Made with Bob