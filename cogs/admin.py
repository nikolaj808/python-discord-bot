import discord
from discord.ext import commands

class Admin(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def kick(self, ctx, member : discord.Member, *, reason=None):
		await member.kick(reason=reason)
		await ctx.send(f'{member.mention} has been kicked.')

	@commands.command()
	async def ban(self, ctx, member : discord.Member, *, reason=None):
		await member.ban(reason=reason)
		await ctx.send(f'{member.mention} has been banned.')

	@commands.command()
	async def unban(self, ctx, *, member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')
		for ban_entry in banned_users:
			user = ban_entry.user
			if (user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f'{user.mention} has been unbanned.')
				return

	@commands.command()
	async def load(self, ctx, extension):
		self.client.load_extension(f'cogs.{extension}')

	@commands.command()
	async def unload(self, ctx, extension):
		self.client.unload_extension(f'cogs.{extension}')

	@commands.command()
	async def reload(self, ctx, extension):
		self.client.unload_extension(f'cogs.{extension}')
		self.client.load_extension(f'cogs.{extension}')

	@commands.command()
	async def yeet(self, ctx):
		#channel_from = discord.utils.get(ctx.guild.voice_channels)
		#channel_to = discord.utils.get(ctx.guild.voice_channels, name='Testing')
		member = ctx.guild.voice_channels[0].members[0]


		await member.move_to(ctx.guild.voice_channels[1], reason='Just a test')


def setup(client):
	client.add_cog(Admin(client))