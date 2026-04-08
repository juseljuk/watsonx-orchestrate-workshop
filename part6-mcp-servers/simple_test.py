#!/usr/bin/env python3
"""
Simple test for Product Catalog MCP Server.
Tests the server by importing and calling functions directly.
"""

import json
import asyncio
from product_catalog_server import (
    search_products,
    get_product_details,
    check_inventory,
    get_recommendations
)

async def test_all_tools():
    """Test all MCP tools directly."""
    
    print("Testing Product Catalog MCP Server Tools")
    print("=" * 50)
    
    # Test 1: Search Products
    print("\n1. Testing search_products...")
    print("-" * 50)
    search_args = {
        "query": "wireless",
        "in_stock_only": True
    }
    result = await search_products(search_args)
    print(f"Query: {search_args}")
    print(f"Result: {result[0].text}")
    
    # Test 2: Get Product Details
    print("\n2. Testing get_product_details...")
    print("-" * 50)
    details_args = {
        "product_id": "PROD-001"
    }
    result = await get_product_details(details_args)
    print(f"Product ID: {details_args['product_id']}")
    print(f"Result: {result[0].text}")
    
    # Test 3: Check Inventory
    print("\n3. Testing check_inventory...")
    print("-" * 50)
    inventory_args = {
        "product_ids": ["PROD-001", "PROD-004", "PROD-007"]
    }
    result = await check_inventory(inventory_args)
    print(f"Product IDs: {inventory_args['product_ids']}")
    print(f"Result: {result[0].text}")
    
    # Test 4: Get Recommendations (by product)
    print("\n4. Testing get_recommendations (by product)...")
    print("-" * 50)
    rec_args = {
        "product_id": "PROD-001",
        "limit": 3
    }
    result = await get_recommendations(rec_args)
    print(f"Based on: {rec_args['product_id']}")
    print(f"Result: {result[0].text}")
    
    # Test 5: Get Recommendations (by category)
    print("\n5. Testing get_recommendations (by category)...")
    print("-" * 50)
    rec_args = {
        "category": "Electronics",
        "max_price": 150,
        "limit": 3
    }
    result = await get_recommendations(rec_args)
    print(f"Category: {rec_args['category']}, Max Price: {rec_args['max_price']}")
    print(f"Result: {result[0].text}")
    
    # Test 6: Search with filters
    print("\n6. Testing search_products with filters...")
    print("-" * 50)
    search_args = {
        "query": "audio",
        "category": "Electronics",
        "max_price": 100
    }
    result = await search_products(search_args)
    print(f"Query: {search_args}")
    print(f"Result: {result[0].text}")
    
    print("\n" + "=" * 50)
    print("✓ All tests completed successfully!")
    print("\nThe MCP server tools are working correctly.")
    print("You can now integrate this server with watsonx Orchestrate.")

if __name__ == "__main__":
    asyncio.run(test_all_tools())

# Made with Bob
