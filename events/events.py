from turtle import title
from discord.ext import commands 
import discord


class events (commands.Cog):
    """Event manager, does not contain commands."""
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after,):
        channel = self.bot.get_channel(940352961299750922)
        if message_before.author.id == self.bot.user.id:
            return
        else:
            embed = discord.Embed(title=f"{message_before.author.name} Edited a message", color = discord.Color.orange())
            embed.add_field(name="Was", value=message_before.content)
            embed.add_field(name="Is", value=message_after.content)
            try:
                await channel.send(embed = embed)
            except discord.errors.Forbidden:
                pass
            except Exception as e:
                print(e + "\n")
    
    @commands.Cog.listener()
    async def on_message_delete(self, message_before):
        channel = self.bot.get_channel(940352961299750922)
        if message_before.author.id == self.bot.user.id:
            return
        else:
            embed = discord.Embed(title=f'{message_before.author.name}#{message_before.author.discriminator} Deleted a message in #{message_before.channel.name}', color = discord.Color.red())
            embed.add_field(name="Was:", value=message_before.content)
            embed.set_footer(text = f"Author: {message_before.author.id}")
            try:
                await channel.send(embed = embed)
            except discord.errors.Forbidden:
                pass
            except Exception as e:
                print(e + "\n")





def setup(bot):
    bot.add_cog(events(bot))
        











