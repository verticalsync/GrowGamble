import os
import misc.logger as logger
import misc.tasks as tasks
from misc.variables import *

first_run = True


@bot.event
async def on_ready():
	global first_run

	if first_run:
		for filename in os.listdir("./cogs"):
			for file in os.listdir(f"./cogs/{filename}"):
				if filename.endswith("__") or file.endswith("__"):
					continue
				await bot.load_extension(f"cogs.{filename}.{file[:-3]}")
				logger.info(f"Loaded command cog: {filename}.{file[:-3]}", __name__)

	logger.info(f"Logged in as {bot.user} in {len(bot.guilds)} guild(s).", __name__)

	if first_run:
		tasks.status_loop.start()
		tasks.jackpot_check.start()

	first_run = False


@bot.event
async def on_command_error(ctx: commands.Context, error):
	if isinstance(error, commands.NotOwner):
		await ctx.send("You're not in the list of owners.")
	elif isinstance(error, commands.CommandNotFound):
		return
	else:
		await ctx.send(error)


@bot.event
async def on_message(message: discord.Message):
	if message.author.id == 1050214270727618600:
		content = message.content.replace(" ", "")
		deposit_logs = bot.get_channel(1050218323658412133)
		split = content.split(":")
		author = split[0].lower()
		item = split[1]
		amount = int(split[2])
		if item not in ["WorldLock", "DiamondLock", "BlueGemLock"]:
			return
		multiplier = 1
		if item == "DiamondLock":
			multiplier = 100
		elif item == "BlueGemLock":
			multiplier = 10000
		user = database.get_user_by_growid(author)
		if user:
			balance = user.get_balance()
			new_balance = balance + (amount * multiplier)
			user.set_balance(new_balance)
			await message.channel.send(f"user {author} is linked to <@{user.get_user_id()}>, user has deposited {amount * multiplier} world locks")
			await deposit_logs.send(f"<@{user.get_user_id()}> has deposited {amount * multiplier} world locks, their balance has been updated from {balance} to {new_balance}")
			return
		await message.channel.send(f"{author} is not linked to any account.")

	await bot.process_commands(message)


bot.run(token)
