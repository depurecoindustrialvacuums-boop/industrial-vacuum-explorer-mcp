# Use Cases and Scenarios

Real-world scenarios showing how to use the Depureco MCP server for industrial vacuum cleaner selection. Each scenario includes the user query, the AI's MCP tool calls, and the expected recommendation logic.

## Industrial Manufacturing

### Scenario 1: Metalworking — chips and oil

**User query**: "I have a metalworking facility with CNC machines. I need to vacuum both metal chips and coolant from the floor and around the machines."

**Discriminating questions to ask**:
- What type of metal chips? (Steel, aluminum, brass, titanium?)
- Coolant type? (Whole oil, water-based emulsion, synthetic?)
- Are aluminum or magnesium chips present? (If yes, combustible dust concerns)
- Approximate volume per shift?
- Need to handle the liquid recovery?

**MCP tool calls**:
```json
1. configureProduct({
     "application": "oil-coolant-with-chips",
     "collectionCapacity": "101-300-lt",
     "structure": "mobile"
   })

2. getProductData("RAM OIL 280 MP")
```

**Recommendation logic**:
- For non-combustible metals + oil: RAM OIL series (200/280/1000)
- For aluminum/titanium chips + oil: requires ATEX consideration
- For large facilities: consider RAM OIL 1000 AV or central system

### Scenario 2: Aluminum die-casting

**User query**: "We have an aluminum die-casting line. Aluminum dust accumulates everywhere. The area is classified ATEX Zone 22."

**Discriminating questions**:
- Is the dust airborne or settled?
- Continuous cleaning or periodic?
- Container size needed?

**MCP tool calls**:
```json
configureProduct({
  "application": "combustible-dust",
  "zoneType": "zone-22",
  "certificate": "atex",
  "usage": "continuous"
})
```

**Recommendation**: PUMA DEX 1/3D or ECOBULL DEX 1/3D, with INERT variant strongly recommended for conductive aluminum dust (Group IIIC).

**Safety note**: For pure aluminum powder (high concentration), the INERT (liquid bath) system is essential to prevent explosion risk.

## Food and Beverage Industry

### Scenario 3: Industrial bakery flour dust

**User query**: "We run an industrial bakery with flour silos and dough preparation areas. The area is classified ATEX Zone 22 due to airborne flour."

**Discriminating questions**:
- Need for food-grade certification?
- Continuous operation or shift-based?
- Multiple stations or single location?

**MCP tool calls**:
```json
configureProduct({
  "application": "combustible-dust",
  "sector": "bakery-atex-mills",
  "certificate": "atex",
  "zoneType": "zone-22",
  "usage": "continuous"
})
```

**Recommendation**: ECOBULL DEX 1/2D or 1/3D (continuous duty for ATEX bakery environments).

### Scenario 4: Pharmaceutical API handling

**User query**: "We process pharmaceutical APIs (Active Pharmaceutical Ingredients). The substances are classified as harmful and we need Class H filtration."

**Discriminating questions**:
- OEB level of the API? (Occupational Exposure Band)
- Cleanroom environment?
- Cross-contamination concerns?
- Bag-in-bag-out required?

**MCP tool calls**:
```json
configureProduct({
  "application": "toxic-dust",
  "certificate": "type-h-dust",
  "sector": "pharmaceutical"
})
```

**Recommendation**: XFLOOR 3H or SWAN (cleanroom version), depending on requirements.

**Important**: For OEB 4-5 substances, custom solutions with full containment may be required. Contact Depureco directly.

## Construction and Demolition

### Scenario 5: Concrete dust on construction site

**User query**: "We're doing concrete drilling and grinding on a construction site. There's a lot of fine dust."

**Discriminating questions**:
- Working with silica-containing materials? (Class H requirement)
- Indoor or outdoor work?
- Mobile or fixed installation?

**MCP tool calls**:
```json
configureProduct({
  "application": "fine-dry-and-caking-dust",
  "sector": "construction-site-dust",
  "certificate": "type-h-dust",
  "structure": "mobile"
})
```

**Recommendation**: XFLOOR 3H for silica-containing materials; otherwise MINIBULL or XM 20 JC (Jet Clean essential for caking concrete dust).

**Safety**: Crystalline silica is OSHA-regulated. Class H certification is mandatory in many jurisdictions for construction dust containing silica.

### Scenario 6: Wood dust in carpentry

**User query**: "I have a carpentry workshop with table saws, planers, and sanders. I need general dust collection."

