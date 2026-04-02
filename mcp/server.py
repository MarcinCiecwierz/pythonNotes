import requests
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('API_URL')

mcp = FastMCP("Notes Base")

@mcp.tool()
def get_all_notes() -> list:
    """Gets all notes from database"""
    res = requests.get(f"{API_URL}/")
    return res.json()

@mcp.tool()
def get_note(id: int) -> dict:
    """Gets note by id"""
    res = requests.get(f"{API_URL}/", params={"id": id})
    return res.json()

@mcp.tool()
def create_note(title: str, content: str, tags: str) -> dict:
    """Creates new note (tags has to be comma separated)"""
    res = requests.post(f"{API_URL}/add", json={
        "title": title,
        "content": content,
        "tags": tags
    })
    return res.json()

@mcp.tool()
def delete_note(id: int) -> bool:
    """Deletes note by id"""
    res = requests.delete(f"{API_URL}/{id}")
    return res.json

if __name__ == "__main__":
    mcp.run()