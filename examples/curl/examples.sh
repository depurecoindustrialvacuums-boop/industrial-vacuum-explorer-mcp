#!/bin/bash
#
# Depureco MCP — cURL Examples
#
# Test the Depureco MCP REST API from the command line.
#
# Endpoint: https://depureco.com/wp-json/depureco/v1/mcp
#
# Run with:
#   chmod +x examples.sh
#   ./examples.sh
#
# Requires: curl, jq (optional, for pretty output)

BASE_URL="https://depureco.com/wp-json/depureco/v1/mcp"

# Helper function for pretty JSON output (uses jq if available)
pretty() {
  if command -v jq &> /dev/null; then
    jq '.'
  else
    python3 -m json.tool 2>/dev/null || cat
  fi
}

# Section header
section() {
  echo ""
  echo "================================================================="
  echo "$1"
  echo "================================================================="
}

section "1. Get all filter options"
curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d '{"tool": "getFilterOptions"}' | pretty

section "2. Find ATEX Zone 22 vacuums for combustible dust (limit 5)"
curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "tool": "configureProduct",
    "params": {
      "application": "combustible-dust",
      "zoneType": "zone-22",
      "certificate": "atex",
      "usage": "continuous",
      "limit": 5
    }
  }' | pretty

section "3. Get complete product data for PUMA ACD"
curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "tool": "getProductData",
    "productId": "PUMA ACD"
  }' | pretty

section "4. Get technical specs for PUMA DEX 1/3D"
curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "tool": "getTechnicalSpecs",
    "productId": "PUMA DEX 1/3D"
  }' | pretty

section "5. Get accessories for ECOBULL ACD"
curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "tool": "getProductAccessories",
    "productId": "ECOBULL ACD"
  }' | pretty

section "6. List available ATEX zones"
curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d '{"tool": "getZoneTypes"}' | pretty

section "7. List available certifications"
curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d '{"tool": "getCertificates"}' | pretty

section "8. List materials that can be vacuumed"
curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d '{"tool": "getApplications"}' | pretty

echo ""
echo "Done. For more examples see: https://github.com/depurecoindustrialvacuums-boop/industrial-vacuum-explorer-mcp"
