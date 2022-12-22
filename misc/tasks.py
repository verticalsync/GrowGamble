from discord.ext import tasks

from misc.variables import *


@tasks.loop(minutes=1)
async def status_loop():
	members = [member for member in bot.get_all_members() if not member.bot]

	activity = discord.Activity(
		type=discord.ActivityType.competing,
		name=f"with {len(members)} users")
	await bot.change_presence(activity=activity)

@tasks.loop(seconds=30)
async def jackpot_check():
	pass
