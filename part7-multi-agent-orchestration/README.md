# Part 7: Multi-Agent Orchestration & Workflows

**Duration**: 30 minutes  
**Difficulty**: Advanced

## Overview

In this lesson, you'll learn how to build sophisticated multi-agent systems where specialized agents work together to solve complex tasks. You'll create agent hierarchies, implement routing logic, and orchestrate workflows across multiple agents.

### What You'll Learn

- When and why to use multiple agents
- Creating specialized agents for specific domains
- Building agent hierarchies (parent-child relationships)
- Implementing intelligent routing between agents
- Managing context and handoffs
- Best practices for multi-agent systems

### What You'll Build

A **Travel Planning System** with multiple specialized agents:
- **Travel Concierge** (parent) - Routes requests to specialists
- **Flight Specialist** - Handles flight bookings
- **Hotel Specialist** - Manages accommodation
- **Activity Planner** - Suggests local activities
- **Budget Advisor** - Provides cost analysis

---

## Why Multi-Agent Systems?

### Single Agent vs Multi-Agent

**Single Agent Approach:**
```
Customer Support Agent
├── 50+ tools
├── 10+ knowledge bases
├── Complex instructions (1000+ lines)
└── Handles everything
```

**Problems:**
- ❌ Overwhelming complexity
- ❌ Difficult to maintain
- ❌ Poor performance on specialized tasks
- ❌ Hard to test and debug

**Multi-Agent Approach:**
```
Orchestrator Agent
├── Order Specialist (5 tools, focused instructions)
├── Billing Specialist (3 tools, focused instructions)
├── Technical Support (8 tools, focused instructions)
└── Escalation Handler (2 tools, focused instructions)
```

**Benefits:**
- ✅ Clear separation of concerns
- ✅ Easier to maintain and update
- ✅ Better performance on specialized tasks
- ✅ Simpler testing and debugging
- ✅ Reusable specialists across systems

### When to Use Multi-Agent Systems

| Use Multi-Agent When... | Use Single Agent When... |
|-------------------------|--------------------------|
| Domain has distinct specializations | Task is simple and focused |
| Need expert-level performance | General knowledge is sufficient |
| System will grow over time | Requirements are stable |
| Multiple teams own different parts | Single team owns everything |
| Need to reuse specialists | Agent is purpose-built |

---

## Part 1: Understanding Agent Hierarchies

### Agent Roles

**1. Orchestrator (Parent) Agent**
- Routes requests to appropriate specialists
- Manages overall conversation flow
- Synthesizes responses from multiple agents
- Handles general queries

**2. Specialist (Child) Agents**
- Deep expertise in specific domain
- Focused tools and knowledge
- Clear, specific instructions
- Return to orchestrator when done

### Routing Strategies

**1. Description-Based Routing**
The orchestrator uses agent descriptions to decide routing:

```yaml
# Orchestrator sees these descriptions
collaborators:
  - flight-specialist  # "Handles flight searches, bookings, and changes"
  - hotel-specialist   # "Manages hotel reservations and accommodations"
```

**2. Instruction-Based Routing**
Explicit routing logic in orchestrator instructions:

```yaml
instructions: |
  When user asks about flights:
  - Route to flight-specialist
  
  When user asks about hotels:
  - Route to hotel-specialist
  
  When user needs both:
  - Route to flight-specialist first
  - Then route to hotel-specialist
  - Synthesize both responses
```

**3. Tool-Based Routing**
Specialists have unique tools that trigger routing:

```yaml
# Orchestrator has no flight tools
# When it needs flight info, must use flight-specialist
```

---

## Part 2: Building Specialist Agents

### Step 1: Create Flight Specialist

Create `flight-specialist-agent.yaml`:

