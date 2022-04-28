from http.client import HTTPException
import discord
import platform
from discord.ext import commands
from topgg import Forbidden

class botinfo(commands.Cog):
    """Bot info and statistics"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bstats")
    async def bstats(self, ctx):
        """Get bot information."""
        embed = discord.Embed(name="Bot information", color = discord.Color.red())
        embed.add_field(name="**Discord Version:**", value= discord.__version__, inline=False)
        embed.add_field(name="**Python Version:**", value=platform.python_version(), inline=False)
        embed.add_field(name="**latency:**", value="{0}ms".format(round(self.bot.latency * 1000)), inline=False)
        embed.add_field(name="**Total members:**", value= len(set(self.bot.get_all_members())), inline=False)
        embed.add_field(name="**Total Guilds:**", value= len(self.bot.guilds), inline=False)
        try:
            await ctx.send(embed = embed)
        except HTTPException:
            return await ctx.send("Sorry failed to send an embed at the moment.")
        except Forbidden:
            return await ctx.send("Sorry I do not have the right permissions to send embeds.")
        
    @commands.command(name="invite")
    async def invite(self, ctx):
        """Invite the bot"""
        await ctx.send("You can invite me by pressing this link: <https://discord.com/api/oauth2/authorize?client_id=948699106333843466&permissions=1503707786454&scope=bot>")


def setup(bot):
    bot.add_cog(botinfo(bot))