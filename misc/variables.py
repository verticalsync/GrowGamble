import json
import discord
from misc.database import Database
from discord.ext import commands

with open("config.json", "r") as f:
	config = json.load(f)

database = Database("misc/database.db")

token = config["token"]
prefix = config["prefix"]
owner_ids = config["owners"]
intents = discord.Intents.all()

emojis = {
	"dirt": "<:dirt:1050806760090378290>",
	"blue_gem_lock": "<:blue_gem_lock:1050796279074136124>",
	"diamond_lock": "<:diamond_lock:1050796274623971368>",
	"world_lock": "<:world_lock:1050796280747667517>"
}

bot = commands.Bot(command_prefix=prefix, intents=intents, help_command=None, owner_ids=owner_ids)

