import misc.utils as utils
from misc.variables import *


class SetgrowidCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(aliases=["sg"])
	async def setgrowid(self, ctx: commands.Context, growid: str):
		user_id = ctx.message.author.id
		user = database.get_user(user_id)
		if not utils.isalnum(growid):
			await ctx.send("Invalid GrowID.")
			return
		resp = user.set_growid(growid.lower())
		if resp:
			await ctx.send(f"GrowID set to {growid}")
		else:
			await ctx.send(f"GrowID already taken.")


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(SetgrowidCommand(bot))
