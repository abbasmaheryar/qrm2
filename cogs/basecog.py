"""
Base cog for qrm
---
Copyright (C) 2019 Abigail Gold, 0x5c

This file is part of discord-qrmbot and is released under the terms of the GNU
General Public License, version 2.
"""

import discord
import discord.ext.commands as commands

import os

class BaseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gs = bot.get_cog("GlobalSettings")

    @commands.command(name="info", aliases=["about"])
    async def _info(self, ctx):
        """Shows info about qrm."""
        embed = discord.Embed(title="About qrm", description=self.gs.info.description, colour=self.gs.colours.neutral)
        embed = embed.add_field(name="Authors", value=", ".join(self.gs.info.authors))
        embed = embed.add_field(name="Contributing", value=self.gs.info.contributing)
        embed = embed.add_field(name="License", value=self.gs.info.license)
        await ctx.send(embed=embed)

    @commands.command(name="restart")
    async def _restart_bot(self, ctx):
        """Restarts the bot."""
        if ctx.author.id in self.gs.opt.owners_uids:
            await ctx.message.add_reaction("✅")
            await self.bot.logout()
        else:
            try:
                await ctx.message.add_reaction("❌")
            except:
                return

    @commands.command(name="shutdown")
    async def _shutdown_bot(self, ctx):
        """Shuts down the bot."""
        if ctx.author.id in self.gs.opt.owners_uids:
            await ctx.message.add_reaction("✅")
            os._exit(42)
        else:
            try:
                await ctx.message.add_reaction("❌")
            except:
                return

    @commands.command(name="ping")
    async def _ping(self, ctx):
        await ctx.send(f'**Pong!** Current ping is {self.bot.latency*1000:.1f} ms')


def setup(bot):
    bot.add_cog(BaseCog(bot))
