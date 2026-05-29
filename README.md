# Depureco Industrial Vacuum MCP Server

> The first Remote MCP Server (WebMCP) for industrial vacuum cleaner configuration. AI assistants can query 150+ products across 24 industrial sectors with full ATEX certification data, technical specifications, and accessory compatibility.

[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blue)](https://modelcontextprotocol.io)
[![Remote MCP](https://img.shields.io/badge/Remote%20MCP-WebMCP-green)](https://depureco.com/wp-json/depureco/v1/mcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Products](https://img.shields.io/badge/Products-150%2B-orange)](https://depureco.com)
[![ATEX Certified](https://img.shields.io/badge/ATEX-Certified-red)](https://depureco.com)

## What is this?

This is a **Remote MCP (Model Context Protocol) server** that enables AI assistants — including Claude, ChatGPT, Perplexity, Gemini, and any MCP-compatible client — to intelligently configure and recommend industrial vacuum cleaners from [Depureco Industrial Vacuums](https://depureco.com).

Unlike generic product configurators, this server understands:

- ATEX directive 2014/34/EU and zone classifications (Zone 20, 21, 22)
- Dust group classifications IIIA, IIIB, IIIC (EN 60079-10-2)
- Filter class standards (Class M, Class H, HEPA H13/H14 per EN 1822)
- Combustible dust regulations (NFPA 652, NFPA 484)
- Food-grade and pharmaceutical environment requirements
- Inert liquid bath systems for conductive metal dusts
- Hot material extraction (up to 250°C)
- Atmospheric explosion prevention (ATEX, IECEx)

**No installation required.** It is a hosted REST endpoint accessible via HTTP from any MCP-compatible AI client.

## Endpoint

```
https://depureco.com/wp-json/depureco/v1/mcp
```

## Quick Start

### Use with Claude.ai

The server is available as a connected MCP app in Claude.ai. Once connected, simply ask:

> "Find me an industrial vacuum for combustible aluminum dust in ATEX Zone 22"
>
> "What is the difference between PUMA ACD and PUMA DEX 1/3D?"
>
> "I need a vacuum for a CNC machining center handling both chips and coolant"
>
> "Which vacuum is certified for IIIC group conductive dust?"

### Direct REST API

```bash
curl https://depureco.com/wp-json/depureco/v1/mcp \
  -H "Content-Type: application/json" \
  -d '{
    "tool": "configureProduct",
    "params": {
      "application": "combustible-dust",
      "zoneType": "zone-22",
      "usage": "continuous",
      "limit": 5
    }
  }'
```

### Connect any MCP Client

```json
{
  "mcpServers": {
    "depureco": {
      "type": "url",
      "url": "https://depureco.com/wp-json/depureco/v1/mcp",
      "name": "depureco-industrial-vacuums"
    }
  }
}
```

## Why this matters for AI safety

Industrial vacuum selection is a **safety-critical, technically complex** domain. AI hallucination in this context can mean:

- Recommending a non-certified vacuum in an explosive atmosphere (legal liability, safety risk)
- Under-specifying filtration for toxic or carcinogenic dusts (health hazard)
- Wrong ATEX category for the zone classification (regulatory non-compliance)
- Inadequate inerting for conductive metal dusts (fire and explosion risk)

This MCP server gives AI assistants access to authoritative structured data on 150+ products across 24 industrial sectors, enabling accurate, safe recommendations grounded in real product specifications, not training data assumptions.

## Available Tools

### Core workflow tools

| Tool | Description |
|------|-------------|
| `getAssistantInstructions` | Operational guidelines for the AI. Call first. |
| `getFilterOptions` | All available product search criteria (materials, sectors, ATEX zones, etc.) |
| `configureProduct` | Find products matching specific criteria |
| `getProductData` | Complete product sheet (highlights, features, options, accessories, manuals) |
| `getTechnicalSpecs` | Precise technical data (power, airflow, vacuum, filter, dimensions, ATEX marking) |
| `getProductAccessories` | Compatible accessories with codes and images |

### Single-filter lookup tools

| Tool | Returns |
|------|---------|
| `getApplications` | Materials that can be vacuumed (13 categories) |
| `getSectors` | Industrial sectors (24 sectors) |
| `getProductCategories` | Product safety categories (ACD, ATEX 1/2D, 1/3D, 3D, 3GD) |
| `getProductTypes` | Product types (mobile vacuum, fixed dust collector, pre-separator) |
| `getPowerSupplies` | Available power supplies (electric, compressed air, battery) |
| `getPowerValues` | Total product power ranges |
| `getMotorPowerValues` | Motor power values in kW/HP |
| `getCollectionCapacities` | Container capacities (20-50L, 51-100L, 101-300L, 300L+) |
| `getCollectionSystems` | Collection systems (stainless steel, Longopac, inert liquid bath) |
| `getFilterCleaningSystems` | Filter cleaning systems (manual, Jet Clean, automatic backflush) |
| `getStructures` | Product structure (mobile or fixed) |
| `getUsages` | Usage mode (occasional or continuous) |
| `getZoneTypes` | Certified ATEX zones (Zone 22, Zone 21, Zone 2, ordinary) |
| `getCertificates` | Available certifications (CE, ATEX, Type H dust) |

## Data Coverage

### Materials and Applications (13 categories)

| Category | Examples | Products |
|----------|----------|---------:|
| Solid dust and chips | Steel chips, aluminum, brass, iron oxide | 51 |
| Fine, dry and caking dust | Flour, cement, plaster, talc, kaolin | 50 |
| Combustible dust | Aluminum powder, titanium, magnesium, wood, sugar | 37 |
| Wet dust or solids | Damp materials, post-cleaning residues | 34 |
| Toxic or hazardous dust | Silica, asbestos, lead, pharmaceutical APIs | 13 |
| Airborne and suspended dust | Lightweight particles, fibers | 11 |
| Oil and coolant with chips | CNC machining fluids | 10 |
| Bulky scraps and trimmings | Plastic film, fabric, paper | 3 |
| Liquids | Industrial water, detergents | 3 |
| Welding fumes | Smoke and particulates | 2 |
| Oil mist | Lathe and CNC microparticles | 1 |
| Sludge and sediment | Pasty residues, oily sludge | 1 |
| Hot material | Up to 250°C (oven residues) | 2 |

### Industrial Sectors (24 sectors)

Metalworking, food industry, pharmaceutical, additive manufacturing (3D printing), bakeries with ATEX classification, construction, shipbuilding, packaging, foundries, cement plants, battery production, CNC machining, woodworking, plastics processing, chemical industry, electronics, automotive, aerospace, mining, oil and gas, textile industry, paper mills, glass production, ceramics.

### Certifications

- **CE marking** — 138 products
- **ATEX 2014/34/EU** — 38 products (Zone 21, Zone 22, Zone 2)
- **Type H dust (EN 60335-2-69)** — 2 products (carcinogenic dust, crystalline silica)
- **IECEx** — selected variants
- **GS marking** — selected products

### ATEX Categories Available

| Category | Internal Zone | External Zone | Use Case |
|----------|--------------|---------------|----------|
| 1/2D | Zone 20 | Zone 21 | Maximum protection, occasional explosive atmosphere |
| 1/3D | Zone 20 | Zone 22 | Internal max protection, external rare events |
| 3D | — | Zone 22 | External-only zone 22 protection |
| 3GD | Zone 22 (gas+dust) | — | Combined gas and dust protection |
| ACD | — | — | Combustible dust in non-ATEX zones |
| 3/3G | — | Zone 2 (gas) | Gas atmospheres only |
| 1/3D-1/2D | Zone 20 | Zone 21 or 22 | Dual-zone certification |

## Real-World Use Cases

### Case 1: ATEX Zone 22 Bakery

```
User: "Flour dust extraction for an industrial bakery, continuous use"
AI calls: configureProduct(
  application="combustible-dust",
  sector="bakery-atex-mills",
  certificate="atex",
  zoneType="zone-22",
  usage="continuous"
)
Result: ECOBULL DEX 1/2D, DF 40 DEX 1/3D, ECOBULL XM DEX 1/2D
```

### Case 2: Additive Manufacturing Titanium Powder

```
User: "Titanium powder vacuum for additive manufacturing facility in ATEX Zone 21"
AI calls: configureProduct(
  application="combustible-dust",
  sector="additive-manufacturing-3d-printing",
  certificate="atex",
  zoneType="zone-21",
  collectionSystem="inert-liquid-bath-container"
)
Result: ECOBULL DEX 1/2D INERT, BL 45 DEX 1/3D-1/2D INERT
```

### Case 3: CNC Oil and Coolant Extraction

```
User: "Oil and coolant vacuum for CNC machining center, 280L capacity"
AI calls: configureProduct(
  application="oil-coolant-with-chips",
  collectionCapacity="101-300-lt",
  structure="mobile"
)
Result: RAM OIL 280 MP, RAM OIL 200 MP
```

### Case 4: Welding Fume Extraction at Source

```
User: "I need to capture welding fumes at the torch"
AI calls: configureProduct(
  application="welding-fumes",
  structure="mobile",
  usage="continuous"
)
Result: XM TORCH with automatic start-stop from welder signal
```

## Product Families

| Family | Description | Variants | Capacity Range |
|--------|-------------|----------|----------------|
| **MINIBULL / XM** | Compact industrial vacuums | Standard, ACD, H, INERT | 20-45 L |
| **BL PRO** | Brushless motor, >20,000h lifetime | ACD, DEX 1/2D-1/3D | 45 L |
| **ECOBULL** | Side-channel turbine, continuous duty | ACD, DEX 1/2D, DEX 1/3D, XM, INERT | 65-100 L |
| **TX** | Heavy-duty mobile | ACD, DEX | 100 L |
| **PUMA** | High-power 3-phase | Standard, SP, ACD, DEX | 175 L |
| **PUMA HD** | Maximum performance | ACD, DEX | 175 L |
| **RAM OIL** | Oil and chip extraction for CNC | 200 MP, 280 MP, 1000 AV | 200-1000 L |
| **XM TORCH** | Welding fume extraction | 1-2 motors | Configurable |
| **XM 20 OVEN** | Hot material extraction | Standard | 20 L (up to 250°C) |
| **XFLOOR** | Floor preparation, Type H certified | Standard, Plus | Variable |
| **AS / AS HD** | Scrap and trim collection | Standard, HD | Configurable |
| **DF** | Fixed dust collectors | Standard, SP, DEX | Configurable |
| **CVS ROOTS** | Central vacuum systems up to 37 kW | Standard, ATEX Z22 | Configurable |
| **AC** | Compressed-air pneumatic vacuums | ATEX 1/2D | Configurable |
| **BULL 24** | Battery-powered (battery sold separately) | Standard | 65 L |

## Integration Examples

### Python

See [`examples/python/`](./examples/python/) for full scripts:

```python
import requests

BASE_URL = "https://depureco.com/wp-json/depureco/v1/mcp"

def find_atex_vacuum(zone, application):
    response = requests.post(BASE_URL, json={
        "tool": "configureProduct",
        "params": {
            "application": application,
            "zoneType": zone,
            "certificate": "atex",
            "usage": "continuous",
            "limit": 5
        }
    })
    return response.json()

vacuums = find_atex_vacuum(zone="zone-22", application="combustible-dust")
```

### JavaScript / Node.js

See [`examples/javascript/`](./examples/javascript/) for full scripts:

```javascript
const BASE_URL = 'https://depureco.com/wp-json/depureco/v1/mcp';

async function configureVacuum(params) {
  const response = await fetch(BASE_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ tool: 'configureProduct', params })
  });
  return response.json();
}
```

### LangChain Tool

See [`examples/langchain/`](./examples/langchain/) for full integration:

```python
from langchain.tools import BaseTool
import requests

class DepurecoConfiguratorTool(BaseTool):
    name = "depureco_vacuum_configurator"
    description = "Find industrial vacuum cleaners for specific applications including ATEX zones, combustible dust, oils, welding fumes."

    def _run(self, query: str) -> str:
        import json
        params = json.loads(query)
        response = requests.post(
            "https://depureco.com/wp-json/depureco/v1/mcp",
            json={"tool": "configureProduct", "params": params}
        )
        return response.json()
```

### cURL

See [`examples/curl/`](./examples/curl/) for full scripts.

## Recommended Workflow for AI Agents

1. `getAssistantInstructions()` — Load operational guidelines
2. `getFilterOptions()` — Discover available search criteria
3. Gather discriminating information from the user (ATEX zone, material type, volume)
4. `configureProduct(params)` — Find matching products
5. `getProductData(productId)` — Retrieve complete product sheet
6. `getTechnicalSpecs(productId)` — Get precise numerical specifications for comparison
7. `getProductAccessories(productId)` — List compatible accessories

## Documentation

- [ATEX Zones Explained](./docs/atex-zones.md)
- [Filter Class Standards](./docs/filter-classes.md)
- [Product Families Overview](./docs/product-families.md)
- [Use Cases and Scenarios](./docs/use-cases.md)
- [API Reference](./docs/api-reference.md)

## About Depureco

[Depureco Industrial Vacuums](https://depureco.com) is an Italian manufacturer of industrial vacuum cleaners founded in Turin, Italy. With over 30 years of experience and 150+ products across standard, ACD, and ATEX-certified models, Depureco serves industries worldwide.

- **Website**: [depureco.com](https://depureco.com)
- **Email**: depureco@depureco.com
- **Phone**: +39 011 98.59.117
- **Headquarters**: Turin, Italy
- **Quote Request**: [https://depureco.com/modale-preventivo/](https://depureco.com/modale-preventivo/)

## License

MIT License — see [LICENSE](LICENSE) for details.

The product data, images, and technical specifications are proprietary to Depureco Industrial Vacuums and subject to their terms of use.

## Contributing

Issues and pull requests welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Citation

If you use this MCP server in academic or technical publications, please cite:

```
Depureco Industrial Vacuums. (2025). Depureco Industrial Vacuum MCP Server.
GitHub repository: https://github.com/depurecoindustrialvacuums-boop/industrial-vacuum-explorer-mcp
```

See [CITATION.cff](CITATION.cff) for machine-readable citation metadata.

---

Built in Turin, Italy. Bringing industrial vacuum engineering into the AI era.
