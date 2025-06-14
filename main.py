from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("ms-products")
mock_api_url = "https://589d8ea5400db4120026146d.mockapi.io/api/products"


@mcp.tool()
def get_products():
    response = httpx.get(mock_api_url)
    return response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")
