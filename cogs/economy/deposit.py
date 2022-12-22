import discord
from discord.ext import commands


class DepositCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	async def deposit(self, ctx: commands.Context):
		embed = discord.Embed(title="Growbot", description="If you want to deposit create a ticket at <#1050207046819135549>", color=0x8080ff)
		await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(DepositCommand(bot))
