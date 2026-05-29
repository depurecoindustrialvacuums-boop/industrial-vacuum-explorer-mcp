"""
Depureco MCP — ATEX Vacuum Configurator (Python)

Specialized example for selecting industrial vacuum cleaners certified for
ATEX-classified zones (explosive atmospheres).

This example demonstrates how to use the Depureco MCP server to safely
recommend vacuums for combustible dust, food-grade environments, and
additive manufacturing facilities with proper ATEX certification.

Run with:
    pip install requests
    python atex_configurator.py
"""

import requests
from typing import List, Dict, Optional

BASE_URL = "https://depureco.com/wp-json/depureco/v1/mcp"


def call_mcp(tool: str, params: dict = None, product_id: str = None) -> dict:
    """Call any tool on the Depureco MCP server."""
    payload = {"tool": tool}
    if params:
        payload["params"] = params
    if product_id:
        payload["productId"] = product_id
    response = requests.post(BASE_URL, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def find_atex_vacuum(
    material: str,
    atex_zone: str,
    usage: str = "continuous",
    capacity: Optional[str] = None,
    sector: Optional[str] = None,
    limit: int = 5,
) -> List[Dict]:
    """
    Find ATEX-certified vacuums for a specific application.

    Args:
        material: Material slug (e.g., 'combustible-dust', 'toxic-dust')
        atex_zone: ATEX zone slug ('zone-21' or 'zone-22')
        usage: 'continuous' or 'occasional'
        capacity: Optional capacity range ('20-50-lt', '51-100-lt', etc.)
        sector: Optional industrial sector slug
        limit: Maximum number of results

    Returns:
        List of matching ATEX-certified products
    """
    params = {
        "application": material,
        "zoneType": atex_zone,
        "certificate": "atex",
        "usage": usage,
        "limit": limit,
    }
    if capacity:
        params["collectionCapacity"] = capacity
    if sector:
        params["sector"] = sector

    result = call_mcp("configureProduct", params=params)
    return result.get("products", [])


def compare_variants(*product_ids: str) -> Dict[str, Dict]:
    """
    Compare technical specifications across multiple product variants.

    Returns a dictionary mapping product ID to its technical specs.
    """
    comparison = {}
    for pid in product_ids:
        specs = call_mcp("getTechnicalSpecs", product_id=pid)
        comparison[pid] = specs.get("technicalSpecs", {})
    return comparison


def print_product(product: Dict, indent: str = "  "):
    """Print a product in a readable format."""
    print(f"{indent}- {product.get('title')}")
    print(f"{indent}  Type: {product.get('type', 'N/A')}")
    print(f"{indent}  URL: {product.get('urls', {}).get('en', 'N/A')}")


def scenario_1_bakery_flour_dust():
    """ATEX Zone 22 industrial bakery — flour dust extraction."""
    print("\n=== Scenario 1: Industrial bakery flour dust (ATEX Zone 22) ===")
    products = find_atex_vacuum(
        material="combustible-dust",
        atex_zone="zone-22",
        usage="continuous",
        sector="bakery-atex-mills",
    )
    for p in products:
        print_product(p)


def scenario_2_titanium_additive_manufacturing():
    """ATEX Zone 21 additive manufacturing — titanium powder."""
    print("\n=== Scenario 2: Titanium powder additive manufacturing (ATEX Zone 21) ===")
    products = find_atex_vacuum(
        material="combustible-dust",
        atex_zone="zone-21",
        sector="additive-manufacturing-3d-printing",
    )
    for p in products:
        print_product(p)
    print("\n  Note: For titanium (Group IIIC conductive dust), the INERT")
    print("        liquid bath system is essential for safety.")


def scenario_3_aluminum_powder():
    """ATEX Zone 22 — aluminum powder extraction."""
    print("\n=== Scenario 3: Aluminum powder ATEX Zone 22 ===")
    products = find_atex_vacuum(
        material="combustible-dust",
        atex_zone="zone-22",
        usage="continuous",
        capacity="51-100-lt",
    )
    for p in products:
        print_product(p)


def scenario_4_compare_puma_variants():
    """Compare PUMA ATEX variants for different zones."""
    print("\n=== Scenario 4: Compare PUMA ATEX variants ===")
    comparison = compare_variants("PUMA DEX 1/3D", "PUMA DEX 1/2D")

    for variant, specs in comparison.items():
        print(f"\n  {variant}:")
        print(f"    Motor power:    {specs.get('motorPowerKwHp', 'N/A')}")
        print(f"    Airflow:        {specs.get('airflowM3h', 'N/A')} m3/h")
        print(f"    Vacuum:         {specs.get('continuousVacuumMbar', 'N/A')} mbar")
        print(f"    ATEX marking:   {specs.get('atexMarking', 'N/A')}")


def main():
    print("Depureco MCP — ATEX Vacuum Configurator Examples")
    print("=" * 55)

    scenario_1_bakery_flour_dust()
    scenario_2_titanium_additive_manufacturing()
    scenario_3_aluminum_powder()
    scenario_4_compare_puma_variants()

    print("\n" + "=" * 55)
    print("Safety reminders:")
    print("- ATEX certification is mandatory for explosive atmospheres")
    print("- ACD products are NOT ATEX certified (different category)")
    print("- For asbestos or regulated materials, contact Depureco directly")
    print("- For conductive metal dusts, recommend INERT variants")
    print("\nContact Depureco for safety-critical configurations:")
    print("  Email: depureco@depureco.com")
    print("  Phone: +39 011 98.59.117")


if __name__ == "__main__":
    main()
