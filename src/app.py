import os
import logging
import asyncio

from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

app = AsyncApp(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)

@app.event("message")
async def handle_message(client, event):
    text = event.get("text", "")
    channel = event.get("channel")
    
    if "@oncall-ihub" in text:
        await client.chat_postMessage(
            channel=channel,
            text="<@payout>"
        )

async def main():
    handler = AsyncSocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    await handler.start_async()

if __name__ == "__main__":
    asyncio.run(main())