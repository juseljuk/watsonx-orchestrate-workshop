# Part 3 Exercises: Practice Building Tools

<p align="center">
  <img src="bobchestrate_part3_exercises.png" alt="Bobchestrate - Setup" width="700">
</p>

Complete these exercises to master custom tool creation.

## Exercise 1: Calculator Tool (Easy)

**Goal:** Create a tool that performs mathematical calculations

**Task:** Create a calculator tool that can add, subtract, multiply, and divide two numbers.

**Requirements:**<br>
- Function name: `calculate`<br>
- Parameters: `operation` (string: "add", "subtract", "multiply", "divide"), `num1` (float), `num2` (float)<br>
- Should handle division by zero<br>
- Should validate the operation parameter

**Ask Bob for help:**
```
Bob, create a calculator tool for watsonx Orchestrate that can add, subtract, multiply, and divide two numbers
```

**Test cases:**<br>
- Calculate 10 + 5 = 15<br>
- Calculate 20 - 8 = 12<br>
- Calculate 6 * 7 = 42<br>
- Calculate 100 / 4 = 25<br>
- Calculate 10 / 0 = Error

**Success criteria:**<br>
- All operations work correctly<br>
- Division by zero is handled gracefully<br>
- Invalid operations return helpful errors

---

## Exercise 2: Email Validator Tool (Easy)

**Goal:** Create a tool that validates email addresses

**Task:** Build a tool that checks if an email address is valid.

**Requirements:**<br>
- Function name: `validate_email`<br>
- Parameter: `email` (string)<br>
- Should check for @ symbol, domain, and basic format<br>
- Return validation result with explanation

**Ask Bob for help:**
```
Bob, create an email validator tool that checks if an email address is properly formatted
```

**Test cases:**<br>
- user@example.com → Valid<br>
- invalid.email → Invalid (no @)<br>
- user@domain → Invalid (no TLD)<br>
- @example.com → Invalid (no username)

**Success criteria:**<br>
- Correctly identifies valid emails<br>
- Provides clear error messages for invalid emails<br>
- Handles edge cases

---

## Exercise 3: Temperature Converter Tool (Medium)

**Goal:** Create a tool that converts between temperature units

**Task:** Build a tool that converts temperatures between Celsius, Fahrenheit, and Kelvin.

**Requirements:**<br>
- Function name: `convert_temperature`<br>
- Parameters: `value` (float), `from_unit` (string), `to_unit` (string)<br>
- Support: Celsius, Fahrenheit, Kelvin<br>
- Validate that Kelvin values aren't below absolute zero

**Ask Bob for help:**
```
Bob, create a temperature converter tool that converts between Celsius, Fahrenheit, and Kelvin
```

**Test cases:**<br>
- 0°C to Fahrenheit = 32°F<br>
- 100°C to Kelvin = 373.15K<br>
- 32°F to Celsius = 0°C<br>
- -300K = Error (below absolute zero)

**Success criteria:**<br>
- All conversions are accurate<br>
- Validates input ranges<br>
- Handles all unit combinations

---

## Exercise 4: Data Formatter Tool (Medium)

**Goal:** Create a tool that formats data in different ways

**Task:** Build a tool that takes structured data and formats it as JSON, CSV, or a markdown table.

**Requirements:**<br>
- Function name: `format_data`<br>
- Parameters: `data` (list of dicts), `format` (string: "json", "csv", "table")<br>
- Should handle empty data<br>
- Should create proper formatting for each type

**Ask Bob for help:**
```
Bob, create a data formatter tool that can output data as JSON, CSV, or markdown table
```

**Test data:**
```python
[
    {"name": "Alice", "age": 30, "city": "NYC"},
    {"name": "Bob", "age": 25, "city": "LA"}
]
```

**Success criteria:**<br>
- JSON output is valid JSON<br>
- CSV output has proper headers and rows<br>
- Table output is properly formatted markdown<br>
- Handles empty data gracefully

---

## Exercise 5: Text Analyzer Tool (Advanced)

**Goal:** Create a tool that analyzes text and provides statistics

**Task:** Build a tool that analyzes text and returns word count, character count, sentence count, and reading time.

**Requirements:**<br>
- Function name: `analyze_text`<br>
- Parameter: `text` (string)<br>
- Calculate: word count, character count, sentence count, average word length, estimated reading time<br>
- Reading time: assume 200 words per minute

**Ask Bob for help:**
```
Bob, create a text analyzer tool that provides statistics about a piece of text including word count, character count, and reading time
```

**Test text:**
```
"The quick brown fox jumps over the lazy dog. This is a test sentence."
```

**Expected output:**
- Words: 15<br>
- Characters: 68<br>
- Sentences: 2<br>
- Avg word length: ~4.5<br>
- Reading time: ~5 seconds

