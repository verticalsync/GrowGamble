import misc.utils as utils
from misc.variables import *


class ProfileCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(aliases=["p"])
	async def profile(self, ctx: commands.Context, discord_user: discord.Member = None):
		discord_user = ctx.message.author if discord_user is None else discord_user
		user = database.get_user(discord_user.id)
		user_balance = user.get_balance()
		highest_balance = user.get_highest_balance()
		wagered = user.get_wagered()
		dirts, bgls, dls, wls = utils.parse_world_locks(user_balance)
		hdirts, hbgls, hdls, hwls = utils.parse_world_locks(highest_balance)
		wdirts, wbgls, wdls, wwls = utils.parse_world_locks(wagered)
		bal = utils.create_balance_message(dirts, bgls, dls, wls)
		hbal = utils.create_balance_message(hdirts, hbgls, hdls, hwls)
		wbal = utils.create_balance_message(wdirts, wbgls, wdls, wwls)

		embed = discord.Embed(title=f"Profile of {discord_user.name}#{discord_user.discriminator}", color=discord.Color.random())
		embed.add_field(name="Balance", value=f"{bal}", inline=False)
		embed.add_field(name="Highest Balance", value=f"{hbal}", inline=False)
		embed.add_field(name="Wagered", value=f"{wbal}", inline=False)
		await ctx.send(embed=embed)

async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(ProfileCommand(bot))
