import secrets
import misc.utils as utils
from misc.variables import *


class JackpotCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		self.channel = self.bot.get_channel(1052968063978459137)

	@commands.command()
	async def jackpot(self, ctx: commands.Context, amount: int):
		user_id = ctx.message.author.id
		user = database.get_user(user_id)

		if amount > 2000000:
			await ctx.send(f"You can't enter jackpot with more than 200 {emojis['blue_gem_lock']}")
			return
		if user.get_balance() < amount:
			missing = amount - user.get_balance()
			dirts, bgls, dls, wls = utils.parse_world_locks(missing)
			formatted = utils.create_balance_message(dirts, bgls, dls, wls)
			await ctx.send(f"You're tad short of {formatted}")
			return
		if amount < 1:
			await ctx.send(f"Can't join jackpot with anything below 1.")
			return



async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(JackpotCommand(bot))
