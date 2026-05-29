# Changelog

All notable changes to the Depureco Industrial Vacuum MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2025-01-01

### Added

- Initial public release of the Depureco Industrial Vacuum MCP Server
- 20 MCP tools for product configuration and discovery:
  - Core workflow tools (6): `getAssistantInstructions`, `getFilterOptions`, `configureProduct`, `getProductData`, `getTechnicalSpecs`, `getProductAccessories`
  - Single-filter lookup tools (14): `getApplications`, `getSectors`, `getProductCategories`, `getProductTypes`, `getPowerSupplies`, `getPowerValues`, `getMotorPowerValues`, `getCollectionCapacities`, `getCollectionSystems`, `getFilterCleaningSystems`, `getStructures`, `getUsages`, `getZoneTypes`, `getCertificates`
- Coverage of 150+ industrial vacuum products
- 24 industrial sectors supported
- ATEX certification data for 38 products (Zone 21, Zone 22, Zone 2)
- Type H dust certification data (EN 60335-2-69)
- Multilingual product URLs (IT, EN, DE, FR, ES, RO)
- Multilingual manuals and brochures
- Integration examples in Python, JavaScript, cURL, LangChain
- OpenAPI 3.0 specification
- AI discovery files (llms.txt)
- Full documentation on ATEX zones, filter classes, product families, use cases

### MCP server details

- Endpoint: `https://depureco.com/wp-json/depureco/v1/mcp`
- Type: Remote MCP (WebMCP over HTTP)
- Authentication: None required (public access)
- Language: English (catalog data); multilingual product URLs
- License: MIT (code and examples)

## [Unreleased]

### Planned

- `compareProducts` tool for side-by-side product comparison
- Enhanced multilingual support for product descriptions
- Webhook support for catalog updates
- Filter for installation/application notes
- Expanded power range filters
