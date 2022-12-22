import io
from misc.variables import *


class SqlCommand(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	@commands.is_owner()
	async def sql(self, ctx: commands.Context, *, sql: str):
		conn = database.conn
		cursor = conn.cursor()

		try:
			cursor.execute(sql)
			conn.commit()
		except Exception as e:
			embed = discord.Embed(title="SQL Command Error.", color=discord.Color.random())

			embed.add_field(name="Command", value=f"```sql\n{sql}```")
			embed.add_field(name="Error", value=f"```{e}```")
			await ctx.send(embed=embed)
			return

		try:
			out = cursor.fetchall()
		except Exception:
			out = "Failed to fetch any output, probably none."
		embed = discord.Embed(title="SQL Command Ran.", color=discord.Color.random())

		embed.add_field(name="Command", value=f"```sql\n{sql}```")
		file = discord.File(fp=io.StringIO(str(out)), filename='output.txt')
		await ctx.send(embed=embed, file=file)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(SqlCommand(bot))