```yaml
kind: native
name: flight-specialist
title: Flight Booking Specialist
description: Expert in flight searches, bookings, changes, and cancellations. Handles all flight-related queries including availability, pricing, and itinerary modifications.

instructions: |
  You are a flight booking specialist with deep expertise in air travel.
  
  Your capabilities:
  - Search for flights based on dates, destinations, preferences
  - Provide detailed flight information (times, prices, airlines)
  - Handle booking requests
  - Process flight changes and cancellations
  - Explain baggage policies and fees
  
  Guidelines:
  - Always ask for essential details: origin, destination, dates, passengers
  - Present options clearly with prices and durations
  - Highlight best value and most convenient options
  - Explain any restrictions or fees upfront
  - Confirm all details before booking
  
  When you've completed the user's flight-related request:
  - Summarize what was accomplished
  - Ask if they need anything else flight-related
  - If they need other travel services (hotels, activities), let them know
    you'll hand back to the travel concierge
  
  Response format:
  - Be concise but complete
  - Use bullet points for options
  - Include all relevant details (times, prices, airlines)
  - End with clear next steps

tools:
  - search_flights
  - book_flight
  - modify_flight
  - cancel_flight

llm: groq/openai/gpt-oss-120b
```

**💡 Ask Bob:**
```
Bob, create a flight-specialist-agent.yaml file with focused instructions
for handling flight bookings and searches.
```

### Step 2: Create Hotel Specialist

Create `hotel-specialist-agent.yaml`:

```yaml
kind: native
name: hotel-specialist
title: Hotel Booking Specialist
description: Expert in hotel accommodations, reservations, and lodging options. Handles hotel searches, bookings, modifications, and provides recommendations based on preferences and budget.

instructions: |
  You are a hotel booking specialist with extensive knowledge of accommodations.
  
  Your capabilities:
  - Search hotels by location, dates, and preferences
  - Provide detailed hotel information (amenities, ratings, prices)
  - Handle reservation requests
  - Process booking modifications and cancellations
  - Recommend hotels based on budget and needs
  
  Guidelines:
  - Ask for: location, check-in/out dates, guests, budget, preferences
  - Present 3-5 options with key details
  - Highlight amenities that match user preferences
  - Explain cancellation policies clearly
  - Confirm all details before booking
  
  When you've completed the user's hotel-related request:
  - Summarize the booking or recommendations
  - Ask if they need anything else hotel-related
  - If they need other travel services, indicate you'll return to
    the travel concierge
  
  Response format:
  - Clear hotel names and locations
  - Price per night and total cost
  - Key amenities (WiFi, breakfast, parking, etc.)
  - Guest ratings if available
  - Cancellation policy summary

tools:
  - search_hotels
  - book_hotel
  - modify_hotel_booking
  - cancel_hotel_booking

llm: groq/openai/gpt-oss-120b
```

### Step 3: Create Activity Planner

Create `activity-planner-agent.yaml`:

```yaml
kind: native
name: activity-planner
title: Local Activity Specialist
description: Expert in local attractions, activities, tours, and experiences. Provides personalized recommendations for things to do based on interests, location, and travel dates.

instructions: |
  You are a local activity and experience specialist.
  
  Your capabilities:
  - Suggest activities based on location and interests
  - Provide details on tours, attractions, and experiences
  - Recommend restaurants and local cuisine
  - Suggest itineraries for different trip lengths
  - Provide insider tips and local knowledge
  
  Guidelines:
  - Ask about: destination, travel dates, interests, group size
  - Tailor suggestions to user preferences (adventure, culture, food, etc.)
  - Include practical details (duration, cost, booking requirements)
  - Suggest a mix of popular and off-the-beaten-path options
  - Consider timing and logistics
  
  When you've provided activity recommendations:
  - Summarize the suggested itinerary
  - Offer to provide more details on specific activities
  - If they need other travel services, indicate you'll return to
    the travel concierge
  
  Response format:
  - Activity name and brief description
  - Duration and best time to visit
  - Approximate cost
  - Why it's recommended for them
  - Booking/reservation requirements

tools:
  - search_activities
  - get_activity_details
  - search_restaurants
  - create_itinerary

llm: groq/openai/gpt-oss-120b
```

### Step 4: Create Budget Advisor

Create `budget-advisor-agent.yaml`:

