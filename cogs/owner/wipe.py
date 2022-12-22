from misc.variables import *


class WipeCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	@commands.is_owner()
	async def wipe(self, ctx: commands.Context, discord_user: discord.Member):
		user_id = discord_user.id
		user = database.get_user(user_id)
		user.wipe()
		embed = discord.Embed(title="GrowBot", description=f"{discord_user.mention} has been wiped successfully.", color=0x8080ff)
		await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(WipeCommand(bot))
