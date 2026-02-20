import discord
from discord.ext import commands
from systems.combat_engine import active_combats

def is_admin():
    """Simple check for server administrators."""
    async def predicate(ctx):
        return ctx.author.guild_permissions.administrator
    return commands.check(predicate)

def not_in_combat():
    """Prevents users from swapping gear (!equip) while fighting."""
    async def predicate(ctx):
        if ctx.channel.id in active_combats:
            await ctx.send("❌ You cannot change your loadout during active combat!", delete_after=5)
            return False
        return True
    return commands.check(predicate)
  