```yaml
kind: native
name: budget-advisor
title: Travel Budget Specialist
description: Expert in travel cost analysis, budget planning, and money-saving strategies. Helps travelers understand costs, find deals, and optimize their travel budget.

instructions: |
  You are a travel budget and cost analysis specialist.
  
  Your capabilities:
  - Analyze total trip costs (flights, hotels, activities, meals)
  - Suggest budget-friendly alternatives
  - Identify money-saving opportunities
  - Compare costs across different options
  - Provide budget breakdowns and forecasts
  
  Guidelines:
  - Ask about: total budget, trip duration, priorities
  - Break down costs by category
  - Highlight where most money is spent
  - Suggest specific ways to save money
  - Be realistic about costs
  
  When you've completed the budget analysis:
  - Provide clear cost breakdown
  - Highlight savings opportunities
  - Recommend budget allocation
  - If they want to book based on your analysis, indicate you'll
    return to the travel concierge
  
  Response format:
  - Total estimated cost
  - Cost breakdown by category
  - Budget vs actual comparison
  - Money-saving recommendations
  - Alternative options if over budget

tools:
  - calculate_trip_cost
  - compare_options
  - find_deals
  - budget_optimizer

llm: groq/openai/gpt-oss-120b
```

---

## Part 3: Creating the Orchestrator Agent

### Step 1: Design Orchestrator Instructions

The orchestrator needs clear routing logic:

Create `travel-concierge-agent.yaml`:

```yaml
kind: native
name: travel-concierge
title: Travel Concierge
description: Your personal travel planning assistant that coordinates with specialists to help plan your perfect trip.

instructions: |
  You are a friendly travel concierge who helps users plan their trips by
  coordinating with specialized travel agents.
  
  Your role:
  - Understand the user's travel needs and preferences
  - Route requests to appropriate specialists
  - Synthesize information from multiple specialists
  - Provide a cohesive travel planning experience
  
  Available specialists:
  - flight-specialist: For all flight-related queries (searches, bookings, changes)
  - hotel-specialist: For accommodation needs (hotels, reservations)
  - activity-planner: For things to do, attractions, restaurants
  - budget-advisor: For cost analysis and budget planning
  
  Routing guidelines:
  
  1. Flight queries → flight-specialist
     - "Find me flights to Paris"
     - "Change my flight booking"
     - "What's the baggage allowance?"
  
  2. Hotel queries → hotel-specialist
     - "Find hotels in Tokyo"
     - "Book a hotel near the airport"
     - "Cancel my hotel reservation"
  
  3. Activity queries → activity-planner
     - "What should I do in Rome?"
     - "Recommend restaurants in Barcelona"
     - "Plan a 3-day itinerary"
  
  4. Budget queries → budget-advisor
     - "How much will this trip cost?"
     - "Help me save money on my trip"
     - "Compare these options"
  
  5. Complex queries → Multiple specialists
     - "Plan a week in London" → hotel + activity-planner + budget-advisor
     - "Book my entire trip" → flight + hotel + activity-planner
  
  Workflow for complex requests:
  1. Break down the request into components
  2. Route to specialists in logical order:
     - Flights first (determines dates)
     - Hotels second (based on flight dates)
     - Activities third (based on location and dates)
     - Budget last (analyzes all costs)
  3. Synthesize responses into cohesive plan
  4. Present complete solution to user
  
  General queries you handle directly:
  - Greetings and general questions
  - Travel tips and advice
  - Clarifying user needs
  - Summarizing plans
  
  Response style:
  - Friendly and helpful
  - Clear about which specialist is helping
  - Synthesize specialist responses naturally
  - Proactive in suggesting next steps
  
  Example interactions:
  
  User: "I want to visit Paris next month"
  You: "I'd love to help you plan your Paris trip! Let me connect you with
  our specialists. First, let me check with our flight specialist for
  available flights..."
  [Route to flight-specialist]
  
  User: "Plan a complete 5-day trip to Tokyo"
  You: "Exciting! Let me coordinate with our team to plan your Tokyo adventure.
  I'll work with our flight, hotel, and activity specialists to create a
  complete itinerary for you..."
  [Route to flight-specialist, then hotel-specialist, then activity-planner]

collaborators:
  - flight-specialist
  - hotel-specialist
  - activity-planner
  - budget-advisor

llm: groq/openai/gpt-oss-120b
```