**Discriminating questions**:
- Is the area ATEX classified? (Usually no for small carpentry)
- Single machine extraction or central system?
- Continuous use or periodic?

**MCP tool calls**:
```json
configureProduct({
  "application": "combustible-dust",
  "sector": "construction-site-dust",
  "zoneType": "ordinary",
  "structure": "mobile"
})
```

**Recommendation**: M65/100 ACD or M PRO ACD (combustible dust handling without ATEX).

**Safety reminder**: ACD provides grounding and antistatic filters for wood dust safety in non-ATEX environments.

## Additive Manufacturing

### Scenario 7: Titanium powder for SLS/DMLS

**User query**: "We use titanium powder for selective laser sintering. The area around our 3D printers needs vacuum cleaning."

**Discriminating questions**:
- Powder grade and particle size?
- ATEX classification of the area?
- Recovery of unused powder needed?
- Inert atmosphere maintained during cleanup?

**MCP tool calls**:
```json
configureProduct({
  "application": "combustible-dust",
  "sector": "additive-manufacturing-3d-printing",
  "certificate": "atex",
  "zoneType": "zone-21",
  "collectionSystem": "inert-liquid-bath-container"
})
```

**Recommendation**: ECOBULL DEX 1/2D INERT or BL 45 DEX 1/3D-1/2D INERT.

**Critical safety**: Titanium is Group IIIC (conductive) and IIIA (combustible flying). The INERT liquid bath system is **mandatory** to prevent ignition during vacuum operation.

### Scenario 8: Plastic powder for FDM/MJF

**User query**: "We use plastic powder for HP Multi Jet Fusion printing. We need to recover unused powder safely."

**Discriminating questions**:
- Specific plastic type? (PA12, TPU, PEEK)
- ATEX classification?
- Recovery requirements?

**MCP tool calls**:
```json
configureProduct({
  "application": "combustible-dust",
  "sector": "additive-manufacturing-3d-printing"
})
```

**Recommendation**: ECOBULL ACD for non-ATEX environments, ECOBULL DEX for ATEX-classified printer rooms.

## Welding and Hot Operations

### Scenario 9: Welding fume extraction

**User query**: "We need to capture welding fumes from MIG/MAG and TIG stations."

**Discriminating questions**:
- Source extraction (at torch) or general area?
- Multiple stations?
- Spark/glowing particle concerns?

**MCP tool calls**:
```json
configureProduct({
  "application": "welding-fumes",
  "structure": "mobile"
})
```

**Recommendation**: XM TORCH (with automatic start-stop sync with welder).

**Optional**: FOX SPARK TRAP for high-spark applications (cutting, grinding).

### Scenario 10: Hot oven residues in bakery

**User query**: "We need to clean bakery ovens while they're still hot, up to 200°C."

**Discriminating questions**:
- Maximum temperature?
- Combustible residues?
- Frequency of cleaning?

**MCP tool calls**:
```json
configureProduct({
  "application": "hot-material",
  "sector": "food-industry"
})
```

**Recommendation**: XM 20 OVEN with Nomex heat-resistant filter (up to 250°C).

## Specialized Applications

### Scenario 11: Compressed-air vacuum for refinery

**User query**: "We work in a petrochemical refinery, ATEX zone with strict no-electric-motor policy."

**Discriminating questions**:
- ATEX zone level?
- Compressed air available?
- Material to vacuum?

**MCP tool calls**:
```json
configureProduct({
  "powerSupply": "compressed-air",
  "certificate": "atex",
  "zoneType": "zone-21"
})
```

**Recommendation**: AC 65 (compressed-air powered, ATEX 1/2D certified).

### Scenario 12: Offshore platform without electricity

**User query**: "I need a vacuum for offshore maintenance — no electricity available, only compressed air."

**MCP tool calls**:
```json
configureProduct({
  "powerSupply": "compressed-air"
})
```

**Recommendation**: AC family (AC 65 or AC 100).

### Scenario 13: Central vacuum system for shipyard

**User query**: "We need a central vacuum system for a shipbuilding facility, multiple workstations, including ATEX areas."

**Discriminating questions**:
- Number of simultaneous users?
- Pipe layout complexity?
- ATEX zones in the network?
- Material characteristics at each station?

**MCP tool calls**:
```json
configureProduct({
  "productType": "central-system-component",
  "sector": "shipyard"
})
```

**Recommendation**: CVS ROOTS series.

