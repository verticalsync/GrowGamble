import misc.utils as utils

from misc.variables import *


class LeaderboardCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def leaderboard(self, ctx: commands.Context, lb: str = "balance"):
        lb = lb.lower()
        if lb not in ["balance", "highest_balance", "wagered"]:
            await ctx.send("Invalid leaderboard")
            return

        users = database.get_users()
        user_list = {}
        for user in users:
            uid = user.get_user_id()
            if lb == "balance":
                user_list[uid] = user.get_balance()
            elif lb == "highest_balance":
                user_list[uid] = user.get_highest_balance()
            elif lb == "wagered":
                user_list[uid] = user.get_wagered()

        sorted_balances = sorted(
            user_list.items(), key=lambda x: int(x[1]), reverse=True
        )

        embed = discord.Embed(
            title=f"Leaderboard for {lb}",
            description="These are the top 10 users.",
            color=discord.Color.random(),
        )
        players = 10
        if len(user_list) < 10:
            players = len(user_list)
        for x in range(players):
            user_id, balance = sorted_balances[x]
            dirts, bgls, dls, wls = utils.parse_world_locks(balance)
            balance_message = utils.create_balance_message(dirts, bgls, dls, wls)
            embed.add_field(
                name=f"#{x + 1}",
                value=f"<@{user_id}> with {balance_message}",
                inline=False,
            )

        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LeaderboardCommand(bot))
