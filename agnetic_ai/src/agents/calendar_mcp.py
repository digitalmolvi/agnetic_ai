import os
import json
import sys
import logging
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from mcp.server.fastmcp import FastMCP

load_dotenv()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

mcp = FastMCP("Google Calendar MCP", dependencies=["google-api-python-client", "python-dotenv"])

def get_credentials():
    return Credentials(
        None,
        refresh_token=os.getenv("GOOGLE_REFRESH_TOKEN"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET")
    )

@mcp.tool()
async def create_event(summary: str, start_time: str, end_time: str, location: str = None) -> str:
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': summary,
        'start': {'dateTime': start_time, 'timeZone': 'Asia/Karachi'},
        'end': {'dateTime': end_time, 'timeZone': 'Asia/Karachi'},
        'location': location,
        'reminders': {
            'useDefault': False,
            'overrides': [{'method': 'popup', 'minutes': 30}]
        }
    }

    created_event = service.events().insert(calendarId='primary', body=event).execute()
    return f"Event created: {created_event.get('htmlLink')}"

def main():
    try:
        mcp.run()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")

if __name__ == "__main__":
    main()
