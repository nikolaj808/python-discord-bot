import discord
from discord.ext import commands
import random
import re

class Games(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.epstein = re.compile("[eE][pP][sS][tT][eE][iI][nN]")

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author != self.client.user:
			channel = message.channel
			print('{} said: {} (in channel: {})'.format(message.author, message.content, channel))
			if message.content == 'What is love?':
				await channel.send('Baby don\'t hurt me..')
			elif self.epstein.search(message.content):
				await channel.send('Epstein didn\'t kill himself!')

	@commands.command(aliases=['8ball'])
	async def _8ball(self, ctx, *, question):
		responses = ['It is certain.',
		'It is decidedly so.',
		'Without a doubt.',
		'Yes - definitely.',
		'You may rely on it.',
		'As I see it, yes.',
		'Most likely.',
		'Outlook good.',
		'Yes.',
		'Signs point to yes.',
		'Reply hazy, try again.',
		'Ask again later.',
		'Better not tell you now.',
		'Cannot predict now.',
		'Concentrate and ask again.',
		'Don\'t count on it.',
		'My reply is no.',
		'My sources say no.',
		'Outlook not so good.',
		'Very doubtful.']

		await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(client):
	client.add_cog(Games(client))