# API Reference

Quick reference for all 20 tools exposed by the Depureco MCP server.

## Endpoint

```
POST https://depureco.com/wp-json/depureco/v1/mcp
Content-Type: application/json
```

## Request format

All tool calls use the same endpoint with a JSON body:

```json
{
  "tool": "<toolName>",
  "params": { ... },        // optional parameters
  "productId": "<id>"        // for product-specific tools
}
```

## Core workflow tools

### `getAssistantInstructions`

Returns operational guidelines for the AI.

**Parameters**: none

```json
{ "tool": "getAssistantInstructions" }
```

**Recommended**: Call first before any other tool.

---

### `getFilterOptions`

Returns all available product search criteria.

**Parameters** (all optional):
- `search` (string): Text filter for results
- `includeEmpty` (boolean): Include terms with no published products (default: false)

```json
{
  "tool": "getFilterOptions",
  "params": { "search": "atex" }
}
```

**Recommended**: Call before `configureProduct` to discover valid filter values.

---

### `configureProduct`

Finds products matching specific criteria.

**Parameters** (all optional):

| Parameter | Type | Description |
|-----------|------|-------------|
| `application` | string | Material/application slug |
| `sector` | string | Industrial sector slug |
| `productCategory` | string | Safety category slug |
| `productType` | string | Product type slug |
| `powerSupply` | string | Power supply slug |
| `motorPower` | string | Motor power value |
| `power` | string | Total power value |
| `collectionCapacity` | string | Capacity slug |
| `collectionSystem` | string | Collection system slug |
| `filterCleaningSystem` | string | Filter cleaning slug |
| `structure` | string | Structure slug |
| `usage` | string | Usage mode slug |
| `zoneType` | string | ATEX zone slug |
| `certificate` | string | Certificate slug |
| `limit` | integer | Max results (1-25, default 10) |

```json
{
  "tool": "configureProduct",
  "params": {
    "application": "combustible-dust",
    "zoneType": "zone-22",
    "certificate": "atex",
    "limit": 5
  }
}
```

---

### `getProductData`

Returns complete product sheet.

**Parameters**:
- `productId` (required, string): Product name, title, or numeric ID

```json
{
  "tool": "getProductData",
  "productId": "PUMA ACD"
}
```

**Returns**: Description, highlights, features, options, accessories, manuals, brochures, multilingual URLs.

---

### `getTechnicalSpecs`

Returns precise numerical specifications.

**Parameters**:
- `productId` (required, string): Product name, title, or numeric ID

```json
{
  "tool": "getTechnicalSpecs",
  "productId": "PUMA DEX 1/3D"
}
```

**Returns**: Motor power, airflow, vacuum, filter class/area, dimensions, weight, ATEX marking, voltage, frequency.

---

### `getProductAccessories`

Returns compatible accessories.

**Parameters**:
- `productId` (required, string): Product name, title, or numeric ID

```json
{
  "tool": "getProductAccessories",
  "productId": "ECOBULL ACD"
}
```

**Returns**: List of accessories with code, name, description, image URL.

---

## Single-filter lookup tools

All single-filter tools share the same parameter signature:

```json
{
  "tool": "<lookupTool>",
  "params": {
    "search": "<text>",          // optional
    "includeEmpty": false         // optional
  }
}
```

### `getApplications`

Materials that can be vacuumed. 13 categories.

### `getSectors`

Industrial sectors served. 24 sectors.

### `getProductCategories`

Product safety categories: ACD, 1/2D, 1/3D, 3D, 3GD, 3/3G, 1/3D-1/2D.

### `getProductTypes`

Product types: mobile vacuum, fixed dust collector, central system component, pre-separator, professional vacuum.

### `getPowerSupplies`

Power supplies: electric, compressed air, battery.

### `getPowerValues`

Total product power ranges available.

### `getMotorPowerValues`

Motor power values in kW/HP.

### `getCollectionCapacities`

Container capacities: 20-50L, 51-100L, 101-300L, 300L+.

### `getCollectionSystems`

Collection systems: stainless steel container, Longopac (continuous bag), inert liquid bath, piped discharge.

### `getFilterCleaningSystems`

Filter cleaning systems: manual shaker, Jet Clean, automatic backflush, pneumatic shaker.

### `getStructures`

Product structures: mobile (cart) or fixed.

### `getUsages`

Usage modes: occasional or continuous.

### `getZoneTypes`

Certified ATEX zones: Zone 22, Zone 21, Zone 2, ordinary.

### `getCertificates`

Available certifications: CE, ATEX, Type H dust.

---

## Response format

Successful responses return JSON with varying structures depending on the tool:

### Lookup tools

```json
{
  "items": [
    { "slug": "...", "name": "...", "count": 5 },
    ...
  ]
}
```

### `configureProduct`

```json
{
  "total": 5,
  "count": 5,
  "products": [
    {
      "product_id": 12345,
      "slug": "puma-acd",
      "title": "PUMA ACD",
      "type": "...",
      "description": "...",
      "image": "https://...",
      "urls": { "it": "...", "en": "...", ... }
    },
    ...
  ]
}
```

### `getProductData`

```json
{
  "product_id": 12345,
  "title": "...",
  "description": "...",
  "highlights": [...],
  "features": [...],
  "options": [...],
  "accessories": [...],
  "manuals": { "it": "...", "en": "..." },
  "brochures": { "it": "...", "en": "..." }
}
```

### `getTechnicalSpecs`

```json
{
  "technicalSpecs": {
    "motorPowerKwHp": "7.5 kW / 10 HP",
    "airflowM3h": "700",
    "continuousVacuumMbar": "280",
    "atexMarking": "II 1/3D Ex h IIIC T140°C Da/Dc",
    ...
  }
}
```

---

## Error responses

- **400 Bad Request**: Invalid tool name or parameters
- **404 Not Found**: Product or filter value not found
- **500 Server Error**: Unexpected server error

---

## Rate limiting

The endpoint is publicly accessible with reasonable rate limiting. For high-volume integrations, contact Depureco for dedicated access.

## Authentication

None required for read-only operations on the public catalog.

## Further reading

- [README](../README.md) — Main documentation
- [ATEX Zones](./atex-zones.md) — Safety classifications
- [Filter Classes](./filter-classes.md) — Filtration standards
- [Product Families](./product-families.md) — Catalog overview
- [Use Cases](./use-cases.md) — Real-world scenarios
- [OpenAPI Spec](../openapi.yaml) — Machine-readable API definition
