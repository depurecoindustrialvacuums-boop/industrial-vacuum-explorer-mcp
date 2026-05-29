# Integration Examples

This folder contains working integration examples for the Depureco MCP server in various languages and frameworks.

## Available examples

### Python (`python/`)

- **`basic_query.py`** — Minimal Python example using `requests`. Shows all main tools.
- **`atex_configurator.py`** — Specialized example for ATEX-certified vacuum selection.

```bash
cd python/
pip install requests
python basic_query.py
```

### JavaScript / Node.js (`javascript/`)

- **`basic_query.js`** — Node.js example using the built-in `fetch` API (Node 18+).

```bash
cd javascript/
node basic_query.js
```

### cURL / Bash (`curl/`)

- **`examples.sh`** — Shell script with all main API calls.

```bash
cd curl/
chmod +x examples.sh
./examples.sh
```

### LangChain (`langchain/`)

- **`langchain_tool.py`** — Three LangChain BaseTool wrappers ready for agents.

```bash
cd langchain/
pip install langchain langchain-community requests pydantic
python langchain_tool.py
```

## Want to add more examples?

We welcome contributions for:

- **LlamaIndex** integration
- **AutoGen** multi-agent setups
- **CrewAI** agent crews
- **Ruby, Go, Rust, PHP, Java** native clients
- **Browser-based JavaScript** examples
- **Custom MCP clients**

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## Endpoint reminder

```
https://depureco.com/wp-json/depureco/v1/mcp
```

No authentication required. Public access.

## Need help?

- Open a GitHub issue for technical questions
- Email Depureco: depureco@depureco.com
