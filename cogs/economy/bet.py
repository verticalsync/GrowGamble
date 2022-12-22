import secrets
import misc.utils as utils
from misc.variables import *


class BetCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	async def bet(self, ctx: commands.Context, amount: int, choice: int):
		user_id = ctx.message.author.id
		user = database.get_user(user_id)

		if amount > 2000000:
			await ctx.send(f"You can't bet more than 200 {emojis['blue_gem_lock']}")
			return
		if user.get_balance() < amount:
			missing = amount - user.get_balance()
			dirts, bgls, dls, wls = utils.parse_world_locks(missing)
			formatted = utils.create_balance_message(dirts, bgls, dls, wls)
			await ctx.send(f"You're tad short of {formatted}")
			return
		if amount < 1:
			await ctx.send(f"Can't bet below 1.")
			return
		if choice < 1 or choice > 3:
			await ctx.send(f"Choice cannot be below 1 or higher than 3")
			return

		result = secrets.randbelow(3) + 1

		win = True if result == choice else False

		user.set_wagered(user.get_wagered() + amount)

		if win:
			user.set_balance(user.get_balance() + amount)
		else:
			user.set_balance(user.get_balance() - amount)

		dirts, bgls, dls, wls = utils.parse_world_locks(amount)
		formatted = utils.create_balance_message(dirts, bgls, dls, wls)

		embed = discord.Embed(title="Win" if win else "Lose", description=f"You {'won ' + formatted if win else 'lost ' + formatted}",
			color=discord.Color.green() if win else discord.Color.red())
		embed.add_field(name="You", value=f"rolled {choice}")
		embed.add_field(name="Dealer", value=f"rolled {result}")
		await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(BetCommand(bot))
