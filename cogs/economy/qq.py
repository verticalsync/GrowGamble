import secrets
import misc.utils as utils
from misc.variables import *


class QQCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	async def qq(self, ctx: commands.Context, amount: int):
		user_id = ctx.author.id
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

		win = False
		tie = False
		you = str(secrets.randbelow(37))
		you_qq = 0
		dealer = str(secrets.randbelow(37))
		dealer_qq = 0

		if len(you) == 2:
			you_qq = int(you[1])
		else:
			you_qq = int(you)

		if len(dealer) == 2:
			dealer_qq = int(dealer[1])
		else:
			dealer_qq = int(dealer)

		if dealer_qq > you_qq:
			win = False
		if dealer_qq < you_qq:
			win = True

		if dealer_qq == 0:
			win = False
		if you_qq == 0:
			win = True

		if dealer_qq == you_qq:
			tie = True

		user.set_wagered(user.get_wagered() + amount)

		if tie:
			embed = discord.Embed(title="Tied!",
				description="You and the dealer have tied, no balances have been modified.",
				color=discord.Color.yellow(), )
			embed.add_field(name="You", value=f"rolled {you}")
			embed.add_field(name="Dealer", value=f"rolled {dealer}")
			await ctx.send(embed=embed)
			return

		if win:
			user.set_balance(user.get_balance() + amount)
		else:
			user.set_balance(user.get_balance() - amount)

		dirts, bgls, dls, wls = utils.parse_world_locks(amount)
		formatted = utils.create_balance_message(dirts, bgls, dls, wls)

		embed = discord.Embed(title="Win" if win else "Lose", description=f"You {'won ' + formatted if win else 'lost ' + formatted}",
			color=discord.Color.green() if win else discord.Color.red())
		embed.add_field(name="You", value=f"rolled {you}")
		embed.add_field(name="Dealer", value=f"rolled {dealer}")
		await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(QQCommand(bot))
