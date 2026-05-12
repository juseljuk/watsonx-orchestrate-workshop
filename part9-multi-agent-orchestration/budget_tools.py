"""
Budget analysis and optimization tools for the travel planning system.
Provides mock implementations for cost calculation, comparison, deal finding, and budget optimization.
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def calculate_trip_cost(
    destination: str,
    duration_days: int,
    flights_cost: float | None = None,
    hotels_cost: float | None = None,
    activities_cost: float | None = None,
    meals_budget: float | None = None,
    transportation_budget: float | None = None
) -> dict:
    """
    Calculate total trip cost with detailed breakdown.
    
    Args:
        destination: Trip destination
        duration_days: Number of days
        flights_cost: Cost of flights (if known)
        hotels_cost: Cost of hotels (if known)
        activities_cost: Cost of activities (if known)
        meals_budget: Daily meals budget (if known)
        transportation_budget: Local transportation budget (if known)
    
    Returns:
        Detailed cost breakdown and total
    """
    # Use provided costs or estimate based on destination
    destination_multiplier = {
        "budget": 0.8,
        "moderate": 1.0,
        "expensive": 1.5
    }
    
    # Determine destination tier (simplified logic)
    tier = "moderate"
    if any(city in destination.lower() for city in ["tokyo", "london", "paris", "new york", "zurich"]):
        tier = "expensive"
    elif any(city in destination.lower() for city in ["bangkok", "mexico city", "prague", "budapest"]):
        tier = "budget"
    
    multiplier = destination_multiplier[tier]
    
    # Calculate or use provided costs
    flights = flights_cost if flights_cost else 800.00 * multiplier
    hotels = hotels_cost if hotels_cost else (150.00 * duration_days * multiplier)
    activities = activities_cost if activities_cost else (100.00 * duration_days * multiplier)
    meals = (meals_budget * duration_days) if meals_budget else (60.00 * duration_days * multiplier)
    transportation = (transportation_budget * duration_days) if transportation_budget else (30.00 * duration_days * multiplier)
    
    # Additional costs
    travel_insurance = 50.00
    miscellaneous = 100.00 * multiplier
    
    total = flights + hotels + activities + meals + transportation + travel_insurance + miscellaneous
    
    breakdown = {
        "flights": {
            "cost": round(flights, 2),
            "percentage": round((flights / total) * 100, 1),
            "notes": "Round-trip airfare"
        },
        "accommodation": {
            "cost": round(hotels, 2),
            "percentage": round((hotels / total) * 100, 1),
            "notes": f"{duration_days} nights"
        },
        "activities": {
            "cost": round(activities, 2),
            "percentage": round((activities / total) * 100, 1),
            "notes": "Tours, attractions, entertainment"
        },
        "meals": {
            "cost": round(meals, 2),
            "percentage": round((meals / total) * 100, 1),
            "notes": f"${round(meals/duration_days, 2)} per day"
        },
        "transportation": {
            "cost": round(transportation, 2),
            "percentage": round((transportation / total) * 100, 1),
            "notes": "Local transport, taxis, metro"
        },
        "insurance": {
            "cost": travel_insurance,
            "percentage": round((travel_insurance / total) * 100, 1),
            "notes": "Travel insurance"
        },
        "miscellaneous": {
            "cost": round(miscellaneous, 2),
            "percentage": round((miscellaneous / total) * 100, 1),
            "notes": "Shopping, tips, emergencies"
        }
    }
    
    return {
        "destination": destination,
        "duration_days": duration_days,
        "destination_tier": tier,
        "total_cost": round(total, 2),
        "cost_per_day": round(total / duration_days, 2),
        "breakdown": breakdown,
        "currency": "USD",
        "summary": f"Total estimated cost for {duration_days}-day trip to {destination}: ${round(total, 2)}"
    }


@tool
def compare_options(
    option_a: dict,
    option_b: dict,
    priorities: list | None = None
) -> dict:
    """
    Compare two travel options and provide recommendation.
    
    Args:
        option_a: First option with details (name, cost, features)
        option_b: Second option with details (name, cost, features)
        priorities: List of priorities (e.g., ["cost", "comfort", "time"])
    
    Returns:
        Detailed comparison and recommendation
    """
    if not priorities:
        priorities = ["cost", "value"]
    
    # Extract costs
    cost_a = option_a.get("cost", 0)
    cost_b = option_b.get("cost", 0)
    
    # Calculate savings
    savings = abs(cost_a - cost_b)
    cheaper_option = "Option A" if cost_a < cost_b else "Option B"
    savings_percentage = round((savings / max(cost_a, cost_b)) * 100, 1)
    
    # Mock scoring based on priorities
    scores = {
        "Option A": {
            "cost": 8 if cost_a < cost_b else 6,
            "comfort": 7,
            "convenience": 8,
            "value": 8,
            "time": 7
        },
        "Option B": {
            "cost": 8 if cost_b < cost_a else 6,
            "comfort": 8,
            "convenience": 7,
            "value": 7,
            "time": 8
        }
    }
    
    # Calculate weighted scores
    total_score_a = sum(scores["Option A"].get(p, 5) for p in priorities) / len(priorities)
    total_score_b = sum(scores["Option B"].get(p, 5) for p in priorities) / len(priorities)
    
    recommended = "Option A" if total_score_a > total_score_b else "Option B"
    
    comparison = {
        "option_a": {
            "name": option_a.get("name", "Option A"),
            "cost": cost_a,
            "score": round(total_score_a, 1),
            "pros": option_a.get("pros", ["Lower cost", "Good value"]),
            "cons": option_a.get("cons", ["Less luxurious"])
        },
        "option_b": {
            "name": option_b.get("name", "Option B"),
            "cost": cost_b,
            "score": round(total_score_b, 1),
            "pros": option_b.get("pros", ["More comfortable", "Better amenities"]),
            "cons": option_b.get("cons", ["Higher cost"])
        },
        "cost_difference": round(savings, 2),
        "savings_percentage": savings_percentage,
        "cheaper_option": cheaper_option,
        "recommended": recommended,
        "recommendation_reason": f"Based on your priorities ({', '.join(priorities)}), {recommended} offers the best overall value.",
        "priorities_considered": priorities
    }
    
    return comparison


@tool
def find_deals(
    destination: str,
    travel_dates: str | None = None,
    category: str | None = None
) -> dict:
    """
    Find current deals and discounts for travel.
    
    Args:
        destination: Destination to find deals for
        travel_dates: Travel dates (YYYY-MM-DD to YYYY-MM-DD)
        category: Deal category ("flights", "hotels", "activities", "packages")
    
    Returns:
        Available deals and savings opportunities
    """
    # Mock deals data
    all_deals = [
        {
            "type": "flight",
            "title": "Early Bird Flight Discount",
            "description": "Book 30+ days in advance and save 15%",
            "savings": "15%",
            "savings_amount": 120.00,
            "valid_until": "2024-12-31",
            "conditions": ["Book 30 days in advance", "Non-refundable"],
            "how_to_claim": "Use code EARLY15 at checkout"
        },
        {
            "type": "hotel",
            "title": "Extended Stay Discount",
            "description": "Stay 5+ nights and get 20% off",
            "savings": "20%",
            "savings_amount": 180.00,
            "valid_until": "2024-12-31",
            "conditions": ["Minimum 5 nights", "Select hotels only"],
            "how_to_claim": "Automatically applied for qualifying stays"
        },
        {
            "type": "activity",
            "title": "Combo Tour Package",
            "description": "Book 3+ activities and save 25%",
            "savings": "25%",
            "savings_amount": 75.00,
            "valid_until": "2024-11-30",
            "conditions": ["Book 3 or more activities", "Same day booking"],
            "how_to_claim": "Use code COMBO25"
        },
        {
            "type": "package",
            "title": "Complete Travel Package",
            "description": "Book flight + hotel + activities together",
            "savings": "30%",
            "savings_amount": 450.00,
            "valid_until": "2024-12-31",
            "conditions": ["All components booked together", "Minimum 4 nights"],
            "how_to_claim": "Select package option at booking"
        },
        {
            "type": "hotel",
            "title": "Last Minute Deal",
            "description": "Book within 48 hours of check-in",
            "savings": "35%",
            "savings_amount": 210.00,
            "valid_until": "Ongoing",
            "conditions": ["Book within 48 hours", "Subject to availability"],
            "how_to_claim": "Check last-minute section"
        }
    ]
    
    # Filter by category if specified
    if category:
        deals = [d for d in all_deals if d["type"] == category.lower()]
    else:
        deals = all_deals
    
    total_potential_savings = sum(d["savings_amount"] for d in deals)
    
    return {
        "destination": destination,
        "travel_dates": travel_dates,
        "category": category,
        "deals": deals,
        "count": len(deals),
        "total_potential_savings": round(total_potential_savings, 2),
        "best_deal": max(deals, key=lambda x: x["savings_amount"]) if deals else None,
        "tips": [
            "Book early for best flight prices",
            "Consider flexible dates for better deals",
            "Package deals often provide best value",
            "Sign up for price alerts",
            "Check for seasonal promotions"
        ]
    }


@tool
def budget_optimizer(
    total_budget: float,
    duration_days: int,
    priorities: list | None = None,
    must_haves: list | None = None
) -> dict:
    """
    Optimize budget allocation across trip categories.
    
    Args:
        total_budget: Total available budget
        duration_days: Trip duration in days
        priorities: List of priorities (e.g., ["accommodation", "activities"])
        must_haves: List of must-have items/experiences
    
    Returns:
        Optimized budget allocation recommendations
    """
    if not priorities:
        priorities = ["balanced"]
    
    # Define allocation strategies
    strategies = {
        "balanced": {
            "flights": 0.30,
            "accommodation": 0.30,
            "activities": 0.20,
            "meals": 0.15,
            "other": 0.05
        },
        "luxury_accommodation": {
            "flights": 0.25,
            "accommodation": 0.45,
            "activities": 0.15,
            "meals": 0.10,
            "other": 0.05
        },
        "experience_focused": {
            "flights": 0.25,
            "accommodation": 0.20,
            "activities": 0.35,
            "meals": 0.15,
            "other": 0.05
        },
        "budget_conscious": {
            "flights": 0.35,
            "accommodation": 0.25,
            "activities": 0.20,
            "meals": 0.15,
            "other": 0.05
        }
    }
    
    # Select strategy based on priorities
    if "accommodation" in priorities or "comfort" in priorities:
        strategy = strategies["luxury_accommodation"]
        strategy_name = "Luxury Accommodation Focus"
    elif "activities" in priorities or "experiences" in priorities:
        strategy = strategies["experience_focused"]
        strategy_name = "Experience-Focused"
    elif "budget" in priorities or "savings" in priorities:
        strategy = strategies["budget_conscious"]
        strategy_name = "Budget-Conscious"
    else:
        strategy = strategies["balanced"]
        strategy_name = "Balanced Approach"
    
    # Calculate allocations
    allocations = {}
    for category, percentage in strategy.items():
        amount = total_budget * percentage
        allocations[category] = {
            "amount": round(amount, 2),
            "percentage": round(percentage * 100, 1),
            "daily_budget": round(amount / duration_days, 2) if category != "flights" else None
        }
    
    # Add recommendations
    recommendations = [
        f"Allocate ${allocations['flights']['amount']} for flights - book early for best prices",
        f"Budget ${allocations['accommodation']['amount']} for accommodation (${allocations['accommodation']['daily_budget']}/night)",
        f"Set aside ${allocations['activities']['amount']} for activities and tours",
        f"Plan ${allocations['meals']['daily_budget']}/day for meals",
        f"Keep ${allocations['other']['amount']} as buffer for unexpected expenses"
    ]
    
    # Add must-haves impact
    must_haves_cost = 0
    if must_haves:
        must_haves_cost = len(must_haves) * 100  # Estimate $100 per must-have
        recommendations.append(f"Reserve approximately ${must_haves_cost} for must-have experiences: {', '.join(must_haves)}")
    
    remaining_budget = total_budget - must_haves_cost
    
    return {
        "total_budget": total_budget,
        "duration_days": duration_days,
        "strategy": strategy_name,
        "priorities": priorities,
        "must_haves": must_haves,
        "allocations": allocations,
        "daily_budget": round(total_budget / duration_days, 2),
        "must_haves_cost": must_haves_cost,
        "remaining_flexible_budget": round(remaining_budget, 2),
        "recommendations": recommendations,
        "savings_tips": [
            "Book flights on Tuesday/Wednesday for better prices",
            "Consider accommodations with kitchen to save on meals",
            "Look for free walking tours and activities",
            "Use public transportation instead of taxis",
            "Book activities online in advance for discounts",
            "Travel during shoulder season for better rates"
        ],
        "warning": "Budget is tight - consider extending trip duration or reducing scope" if total_budget / duration_days < 100 else None
    }

# Made with Bob