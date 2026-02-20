def player_document(user_id, username):
    """Template for new sorcerers."""
    return {
        "_id": str(user_id),
        "name": username,
        "level": 1,
        "xp": 0,
        "grade": "Grade 4 Sorcerer",
        "money": 0,
        "stat_points": 0,
        "stats": {
            "max_hp": 100,
            "current_hp": 100,
            "max_ce": 50,
            "current_ce": 50,
            "dmg": 10
        },
        "loadout": {
            "technique": None,
            "weapon": None,
            "fighting_style": "Basic Brawling"
        },
        "inventory": [],
        "mastery": {},  # {"SkillName": XP_Amount}
        "vows": []
    }

def npc_document(name, is_boss, hp, dmg, image_url):
    """Template for NPCs created via /npc create."""
    return {
        "name": name,
        "is_boss": is_boss,
        "image_url": image_url,
        "hp": hp,
        "base_dmg": dmg,
        "moveset": {
            "technique": None, 
            "weapon": None, 
            "fighting_style": None
        },
        "drops": [], # List of {"item": str, "chance": float}
        "money_range": [0, 0],
        "mastery_reward": 0,
        "ping_role": None,
        "spawn_channels": []
    }
  
