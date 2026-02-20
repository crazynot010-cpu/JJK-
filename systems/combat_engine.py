import random
import asyncio
from database.connection import db

# Global combat state to track active fights
# Format: {channel_id: {"boss_id": id, "players": {user_id: dmg}, "variance": 1.0}}
active_combats = {}

async def calculate_variance(channel_id):
    """The 12-13 second loop that shifts Boss damage by 1-3%."""
    while channel_id in active_combats:
        await asyncio.sleep(random.randint(12, 13))
        if channel_id in active_combats:
            # Shift variance between 0.97 (-3%) and 1.03 (+3%)
            new_var = random.uniform(0.97, 1.03)
            active_combats[channel_id]["variance"] = new_var

async def npc_auto_attack_loop(ctx, npc_data):
    """The automated attack loop for NPCs and Bosses."""
    channel_id = ctx.channel.id
    
    # Initialize Combat Entry
    active_combats[channel_id] = {
        "npc": npc_data,
        "players": {}, 
        "variance": 1.0
    }
    
    # Start the Variance background task
    if npc_data.get("is_boss"):
        asyncio.create_task(calculate_variance(channel_id))

    while channel_id in active_combats:
        # Attack Speed: Boss = 5s, Normal = 8s
        wait_time = 5 if npc_data.get("is_boss") else 8
        await asyncio.sleep(wait_time)

        combat_data = active_combats.get(channel_id)
        if not combat_data or not combat_data["players"]:
            continue

        # Aggro Logic: Target the player who dealt the most damage
        target_id = max(combat_data["players"], key=combat_data["players"].get)
        target = ctx.guild.get_member(int(target_id))

        if not target:
            continue

        # Damage Logic
        base_dmg = npc_data["base_dmg"]
        final_dmg = int(base_dmg * combat_data["variance"])
        
        # In a real scenario, we'd subtract from player HP here
        await ctx.send(f"💢 **{npc_data['name']}** attacks <@{target_id}> for **{final_dmg}** DMG!")

async def check_black_flash():
    """2.5% chance for Black Flash (Damage^2.5)"""
    return random.random() < 0.025
  
