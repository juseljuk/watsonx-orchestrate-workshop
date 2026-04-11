"""
Product Catalog MCP Server

Provides tools for product search, details, inventory, and recommendations.

Tools:
- search_products: Search for products by keyword
- get_product_details: Get detailed product information
- check_inventory: Check product availability
- get_recommendations: Get product recommendations

Environment Variables:
- API_KEY: Backend API key (optional)
- API_URL: Backend API URL (optional)
"""

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import json

# Mock product database
PRODUCTS = {
    "LAPTOP-001": {
        "id": "LAPTOP-001",
        "name": "ProBook 15",
        "category": "Laptops",
        "price": 899.99,
        "stock": 15,
        "description": "15-inch professional laptop with 16GB RAM",
        "specs": {"ram": "16GB", "storage": "512GB SSD", "screen": "15.6 inch"}
    },
    "PHONE-001": {
        "id": "PHONE-001",
        "name": "SmartPhone X",
        "category": "Phones",
        "price": 699.99,
        "stock": 25,
        "description": "Latest smartphone with 5G connectivity",
        "specs": {"storage": "128GB", "camera": "48MP", "battery": "4500mAh"}
    },
    "TABLET-001": {
        "id": "TABLET-001",
        "name": "TabPro 10",
        "category": "Tablets",
        "price": 449.99,
        "stock": 8,
        "description": "10-inch tablet perfect for work and play",
        "specs": {"storage": "64GB", "screen": "10.1 inch", "battery": "8000mAh"}
    },
    "HEADPHONES-001": {
        "id": "HEADPHONES-001",
        "name": "SoundMax Pro",
        "category": "Audio",
        "price": 199.99,
        "stock": 30,
        "description": "Premium noise-cancelling headphones",
        "specs": {"battery": "30 hours", "noise_cancelling": True, "wireless": True}
    },
    "MONITOR-001": {
        "id": "MONITOR-001",
        "name": "UltraView 27",
        "category": "Monitors",
        "price": 349.99,
        "stock": 12,
        "description": "27-inch 4K monitor with HDR support",
        "specs": {"resolution": "3840x2160", "refresh_rate": "60Hz", "hdr": True}
    }
}

# Create MCP server
app = Server("product-catalog")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List all available tools in this MCP server."""
    return [
        Tool(
            name="search_products",
            description="Search for products by name, category, or keyword",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query (product name, category, or keyword)"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of results to return",
                        "default": 10
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="get_product_details",
            description="Get detailed information about a specific product",
            inputSchema={
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "string",
                        "description": "The unique product ID"
                    }
                },
                "required": ["product_id"]
            }
        ),
        Tool(
            name="check_inventory",
            description="Check if a product is in stock and get quantity",
            inputSchema={
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "string",
                        "description": "The unique product ID"
                    }
                },
                "required": ["product_id"]
            }
        ),
        Tool(
            name="get_recommendations",
            description="Get product recommendations based on a category or product",
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Product category (e.g., Laptops, Phones, Tablets, Audio, Monitors)"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of recommendations",
                        "default": 3
                    }
                },
                "required": ["category"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls and return results."""
    
    try:
        if name == "search_products":
            query = arguments["query"].lower()
            max_results = arguments.get("max_results", 10)
            
            # Search products
            results = []
            for product in PRODUCTS.values():
                if (query in product["name"].lower() or 
                    query in product["category"].lower() or
                    query in product["description"].lower()):
                    results.append({
                        "id": product["id"],
                        "name": product["name"],
                        "category": product["category"],
                        "price": product["price"],
                        "in_stock": product["stock"] > 0
                    })
            
            results = results[:max_results]
            return [TextContent(
                type="text",
                text=json.dumps({"results": results, "count": len(results)}, indent=2)
            )]
        
        elif name == "get_product_details":
            product_id = arguments["product_id"]
            
            if product_id not in PRODUCTS:
                return [TextContent(
                    type="text",
                    text=json.dumps({"error": f"Product {product_id} not found"})
                )]
            
            product = PRODUCTS[product_id]
            return [TextContent(
                type="text",
                text=json.dumps(product, indent=2)
            )]
        
        elif name == "check_inventory":
            product_id = arguments["product_id"]
            
            if product_id not in PRODUCTS:
                return [TextContent(
                    type="text",
                    text=json.dumps({"error": f"Product {product_id} not found"})
                )]
            
            product = PRODUCTS[product_id]
            inventory = {
                "product_id": product_id,
                "product_name": product["name"],
                "in_stock": product["stock"] > 0,
                "quantity": product["stock"],
                "status": "Available" if product["stock"] > 5 else "Low Stock" if product["stock"] > 0 else "Out of Stock"
            }
            return [TextContent(
                type="text",
                text=json.dumps(inventory, indent=2)
            )]
        
        elif name == "get_recommendations":
            category = arguments["category"]
            max_results = arguments.get("max_results", 3)
            
            # Get products in category
            recommendations = [
                {
                    "id": p["id"],
                    "name": p["name"],
                    "price": p["price"],
                    "description": p["description"]
                }
                for p in PRODUCTS.values()
                if p["category"].lower() == category.lower()
            ][:max_results]
            
            return [TextContent(
                type="text",
                text=json.dumps({"recommendations": recommendations, "count": len(recommendations)}, indent=2)
            )]
        
        else:
            return [TextContent(
                type="text",
                text=json.dumps({"error": f"Unknown tool: {name}"})
            )]
    
    except Exception as e:
        return [TextContent(
            type="text",
            text=json.dumps({"error": f"Server error: {str(e)}"})
        )]


# Run the server
if __name__ == "__main__":
    import asyncio
    import asyncio
    asyncio.run(stdio_server(app))

# Made with Bob
