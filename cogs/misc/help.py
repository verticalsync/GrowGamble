import discord
from discord.ext import commands


class HelpCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx: commands.Context):
		embed = discord.Embed(title="Growbot", color=0x8080ff)
		embed.add_field(name="Commands", value="""() optional | <> required

		prefix is .

		commands:
		.setgrowid <growid> - you should use this when depositing, set it to the accounts username that you'll deposit with.
		.balance (user) - shows your balance, shows another users balance if provided.
		.tip <user> <amount> - tip the specified user the specified amount of world locks.
		.bet <amount> <choice> - number has to be from 1 to 3 if the bot gets the same number you picked, your amount will be doubled
		.qq <amount> - Play QQ, how it works: if you get a double number the first number doesnt count only the last one does, highest one wins and if 0 = auto win, if single letter same rules apply""")
		await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(HelpCommand(bot))
