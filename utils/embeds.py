import discord

class JJKEmbeds:
    @staticmethod
    def success(title, description):
        """Standard success message (Blue/Cursed Energy theme)."""
        embed = discord.Embed(
            title=f"🌀 {title}",
            description=description,
            color=discord.Color.blue()
        )
        return embed

    @staticmethod
    def combat_log(npc_name, player_name, action, damage, is_black_flash=False):
        """Combat specific formatting."""
        color = discord.Color.red() if not is_black_flash else discord.Color.from_rgb(0, 0, 0)
        title = "✨ BLACK FLASH!" if is_black_flash else "⚔️ Combat Log"
        
        embed = discord.Embed(title=title, color=color)
        embed.add_field(name="Source", value=npc_name, inline=True)
        embed.add_field(name="Target", value=player_name, inline=True)
        embed.add_field(name="Action", value=f"**{action}**", inline=False)
        embed.add_field(name="Damage", value=f"**{damage}**", inline=True)
        return embed

    @staticmethod
    def profile(player_data):
        """The /profile embed logic."""
        embed = discord.Embed(
            title=f"⛩️ {player_data['name']}'s Profile",
            description=f"**Grade:** {player_data['grade']}",
            color=discord.Color.dark_purple()
        )
        embed.add_field(name="Level", value=player_data['level'], inline=True)
        embed.add_field(name="Money", value=f"¥{player_data['money']}", inline=True)
        embed.add_field(name="Stats", value=(
            f"❤️ HP: {player_data['stats']['current_hp']}/{player_data['stats']['max_hp']}\n"
            f"💠 CE: {player_data['stats']['current_ce']}/{player_data['stats']['max_ce']}\n"
            f"💥 DMG: {player_data['stats']['dmg']}"
        ), inline=False)
        return embed
      
