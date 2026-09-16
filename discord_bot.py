import discord
from config import discord_token
from generate_response import generate_response

message_history = []

def discord_bot():
    
    class MyClient(discord.Client):
        async def on_ready(self):
            print(f'\033[0;34mSigned in as {self.user}\033[0m')

        async def on_message(self, message):

            message_history.append(f"{message.author} said:{message.content}")

            if message.author == self.user or self.user not in message.mentions:
                return

            response = generate_response(f"""
            Message History:{message_history}

            Latest message from {message.author}: {message.content}""")
            await message.channel.send(response)

    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)
    client.run(discord_token)

if __name__ == "__discord_bot__":
    discord_bot()
