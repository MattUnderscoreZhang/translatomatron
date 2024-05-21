import discord
from dotenv import load_dotenv
from gpt_interface import GptInterface
import os
from typing import cast


if __name__ == "__main__":
    load_dotenv()
    TOKEN=cast(str, os.getenv("BOT_TOKEN"))
    BOT_PUBLIC_KEY=cast(str, os.getenv("BOT_PUBLIC_KEY"))

    interface = GptInterface(  # create interface
        api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
    )

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_message(message: discord.Message):
        # ignore messages from the bot itself
        if message.author == client.user:
            return

        # translate
        prompt = f"If the following text is Chinese, translate it to English. If it is English, translate it to Chinese: {message.content}"
        translation = interface.say(prompt)

        # reply to original message
        await message.reply(f"{message.author.display_name}: {translation}")

    client.run(TOKEN)
