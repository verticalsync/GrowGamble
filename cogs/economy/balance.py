from misc.variables import *


class BalanceCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(aliases=["bal"])
	async def balance(self, ctx: commands.Context, discord_user: discord.Member = None):
		user_id = ctx.message.author.id if discord_user is None else discord_user.id
		user = database.get_user(user_id)
		user_balance = user.get_balance()
		bal = ""
		dirts = 0
		bgls = 0
		dls = 0
		wls = 0
		if user_balance < 0:
			user_balance = 0
		while user_balance != 0:
			if user_balance > 1999999:
				dirts += 2
				user_balance -= 2000000
			if user_balance > 19999:
				bgls += 2
				user_balance -= 20000
			elif user_balance > 199:
				dls += 2
				user_balance -= 200
			else:
				wls += 1
				user_balance -= 1

		if dirts != 0:
			bal += f"{dirts} {emojis['dirt']} "
		if bgls != 0:
			bal += f"{bgls} {emojis['blue_gem_lock']} "
		if dls != 0:
			bal += f"{dls} {emojis['diamond_lock']} "
		if wls != 0:
			bal += f"{wls} {emojis['world_lock']}"

		await ctx.send(
			f"{'You have' if discord_user is None else discord_user.name + ' has'} {bal if bal != '' else '0 ' + emojis['world_lock']} (raw: {user.get_balance()})")


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(BalanceCommand(bot))
