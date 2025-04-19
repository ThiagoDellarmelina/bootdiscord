import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

client = commands.Bot(command_prefix="__", intents=intents)

@client.event
async def on_ready():
    print(f"🤖 Bot conectado como {client.user.name}")

# Carregando Opus
try:
    if not discord.opus.is_loaded():
        discord.opus.load_opus("libopus-0.dll")
        print("✅ Opus carregado manualmente com libopus-0.dll.")
    else:
        print("🎤 OPUS LOADED:", discord.opus.is_loaded())
except Exception as e:
    print(f"❌ Falha ao carregar Opus: {e}")

# Carregando extensões
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            name = f"cogs.{filename[:-3]}"
            try:
                await client.load_extension(name)
                print(f"✅ Cog carregado: {filename}")
            except Exception as e:
                print(f"❌ Erro ao carregar cog '{filename}': {e}")

async def main():
    await load_extensions()
    await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
