import discord
from database.connection import db

# Configuration for Auto-Ranking
RANKS = {
    1: "Grade 4 Sorcerer",
    15: "Grade 3 Sorcerer",
    30: "Grade 2 Sorcerer",
    50: "Grade 1 Sorcerer",
    80: "Special Grade Sorcerer"
}

async def add_xp(user_id, guild, amount):
    """Adds XP and handles Auto-Role Ranking."""
    player = await db.players.find_one({"_id": str(user_id)})
    if not player:
        return

    new_xp = player["xp"] + amount
    # Simple level formula: Level * 100 XP
    needed_xp = player["level"] * 100
    
    if new_xp >= needed_xp:
        new_level = player["level"] + 1
        new_stat_points = player["stat_points"] + 5
        
        # Check for Grade Promotion
        new_grade = player["grade"]
        if new_level in RANKS:
            new_grade = RANKS[new_level]
            await update_discord_role(guild, user_id, new_grade)

        await db.players.update_one(
            {"_id": str(user_id)},
            {"$set": {"xp": 0, "level": new_level, "grade": new_grade}, 
             "$inc": {"stat_points": 5}}
        )
        return {"level_up": True, "level": new_level, "grade": new_grade}
    
    await db.players.update_one({"_id": str(user_id)}, {"$set": {"xp": new_xp}})
    return {"level_up": False}

async def update_discord_role(guild, user_id, grade_name):
    """Auto-creates and gives the grade role to the player."""
    member = guild.get_member(int(user_id))
    if not member:
        return

    # Find or create the role
    role = discord.utils.get(guild.roles, name=grade_name)
    if not role:
        role = await guild.create_role(name=grade_name, color=discord.Color.gold())

    # Remove old grade roles
    old_roles = [r for r in member.roles if "Sorcerer" in r.name]
    await member.remove_roles(*old_roles)
    await member.add_roles(role)
  
