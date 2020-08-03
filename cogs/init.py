import discord
from discord.ext import commands, tasks
from itertools import cycle

class Init(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.status = cycle(['Minecraft', 'Rocket League', 'League of Legends', 'Destiny 2', 'World of Warcraft', 'The Witcher 3: Wild Hunt', 'Fortnite', 'GTA V', 'Overwatch', 'Metal Gear', 'PlayerUnknown\'s Battlegrounds', 'Life is Strange', 'Escape from Tarkov', 'Tom Clancy\'s: The Division 2', 'Battlefield V', 'Star Wars Jedi: Fallen Order', 'Sekiro: Shadows Die Twice', 'Borderlands 3'])

	@commands.Cog.listener()
	async def on_ready(self):
		self.change_status.start()
		print('Bot is online as {0.user}.'.format(self.client))

	@tasks.loop(seconds=60)
	async def change_status(self):
		await self.client.change_presence(activity=discord.Game(next(self.status)))

def setup(client):
	client.add_cog(Init(client))