**💡 Ask Bob:**
```
Bob, create a travel-concierge-agent.yaml that orchestrates between
the four specialist agents with clear routing logic.
```

---

## Part 4: Implementing Mock Tools

For this workshop, we'll create mock tools that simulate the specialist capabilities.

### Create Flight Tools

Create `flight_tools.py`:

```python
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
            "stops": 0
        },
        {
            "flight_number": "UA456",
            "airline": "United Airlines",
            "departure": f"{origin} 10:30",
            "arrival": f"{destination} 17:15",
            "duration": "6h 45m",
            "price": 425.00,
            "stops": 0
        },
        {
            "flight_number": "DL789",
            "airline": "Delta",
            "departure": f"{origin} 14:00",
            "arrival": f"{destination} 22:00",
            "duration": "8h 00m",
            "price": 380.00,
            "stops": 1
        }
    ]
    
    return {
        "origin": origin,
        "destination": destination,
        "departure_date": departure_date,
        "return_date": return_date,
        "passengers": passengers,
        "flights": flights,
        "count": len(flights)
    }


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
        "message": f"Flight {flight_number} booked successfully! Confirmation: {confirmation}"
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
    return {
        "status": "modified",
        "confirmation_number": confirmation_number,
        "changes": {
            "new_date": new_date,
            "new_flight": new_flight
        },
        "fee": 75.00,
        "message": "Flight modified successfully. Change fee: $75.00"
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
        "refund_amount": 350.00,
        "refund_method": "original payment method",
        "processing_time": "5-7 business days",
        "message": "Flight cancelled. Refund of $350.00 will be processed."
    }
```

**💡 Ask Bob:**
```
Bob, create flight_tools.py with mock implementations of search_flights,
book_flight, modify_flight, and cancel_flight tools.
```

### Create Hotel Tools

Create `hotel_tools.py`:

```python
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
            "amenities": ["WiFi", "Breakfast", "Pool", "Gym"],
            "cancellation": "Free cancellation until 24h before"
        },
        {
            "name": "City Center Inn",
            "location": location,
            "rating": 4.0,
            "price_per_night": 120.00,
            "amenities": ["WiFi", "Breakfast"],
            "cancellation": "Free cancellation until 48h before"
        },
        {
            "name": "Budget Stay",
            "location": location,
            "rating": 3.5,
            "price_per_night": 80.00,
            "amenities": ["WiFi"],
            "cancellation": "Non-refundable"
        }
    ]
    
    # Filter by max price if specified
    if max_price:
        hotels = [h for h in hotels if h["price_per_night"] <= max_price]
    
    return {
        "location": location,
        "check_in": check_in,
        "check_out": check_out,
        "guests": guests,
        "hotels": hotels,
        "count": len(hotels)
    }


@tool
def book_hotel(
    hotel_name: str,
    guest_name: str,
    guest_email: str,
    check_in: str,
    check_out: str
) -> dict:
    """
    Book a hotel room.
    
    Args:
        hotel_name: Name of the hotel
        guest_name: Guest full name
        guest_email: Guest email
        check_in: Check-in date
        check_out: Check-out date
    
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
        "message": f"Hotel booked successfully! Confirmation: {confirmation}"
    }


@tool
def modify_hotel_booking(
    confirmation_number: str,
    new_check_in: str = None,
    new_check_out: str = None
) -> dict:
    """
    Modify hotel booking dates.
    
    Args:
        confirmation_number: Booking confirmation number
        new_check_in: New check-in date (optional)
        new_check_out: New check-out date (optional)
    
    Returns:
        Modification confirmation
    """
    return {
        "status": "modified",
        "confirmation_number": confirmation_number,
        "new_check_in": new_check_in,
        "new_check_out": new_check_out,
        "message": "Hotel booking modified successfully"
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
        "message": "Hotel booking cancelled. Full refund processed."
    }
```

---

## Part 5: Testing Multi-Agent Workflows

### Import All Agents and Tools

