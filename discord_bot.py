import discord
from config import discord_token
from generate_response import generate_response
def discord_bot():
    
    class MyClient(discord.Client):
        async def on_ready(self):
            print(f'\033[0;34mSigned in as {self.user}\033[0m')

        async def on_message(self, message):
            print(f'Message from {message.author}: {message.content}')
            print(generate_response(f'Message from {message.author}: {message.content}'))

    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)
    client.run(discord_token)

if __name__ == "__discord_bot__":
    discord_bot()