from misc.variables import *


class PurgeCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def purge(self, ctx: commands.Context, amount: int):
		await ctx.channel.purge(limit=amount)
		await ctx.send(f"Purged {amount} messages", delete_after=3)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(PurgeCommand(bot))
