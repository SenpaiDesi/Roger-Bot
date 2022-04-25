import discord
from discord.ext import commands
import platform


class fun(commands.Cog):
    """Fun commands to mess around with."""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = "say")
    async def say (self, ctx, *, message):
        """Repeats your message"""
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{message} ~{ctx.author.display_name}")
    


    @commands.command()
    async def whois(self, ctx, *, user: discord.Member = None):
        """Check to see who this person is, their roles and other stuff. format: whois @user"""
        if user is None:
            user = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=discord.Color.orange(), description=user.mention)
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="Join position", value=str(members.index(user) + 1))
        embed.add_field(name="Registered", value=user.created_at.strftime(date_format))

        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
            embed.set_footer(text='ID: ' + str(user.id))
            return await ctx.send(embed=embed)
        else:
            embed.add_field(name="Roles:", value="None")
        return await ctx.send(embed=embed)

    @commands.command(name='av', aliases=['pfp'])
    @commands.has_permissions(add_reactions=True)
    async def av(self, ctx, user: discord.Member = None):
        """Show the avatar of an user. Format: av @user"""
        if user != None:
            await ctx.send(user.avatar_url)
        else:
            await ctx.send(ctx.author.avatar_url)

    @commands.command()
    @commands.has_permissions(add_reactions=True)
    async def bstats(self, ctx):
        """Command to check a few bot statistics."""
        python_version = platform.python_version()
        discord_py_version = discord.__version__
        total_guilds = len(self.bot.guilds)
        total_members = len(set(self.bot.get_all_members()))
        embed = discord.Embed(name='Bot stats', color=discord.Color.red())
        embed.set_author(name='Roger bot')
        embed.add_field(name='**Python Version:**', value=python_version, inline=False)
        embed.add_field(name='**Library Version:**', value=discord_py_version, inline=False)
        embed.add_field(name='**Server Count:**', value=str(total_guilds), inline=False)
        embed.add_field(name='**Total Members:**', value=str(total_members), inline=False)
        await ctx.send(embed=embed)










def setup(bot):
    bot.add_cog(fun(bot))