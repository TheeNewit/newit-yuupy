from discord.ext import commands
from utils.utils import color_hex_to_int, get_emote_url, get_first_name
import discord
import json
import random
import time


class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.pings = ['Pang', 'Peng', 'Pong', 'Pung']
        self.endings = ['Perfect', 'Good', 'Bad', 'Worst']
        with open('assets/routes.json', 'r', encoding='utf-8') as raw_routes:
            self.routes = json.load(raw_routes)

    @commands.command()
    async def ping(self, ctx: commands.Context):
        curr = time.time()
        latency: float = round(ctx.bot.latency * 1000.0, 2)
        msg = await ctx.send('Pinging... 🏓')
        await msg.edit(
            content=f'🏓 {random.choice(self.pings)}! Latency is {round((time.time() - curr) * 1000.0, 2)}ms. API latency is {latency}ms.')

    @commands.command()
    async def route(self, ctx: commands.Context):
        author: discord.Member = ctx.author
        route = random.choice(self.routes)
        ending = random.choice(self.endings)
        embed = discord.Embed(title=f'Next: {route["name"]}, {ending} Ending',
                              color=color_hex_to_int(route["color"]),
                              description=f"{route['description']}") \
            .set_author(name=author.display_name, icon_url=author.avatar_url) \
            .set_thumbnail(url=get_emote_url(route['emoteId'], 'gif')) \
            .add_field(name="Age", value=route["age"], inline=True) \
            .add_field(name="Birthday", value=route["birthday"], inline=True) \
            .add_field(name="Animal Motif", value=route["animal"], inline=True) \
            .set_footer(text=f"Play {get_first_name(route['name'])}'s route next. All bois are best bois.")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Info(bot))
