import discord
from discord.ext import commands
import os

token = 'NjY0NDk2NzU4Njc1NzM0NTQw.XhYZBw.5oIXpJp7AyF5EojCN_QE4-NdQoY'

client = commands.Bot(command_prefix = '!')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)