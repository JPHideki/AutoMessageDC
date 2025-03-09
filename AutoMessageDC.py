import discord
import asyncio

# Your Discord user token
TOKEN = ''

# The channel ID to send messages to
CHANNEL_ID = 

# Messages to send
PHRASES = [
  
    "TEXT",
    "TEXT"
 
]

# Interval between messages in seconds
INTERVAL = 70

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        channel = self.get_channel(CHANNEL_ID)
        if channel is None:
            print("Invalid CHANNEL_ID. Please check.")
            return

        while True:
            for phrase in PHRASES:
                try:
                    await channel.send(phrase)
                    print(f"Sent: {phrase}")
                except Exception as e:
                    print(f"Error sending message: {e}")
                await asyncio.sleep(INTERVAL)

            # After sending all phrases, exit the loop
            print("All messages sent. Exiting...")
            break

        await self.close()

# Run the bot
client = MyClient()
client.run(TOKEN)  # No `bot=False`
