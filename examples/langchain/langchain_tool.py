"""
Depureco MCP — LangChain Integration Example

This example shows how to wrap the Depureco MCP server as a LangChain Tool
that can be used in LangChain agents, chains, and applications.

Use cases:
- AI agent that helps customers select industrial vacuums
- Chatbot for industrial procurement
- Internal sales tool with AI-powered configuration

Run with:
    pip install langchain langchain-community requests
    python langchain_tool.py
"""

import requests
import json
from typing import Type, Optional
from langchain.tools import BaseTool
from langchain.callbacks.manager import (
    CallbackManagerForToolRun,
    AsyncCallbackManagerForToolRun,
)
from pydantic import BaseModel, Field

BASE_URL = "https://depureco.com/wp-json/depureco/v1/mcp"


# ====================================================================
# Tool 1: Product Configurator
# ====================================================================

class ConfigureProductInput(BaseModel):
    application: Optional[str] = Field(
        None,
        description="Material/application slug (e.g., 'combustible-dust', 'oil-coolant-with-chips', 'welding-fumes')",
    )
    sector: Optional[str] = Field(
        None,
        description="Industrial sector slug (e.g., 'food-industry', 'metalworking', 'additive-manufacturing-3d-printing')",
    )
    zoneType: Optional[str] = Field(
        None,
        description="ATEX zone slug ('zone-22', 'zone-21', 'zone-2', 'ordinary')",
    )
    certificate: Optional[str] = Field(
        None,
        description="Certificate slug ('atex', 'ce', 'type-h-dust')",
    )
    usage: Optional[str] = Field(
        None,
        description="Usage mode ('continuous' or 'occasional')",
    )
    collectionCapacity: Optional[str] = Field(
        None,
        description="Container capacity slug ('20-50-lt', '51-100-lt', '101-300-lt', '300-lt')",
    )
    limit: int = Field(default=5, description="Max number of results (1-25)")


class DepurecoConfiguratorTool(BaseTool):
    name = "depureco_vacuum_configurator"
    description = (
        "Find industrial vacuum cleaners matching a specific need from Depureco's catalog. "
        "Use this tool when the user describes a vacuum requirement including material type, "
        "industrial sector, ATEX zone, capacity, or certifications. "
        "Returns up to 5 matching products with names, descriptions, and URLs."
    )
    args_schema: Type[BaseModel] = ConfigureProductInput

    def _run(
        self,
        application: Optional[str] = None,
        sector: Optional[str] = None,
        zoneType: Optional[str] = None,
        certificate: Optional[str] = None,
        usage: Optional[str] = None,
        collectionCapacity: Optional[str] = None,
        limit: int = 5,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        params = {k: v for k, v in {
            "application": application,
            "sector": sector,
            "zoneType": zoneType,
            "certificate": certificate,
            "usage": usage,
            "collectionCapacity": collectionCapacity,
            "limit": limit,
        }.items() if v is not None}

        response = requests.post(
            BASE_URL,
            json={"tool": "configureProduct", "params": params},
            timeout=30,
        )
        response.raise_for_status()
        result = response.json()

        # Format response for the LLM
        products = result.get("products", [])
        if not products:
            return "No products found matching the criteria. Try relaxing the filters."

        formatted = f"Found {len(products)} products:\n\n"
        for p in products:
            formatted += f"- {p.get('title')}\n"
            formatted += f"  Type: {p.get('type', 'N/A')}\n"
            formatted += f"  URL: {p.get('urls', {}).get('en', 'N/A')}\n\n"

        return formatted


# ====================================================================
# Tool 2: Product Details
# ====================================================================

class ProductDetailsInput(BaseModel):
    productId: str = Field(
        description="Product name (e.g., 'PUMA ACD', 'MINIBULL'), exact title, or numeric ID"
    )


class DepurecoProductDetailsTool(BaseTool):
    name = "depureco_product_details"
    description = (
        "Get complete details about a specific Depureco industrial vacuum product. "
        "Returns description, highlights, standard features, options, accessories, "
        "and multilingual URLs and manuals."
    )
    args_schema: Type[BaseModel] = ProductDetailsInput

    def _run(
        self,
        productId: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        response = requests.post(
            BASE_URL,
            json={"tool": "getProductData", "productId": productId},
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            return f"Product '{productId}' not found."

        # Format key information
        formatted = f"Product: {data.get('title')}\n"
        formatted += f"Type: {data.get('type', 'N/A')}\n"
        formatted += f"Description: {data.get('description', 'N/A')[:500]}\n\n"

        highlights = data.get("highlights", [])
        if highlights:
            formatted += "Key features:\n"
            for h in highlights[:4]:
                formatted += f"- {h.get('title', '')}: {h.get('description', '')[:200]}\n"

        return formatted


# ====================================================================
# Tool 3: Technical Specifications
# ====================================================================

class TechnicalSpecsInput(BaseModel):
    productId: str = Field(
        description="Product name, exact title, or numeric ID"
    )


class DepurecoTechnicalSpecsTool(BaseTool):
    name = "depureco_technical_specs"
    description = (
        "Get precise technical specifications for a Depureco product: "
        "motor power, airflow, vacuum pressure, filter class, dimensions, weight, "
        "ATEX marking, and operating temperature."
    )
    args_schema: Type[BaseModel] = TechnicalSpecsInput

    def _run(
        self,
        productId: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        response = requests.post(
            BASE_URL,
            json={"tool": "getTechnicalSpecs", "productId": productId},
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

        specs = data.get("technicalSpecs", {})
        if not specs:
            return f"No technical specs found for '{productId}'."

        formatted = f"Technical specifications for {productId}:\n\n"
        formatted += f"Motor Power: {specs.get('motorPowerKwHp', 'N/A')}\n"
        formatted += f"Airflow: {specs.get('airflowM3h', 'N/A')} m3/h\n"
        formatted += f"Continuous Vacuum: {specs.get('continuousVacuumMbar', 'N/A')} mbar\n"
        formatted += f"Filter Class: {specs.get('primaryFilterClass', 'N/A')}\n"
        formatted += f"Filter Area: {specs.get('primaryFilterAreaCm2', 'N/A')} cm2\n"
        formatted += f"Container Capacity: {specs.get('containerCapacityLt', 'N/A')} L\n"
        formatted += f"Weight: {specs.get('weightKg', 'N/A')} kg\n"
        formatted += f"Dimensions: {specs.get('dimensionsMm', 'N/A')} mm\n"
        formatted += f"Voltage: {specs.get('motorVoltageV', 'N/A')} V\n"
        formatted += f"ATEX Marking: {specs.get('atexMarking', 'N/A')}\n"

        return formatted


# ====================================================================
# Example usage
# ====================================================================

def main():
    print("=== Depureco MCP — LangChain Tools Demo ===\n")

    # Initialize tools
    configurator = DepurecoConfiguratorTool()
    details = DepurecoProductDetailsTool()
    specs = DepurecoTechnicalSpecsTool()

    # Demo 1: Configure a product
    print("1. Finding ATEX Zone 22 vacuums for combustible dust...")
    result = configurator.run({
        "application": "combustible-dust",
        "zoneType": "zone-22",
        "certificate": "atex",
        "limit": 3,
    })
    print(result)
    print()

    # Demo 2: Get product details
    print("2. Getting product details for PUMA ACD...")
    result = details.run({"productId": "PUMA ACD"})
    print(result[:500])
    print()

    # Demo 3: Get technical specs
    print("3. Getting technical specs for PUMA DEX 1/3D...")
    result = specs.run({"productId": "PUMA DEX 1/3D"})
    print(result)


if __name__ == "__main__":
    main()