```bash
# Import tools
orchestrate tools import flight_tools.py
orchestrate tools import hotel_tools.py

# Import specialist agents
orchestrate agent import flight-specialist-agent.yaml
orchestrate agent import hotel-specialist-agent.yaml
orchestrate agent import activity-planner-agent.yaml
orchestrate agent import budget-advisor-agent.yaml

# Import orchestrator (must be last, after collaborators exist)
orchestrate agent import travel-concierge-agent.yaml
```

### Test Simple Routing

**Test 1: Single Specialist**
```bash
orchestrate chat --agent travel-concierge \
  --message "Find me flights from New York to London for next week"
```

Expected flow:
1. Concierge receives request
2. Routes to flight-specialist
3. Flight-specialist searches flights
4. Returns results to user

**Test 2: Multiple Specialists**
```bash
orchestrate chat --agent travel-concierge \
  --message "Plan a 5-day trip to Paris including flights and hotels"
```

Expected flow:
1. Concierge receives request
2. Routes to flight-specialist for flights
3. Routes to hotel-specialist for hotels
4. Synthesizes complete plan
5. Returns to user

### Test Complex Workflows

**Test 3: Full Trip Planning**
```bash
orchestrate chat --agent travel-concierge \
  --message "I want to visit Tokyo for a week. I have a budget of $3000. 
  Help me plan everything including flights, hotel, and activities."
```

Expected flow:
1. Concierge breaks down request
2. Routes to flight-specialist
3. Routes to hotel-specialist
4. Routes to activity-planner
5. Routes to budget-advisor
6. Synthesizes complete itinerary
7. Returns comprehensive plan

---

## Part 6: Best Practices

### 1. Agent Design

**Keep Specialists Focused:**
```yaml
# ✅ Good - Focused specialist
name: flight-specialist
tools:
  - search_flights
  - book_flight
  - modify_flight
  - cancel_flight

# ❌ Bad - Too broad
name: travel-specialist
tools:
  - search_flights
  - search_hotels
  - search_activities
  - book_everything
```

**Clear Descriptions:**
```yaml
# ✅ Good - Clear, specific description
description: Expert in flight searches, bookings, changes, and cancellations. 
  Handles all flight-related queries including availability, pricing, and 
  itinerary modifications.

# ❌ Bad - Vague description
description: Helps with travel stuff
```

### 2. Routing Logic

**Explicit Routing Instructions:**
```yaml
instructions: |
  # ✅ Good - Clear routing rules
  When user asks about flights:
  - Route to flight-specialist
  - Wait for response
  - Present to user
  
  When user asks about hotels:
  - Route to hotel-specialist
  - Wait for response
  - Present to user
```

**Handle Edge Cases:**
```yaml
instructions: |
  If user request is ambiguous:
  - Ask clarifying questions first
  - Then route to appropriate specialist
  
  If specialist cannot help:
  - Acknowledge limitation
  - Suggest alternative
  - Route to different specialist if appropriate
```

### 3. Context Management

**Pass Relevant Context:**
```yaml
instructions: |
  When routing to specialist:
  - Include all relevant details from conversation
  - Mention previous specialist interactions if relevant
  - Provide user preferences and constraints
```

**Synthesize Responses:**
```yaml
instructions: |
  After receiving specialist response:
  - Summarize key points
  - Connect to user's original request
  - Suggest logical next steps
  - Maintain conversation flow
```

### 4. Error Handling

**Graceful Failures:**
```yaml
instructions: |
  If specialist returns error:
  - Explain issue to user clearly
  - Suggest alternatives
  - Offer to try different approach
  - Don't expose technical details
```

### 5. Performance Optimization

**Minimize Hops:**
```yaml
# ✅ Good - Direct routing
User → Orchestrator → Specialist → User

# ❌ Bad - Unnecessary hops
User → Orchestrator → Coordinator → Specialist → Coordinator → Orchestrator → User
```

**Parallel Processing (Future):**
```yaml
# When specialists don't depend on each other
# Route to multiple specialists simultaneously
# Synthesize all responses together
```

---

## Part 7: Advanced Patterns

### Pattern 1: Sequential Workflow

