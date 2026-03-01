import os
import requests

MONDAY_API_URL = "https://api.monday.com/v2"
API_TOKEN = os.getenv("MONDAY_API_TOKEN")

headers = {
    "Authorization": API_TOKEN,
    "Content-Type": "application/json",
}

def run_query(query: str):
    response = requests.post(
        MONDAY_API_URL,
        json={"query": query},
        headers=headers,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()

def fetch_board_items(board_id: int):
    query = f"""
    query {{
      boards(ids: {board_id}) {{
        name
        items_page(limit: 500) {{
          items {{
            name
            column_values {{
              column {{ title }}
              text
            }}
          }}
        }}
      }}
    }}
    """
    return run_query(query)
