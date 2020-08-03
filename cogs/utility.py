import discord
from discord.ext import commands

class Utility(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def clear(self, ctx, amount=5):
		await ctx.channel.purge(limit=amount)

	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong! Response time: {round(self.client.latency * 1000)} ms')

def setup(client):
	client.add_cog(Utility(client))