```yaml
instructions: |
  For trip planning:
  1. Get flights first (determines dates)
  2. Get hotels second (based on flight dates)
  3. Get activities third (based on location and dates)
  4. Get budget analysis last (based on all selections)
```

### Pattern 2: Conditional Routing

```yaml
instructions: |
  If user mentions budget constraints:
  - Route to budget-advisor FIRST
  - Get budget recommendations
  - Then route to other specialists with budget in mind
  
  If user has no budget constraints:
  - Route directly to relevant specialists
  - Offer budget analysis at the end
```

### Pattern 3: Iterative Refinement

```yaml
instructions: |
  For complex requests:
  1. Get initial options from specialist
  2. Present to user
  3. If user wants refinements:
     - Route back to same specialist with new criteria
     - Repeat until user satisfied
  4. Move to next specialist
```

### Pattern 4: Fallback Chain

```yaml
instructions: |
  If primary specialist cannot help:
  1. Try secondary specialist
  2. If still cannot help, try general knowledge
  3. If still cannot help, escalate or admit limitation
```

---

## Exercises

### Exercise 1: Add a New Specialist (Easy)

Add a "Car Rental Specialist" to the travel system.

**Requirements:**
- Create car-rental-specialist-agent.yaml
- Create car_rental_tools.py with search and book functions
- Update travel-concierge to include new specialist
- Test routing to car rental specialist

**💡 Ask Bob:**
```
Bob, create a car-rental-specialist agent with tools for searching
and booking rental cars, and update the travel-concierge to route
car rental queries appropriately.
```

### Exercise 2: Implement Budget-First Workflow (Medium)

Modify the orchestrator to always check budget first for trip planning requests.

**Requirements:**
- Update travel-concierge instructions
- Route to budget-advisor before other specialists
- Use budget constraints when routing to other specialists
- Test with budget-constrained requests

### Exercise 3: Create a Different Domain (Advanced)

Build a multi-agent system for a different domain (e.g., e-commerce, healthcare, education).

**Requirements:**
- Design 3-4 specialist agents
- Create orchestrator with routing logic
- Implement mock tools
- Test complete workflows

**Example Domains:**
- **E-commerce**: Product Search, Inventory, Checkout, Support
- **Healthcare**: Appointment, Prescription, Billing, Records
- **Education**: Course Search, Enrollment, Assignments, Grading

---

## Common Issues

### Issue: Orchestrator Not Routing

**Symptoms**: Orchestrator tries to answer directly instead of routing

**Solutions:**
1. Make specialist descriptions more specific
2. Add explicit routing rules in orchestrator instructions
3. Ensure collaborators are properly listed
4. Check that specialist agents exist and are imported

### Issue: Context Lost Between Agents

**Symptoms**: Specialist doesn't have information from previous conversation

**Solutions:**
1. Update orchestrator to pass context explicitly
2. Include relevant details when routing
3. Have orchestrator summarize previous interactions

### Issue: Circular Routing

**Symptoms**: Agents keep routing back and forth

**Solutions:**
1. Add clear termination conditions
2. Limit routing depth
3. Have specialists indicate when they're done
4. Orchestrator should synthesize, not re-route

---

## Summary

In this lesson, you learned:

✅ When and why to use multi-agent systems  
✅ How to design focused specialist agents  
✅ How to create orchestrator agents with routing logic  
✅ How to manage context and handoffs  
✅ Best practices for multi-agent architectures  
✅ Common patterns and anti-patterns  

### Key Takeaways

1. **Separation of Concerns** - Each agent has a clear, focused purpose
2. **Clear Routing** - Orchestrator has explicit logic for routing decisions
3. **Context Management** - Information flows smoothly between agents
4. **Graceful Degradation** - System handles errors and edge cases well
5. **Maintainability** - Specialists can be updated independently

### Next Steps

- Implement the exercises to reinforce learning
- Try building multi-agent systems for your own use cases
- Explore advanced patterns like parallel processing
- Consider how to monitor and optimize multi-agent systems

---

**Ready for deployment?** Head to [Part 5: Testing & Deployment](../part5-deployment/README.md) to learn how to test and deploy your multi-agent systems! 🚀