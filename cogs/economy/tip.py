from misc.variables import *


class TipCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	async def tip(self, ctx: commands.Context, discord_user: discord.Member, amount: int):
		user_id = ctx.author.id
		target_user_id = discord_user.id
		user = database.get_user(user_id)
		target_user = database.get_user(target_user_id)

		if user_id == target_user_id:
			await ctx.send("Can't tip yourself.")
			return

		if amount < 1:
			await ctx.send("Can't tip below 1")
			return

		if user.get_balance() <= amount:
			await ctx.send("Not enough world locks to tip.")
			return

		user.set_balance(user.get_balance() - amount)
		target_user.set_balance(target_user.get_balance() + amount)
		await ctx.send(f"You've tipped {discord_user.name} {amount} of world locks")


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(TipCommand(bot))
