/**
 * Depureco MCP — Basic JavaScript Example (Node.js)
 *
 * Demonstrates how to call the Depureco MCP REST API from Node.js.
 * Uses the built-in fetch API (Node 18+).
 *
 * Endpoint: https://depureco.com/wp-json/depureco/v1/mcp
 *
 * Run with:
 *   node basic_query.js
 */

const BASE_URL = 'https://depureco.com/wp-json/depureco/v1/mcp';

/**
 * Generic helper to call any MCP tool.
 * @param {string} tool - Tool name
 * @param {object} [params] - Optional parameters
 * @param {string} [productId] - Optional product ID
 * @returns {Promise<object>} JSON response
 */
async function callMcp(tool, params = null, productId = null) {
  const payload = { tool };
  if (params) payload.params = params;
  if (productId) payload.productId = productId;

  const response = await fetch(BASE_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
  }

  return await response.json();
}

/**
 * Example: Find ATEX-certified vacuums for combustible dust.
 */
async function findAtexVacuums() {
  console.log('Finding ATEX Zone 22 vacuums for combustible dust...');
  const result = await callMcp('configureProduct', {
    application: 'combustible-dust',
    zoneType: 'zone-22',
    certificate: 'atex',
    limit: 5,
  });

  console.log(`Found ${result.total || 0} products:`);
  for (const product of result.products || []) {
    console.log(`  - ${product.title}`);
    console.log(`    ${product.urls?.en || ''}`);
  }
}

/**
 * Example: Get complete product data.
 */
async function getProductDetails(productId) {
  console.log(`\nGetting full product data for: ${productId}`);
  const data = await callMcp('getProductData', null, productId);

  if (data.product_id) {
    console.log(`Title: ${data.title}`);
    console.log(`Type:  ${data.type}`);
    console.log(`Highlights: ${data.highlights?.length || 0} sections`);
    console.log(`Features:   ${data.features?.length || 0} standard features`);
    console.log(`Accessories: ${data.accessories?.length || 0} items`);
  }
}

/**
 * Example: Compare technical specs of two products.
 */
async function compareSpecs(product1, product2) {
  console.log(`\nComparing ${product1} vs ${product2}...`);

  const [specs1, specs2] = await Promise.all([
    callMcp('getTechnicalSpecs', null, product1),
    callMcp('getTechnicalSpecs', null, product2),
  ]);

  console.log('\nMetric           | Product 1      | Product 2');
  console.log('-----------------+----------------+----------------');

  const fields = [
    ['Motor Power', 'motorPowerKwHp'],
    ['Airflow m3/h', 'airflowM3h'],
    ['Vacuum mbar', 'continuousVacuumMbar'],
    ['Capacity L', 'containerCapacityLt'],
    ['Weight kg', 'weightKg'],
  ];

  for (const [label, key] of fields) {
    const v1 = (specs1.technicalSpecs?.[key] || 'N/A').padEnd(14);
    const v2 = specs2.technicalSpecs?.[key] || 'N/A';
    console.log(`${label.padEnd(16)} | ${v1} | ${v2}`);
  }
}

/**
 * Main runner.
 */
async function main() {
  console.log('=== Depureco MCP — JavaScript Examples ===\n');

  try {
    await findAtexVacuums();
    await getProductDetails('PUMA ACD');
    await compareSpecs('PUMA DEX 1/3D', 'PUMA DEX 1/2D');
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

main();
