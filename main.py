import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class JJKBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True  # Required for !CE, !F, !W commands
        intents.members = True          # Required for Auto-Ranking/Roles
        
        super().__init__(
            command_prefix="!", 
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        print("--- Initializing Jujutsu Systems ---")
        
        # Load Cogs from the cogs/ folder
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    print(f"✅ Loaded Cog: {filename}")
                except Exception as e:
                    print(f"❌ Failed to load {filename}: {e}")
        
        # Sync Slash Commands
        await self.tree.sync()
        print("⚡ Slash Commands Synced")

    async def on_ready(self):
        print(f"🔥 Logged in as {self.user} (ID: {self.user.id})")
        print("--- Sorcerer Database Connected ---")

if __name__ == "__main__":
    bot = JJKBot()
    bot.run(os.getenv("DISCORD_TOKEN"))
  
