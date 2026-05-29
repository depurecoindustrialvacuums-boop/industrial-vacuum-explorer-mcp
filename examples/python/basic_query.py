"""
Depureco MCP — Basic Python Example

A minimal example showing how to call the Depureco MCP REST API
from Python. No dependencies beyond the standard library and requests.

Endpoint: https://depureco.com/wp-json/depureco/v1/mcp

Run with:
    pip install requests
    python basic_query.py
"""

import requests
import json

BASE_URL = "https://depureco.com/wp-json/depureco/v1/mcp"


def call_mcp(tool: str, params: dict = None, product_id: str = None) -> dict:
    """
    Call any tool on the Depureco MCP server.

    Args:
        tool: Tool name (e.g., 'configureProduct', 'getProductData')
        params: Optional parameters dictionary for the tool
        product_id: Optional product ID (for getProductData, getTechnicalSpecs, getProductAccessories)

    Returns:
        JSON response as a Python dictionary
    """
    payload = {"tool": tool}
    if params:
        payload["params"] = params
    if product_id:
        payload["productId"] = product_id

    response = requests.post(BASE_URL, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def main():
    print("=== Depureco MCP — Basic Query Examples ===\n")

    # 1. Get all available filter options
    print("1. Getting all filter options...")
    filters = call_mcp("getFilterOptions")
    print(f"   Found {len(filters.get('applications', []))} applications")
    print(f"   Found {len(filters.get('sectors', []))} sectors")
    print(f"   Found {len(filters.get('certificates', []))} certifications\n")

    # 2. Configure a product search
    print("2. Searching for ATEX Zone 22 vacuums for combustible dust...")
    results = call_mcp(
        "configureProduct",
        params={
            "application": "combustible-dust",
            "zoneType": "zone-22",
            "certificate": "atex",
            "limit": 5,
        },
    )
    print(f"   Found {results.get('total', 0)} matching products:")
    for product in results.get("products", []):
        print(f"   - {product.get('title')}: {product.get('urls', {}).get('en', '')}")
    print()

    # 3. Get complete product sheet
    print("3. Getting complete data for PUMA ACD...")
    product_data = call_mcp("getProductData", product_id="PUMA ACD")
    if "product_id" in product_data:
        print(f"   Product: {product_data.get('title')}")
        print(f"   Description: {product_data.get('description', '')[:100]}...")
        print(f"   Highlights: {len(product_data.get('highlights', []))} sections")
        print(f"   Accessories: {len(product_data.get('accessories', []))} items\n")

    # 4. Get technical specs
    print("4. Getting technical specs for PUMA DEX 1/3D...")
    specs = call_mcp("getTechnicalSpecs", product_id="PUMA DEX 1/3D")
    tech = specs.get("technicalSpecs", {})
    print(f"   Power: {tech.get('motorPowerKwHp', 'N/A')}")
    print(f"   Airflow: {tech.get('airflowM3h', 'N/A')} m3/h")
    print(f"   Vacuum: {tech.get('continuousVacuumMbar', 'N/A')} mbar")
    print(f"   Filter area: {tech.get('primaryFilterAreaCm2', 'N/A')} cm2")
    print(f"   ATEX marking: {tech.get('atexMarking', 'N/A')}\n")

    # 5. Get accessories
    print("5. Getting accessories for ECOBULL ACD...")
    accessories = call_mcp("getProductAccessories", product_id="ECOBULL ACD")
    for acc in accessories.get("products", [])[:5]:
        print(f"   - {acc.get('code')}: {acc.get('name')}")


if __name__ == "__main__":
    main()