**Success criteria:**<br>
- All counts are accurate<br>
- Reading time calculation is reasonable<br>
- Handles empty text<br>
- Handles text with no punctuation

---

## Exercise 6: Product Search Tool (Advanced)

**Goal:** Create a tool that searches a product catalog

**Task:** Build a tool that searches for products by name, category, or price range.

**Requirements:**<br>
- Function name: `search_products`<br>
- Parameters: `query` (string, optional), `category` (string, optional), `min_price` (float, optional), `max_price` (float, optional)<br>
- Use a mock product database (list of dicts)<br>
- Support partial name matching<br>
- Return sorted results

**Ask Bob for help:**
```
Bob, create a product search tool with a mock database that can search by name, category, and price range
```

**Mock database:**
```python
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999.99},
    {"id": 2, "name": "Mouse", "category": "Electronics", "price": 29.99},
    {"id": 3, "name": "Desk", "category": "Furniture", "price": 299.99},
    {"id": 4, "name": "Chair", "category": "Furniture", "price": 199.99},
]
```

**Test cases:**<br>
- Search "Laptop" → Find laptop<br>
- Category "Electronics" → Find laptop and mouse<br>
- Price range $100-$500 → Find desk and chair<br>
- Combined filters → Multiple criteria

**Success criteria:**<br>
- All search filters work<br>
- Partial matching works<br>
- Results are sorted by relevance<br>
- Returns empty list when no matches

---

## Exercise 7: Appointment Scheduler Tool (Advanced)

**Goal:** Create a tool that checks appointment availability

**Task:** Build a tool that checks if a time slot is available and books appointments.

**Requirements:**<br>
- Function name: `schedule_appointment`<br>
- Parameters: `date` (string), `time` (string), `duration_minutes` (int), `customer_name` (string)<br>
- Maintain a simple in-memory schedule<br>
- Check for conflicts<br>
- Business hours: 9 AM - 5 PM, Monday-Friday

**Ask Bob for help:**
```
Bob, create an appointment scheduler tool that checks availability and books time slots
```

**Test cases:**<br>
- Book 2024-03-20 at 10:00 AM for 30 minutes → Success<br>
- Book same time again → Conflict error<br>
- Book at 8:00 AM → Outside business hours<br>
- Book on Saturday → Weekend error

**Success criteria:**<br>
- Detects scheduling conflicts<br>
- Validates business hours<br>
- Validates date/time format<br>
- Stores appointments correctly

---

## Bonus Challenge: Multi-Tool Agent

**Goal:** Create an agent that uses multiple tools together

**Task:** Create a "Personal Assistant" agent that uses at least 3 of your custom tools.

**Requirements:**<br>
- Agent should intelligently choose which tool to use<br>
- Agent should chain tools when needed<br>
- Agent should handle tool errors gracefully<br>

**Example workflow:**
```
User: "Calculate 15% tip on $85.50 and format the result as a table"
Agent: 
1. Uses calculator tool: 85.50 * 0.15 = 12.83
2. Uses formatter tool to create table with original amount, tip, and total
```

**Ask Bob for help:**
```
Bob, create an agent that uses my calculator, formatter, and text analyzer tools together
```

**Success criteria:**<br>
- Agent uses multiple tools appropriately<br>
- Agent chains tools when logical<br>
- Agent provides coherent responses<br>
- Agent handles tool failures

---

## Debugging Exercise

**Goal:** Fix broken tools

**Task:** This tool has several bugs. Find and fix them!

```python
from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool
def broken_calculator(num1, num2, operation):
    """Performs calculations"""
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
```

**Problems to find:**<br>
1. Missing type hints<br>
2. No input validation<br>
3. Division by zero not handled<br>
4. No return type documentation<br>
5. Vague docstring<br>
6. No error handling<br>
7. Doesn't return structured response

**Ask Bob for help:**
```
Bob, review this calculator tool and identify all the problems: [paste code]
```

---

## Reflection Questions

After completing the exercises:

1. **What makes a good tool?**
   - Clear, specific purpose
   - Comprehensive input validation
   - Structured, consistent output
   - Good error handling
   - Helpful documentation

2. **How do you test tools effectively?**
   - Test happy path
   - Test edge cases
   - Test error conditions
   - Test with real agent

3. **When should you create a new tool vs. modifying existing ones?**
   - New functionality → new tool
   - Bug fix/improvement → modify existing
   - Keep tools focused and single-purpose

4. **How can Bob help you build better tools?**
   - Generate initial code
   - Review for issues
   - Suggest improvements
   - Write test cases

---

## Next Steps

Once you've mastered custom tools, you're ready to add knowledge bases and create agent collaborators!

Continue to [Part 3b: AI Gateway and external model providers](../part3b-ai-gateway-models/README.md) →