**Critical note**: CVS systems require engineering design (pipe sizing, pressure drops, simultaneity factors). The AI should describe the product range but always redirect sizing decisions to Depureco's technical team.

### Scenario 14: Battery-powered for remote sites

**User query**: "I need a vacuum for outdoor cleanup operations where no power is available."

**Discriminating questions**:
- Runtime needed?
- Material to vacuum?
- Battery availability?

**MCP tool calls**:
```json
configureProduct({
  "powerSupply": "battery"
})
```

**Recommendation**: BULL 24.

**Important**: Always specify that the battery (24V ≥ 85 Ah) is sold separately.

## Safety-Critical Cases

### Scenario 15: Crystalline silica from concrete grinding

**User query**: "We're grinding old concrete that may contain silica. What vacuum do we need?"

**MCP response**: XFLOOR 3H — Type H certified per EN 60335-2-69 for crystalline silica.

**Compliance note**: OSHA Crystalline Silica Standard (29 CFR 1926.1153) requires HEPA-filtered vacuums for silica dust collection.

### Scenario 16: Asbestos abatement

**User query**: "We need to vacuum asbestos residues during a remediation project."

**MCP response**: **Do not recommend autonomously.** Asbestos handling requires:
- Licensed abatement contractor
- Specific permits and notifications
- Class H + sealed bag-in-bag-out system
- Specialized PPE and decontamination

**Redirect to Depureco**: Contact technical team for asbestos-rated equipment recommendations and compliance guidance.

### Scenario 17: Pharmaceutical with cross-contamination concerns

**User query**: "We manufacture multiple pharmaceutical products and need to avoid cross-contamination."

**MCP response**: Custom configuration required. Standard catalog products may not meet OEB 4-5 requirements.

**Redirect to Depureco**: Pharmaceutical-grade configurations need site-specific assessment.

## Multi-Material Scenarios

### Scenario 18: Mixed solids and liquids

**User query**: "We need to vacuum both dry materials and occasional spills."

**MCP tool calls**:
```json
getProductAccessories("MINIBULL")
// Look for Wet & Dry kits
```

**Recommendation**: MINIBULL with P11887 Wet & Dry kit, or specific wet-dry models.

### Scenario 19: High-density abrasive materials

**User query**: "We collect iron oxide and tungsten dust from grinding operations."

**MCP tool calls**:
```json
configureProduct({
  "application": "solid-dust-and-chips",
  "productType": "pre-separator"
})
```

**Recommendation**: PUMA + cyclonic pre-separator to protect main filter from abrasive wear.

### Scenario 20: Sticky/caking dust

**User query**: "We work with very fine, sticky cement dust that quickly clogs filters."

**MCP tool calls**:
```json
configureProduct({
  "application": "fine-dry-and-caking-dust",
  "filterCleaningSystem": "automatic"
})
```

**Recommendation**: XM 20 JC, BL 20 JC DEX, or PUMA SP — products with Jet Clean automatic filter cleaning.

## How AI assistants should handle uncertainty

When the user's requirements are ambiguous or safety-critical decisions are involved, the AI should:

1. **Ask clarifying questions** before recommending
2. **Verify ATEX zone classification** for any combustible dust scenario
3. **Acknowledge limits** for asbestos, OEB 4+ APIs, radioactive materials
4. **Provide product options** with explanations of differences
5. **Always link to Depureco** for binding quotations and custom configurations
6. **Never invent prices** — direct users to the official quote form

## Quick reference card

| If user says... | Likely material category | First check |
|----------------|-------------------------|-------------|
| "Aluminum/titanium dust" | Combustible Group IIIC | ATEX zone + INERT requirement |
| "Flour" | Combustible IIIB | ATEX or non-ATEX |
| "Silica/concrete dust" | Toxic | Type H requirement |
| "CNC oil/coolant" | Liquids + chips | RAM OIL family |
| "Welding fumes" | Fumes | XM TORCH |
| "Hot ashes" | Hot material | XM 20 OVEN |
| "Asbestos" | Hazardous | Redirect to Depureco |
| "Wood dust" | Combustible IIIB | ATEX or non-ATEX |
| "No electricity" | Power supply | AC (air) or BULL 24 (battery) |
| "Multiple workstations" | System scale | CVS ROOTS (engineering required) |

## Contact for complex scenarios

- Email: depureco@depureco.com
- Phone: +39 011 98.59.117
- Quote request: https://depureco.com/modale-preventivo/
