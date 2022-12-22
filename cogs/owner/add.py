import misc.utils as utils
from misc.variables import *


class AddCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(aliases=["give"])
	@commands.is_owner()
	async def add(self, ctx: commands.Context, discord_user: discord.Member, amount: int):
		user_id = discord_user.id
		user = database.get_user(user_id)
		user.set_balance(user.get_balance() + amount)
		dirts, bgls, dls, wls = utils.parse_world_locks(amount)
		formatted = utils.create_balance_message(dirts, bgls, dls, wls)
		embed = discord.Embed(title="GrowBot", description=f"Added {formatted} to {discord_user.mention} successfully.", color=0x8080ff)
		await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(AddCommand(bot))
