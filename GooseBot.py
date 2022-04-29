import nextcord
from nextcord.ext import commands

PREFIX = '.'

client = commands.Bot( command_prefix = PREFIX )
client.remove_command('help')
client.remove_command('info')


@client.event

async def on_ready():
	print('Бот запустилься!')

	await client.change_presence(status = nextcord.Status.online, activity = nextcord.Game(".help"))

# Clear Message
@client.command(pass_context = True )
@commands.has_permissions(administrator = True)
async def clear( ctx, amount = 100):
	await ctx.channel.purge( limit = amount )


#Kick
@client.command(pass_context = True )
@commands.has_permissions( administrator = True )

async def kick(ctx,member: nextcord.Member, *, reason = None):
	await ctx.channel.purge(limit = 1)

	await member.kick(reason = reason)
	await ctx.send(f"Юзер {member.mention} Успешно был кикнут с причиной {reason}!")

	#Ban
@client.command( pass_context = True )
@commands.has_permissions(administrator = True)

async def ban(ctx, member: nextcord.Member, *, reason = None):
	await ctx.channel.purge(limit = 1)

	await member.ban(reason = reason)
	await ctx.send(f"Юзер {member.mention} Успешно был забанен с причиной {reason}!")

#Unban
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def unban(ctx, *, member):
	await ctx.channel.purge(limit = 1)

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban(user)
		await ctx.send(f"Юзер {user.mention} Успешно был разбанен!")

		return

#Help
@client.command(pass_context = True)

async def help(ctx):
	emb = nextcord.Embed(title = 'Навигация по командам', colour = nextcord.Color.purple())

	emb.add_field(name = '{}clear'.format(PREFIX), value ="Очистка чата.")
	emb.add_field(name = '{}kick'.format(PREFIX), value ="Кикает участника сервера.")
	emb.add_field(name = '{}ban'.format(PREFIX), value ="Банит участника сервера.")
	emb.add_field(name = '{}unban'.format(PREFIX), value ="Разбанивает участника сервера.")
	emb.add_field(name = '{}mute'.format(PREFIX), value ="Замутить участника сервера.")
	emb.add_field(name = '{}unmute'.format(PREFIX), value ="Размутить участника сервера.")
	emb.add_field(name = 'Создатель'.format(PREFIX), value ="Меня создал один человек и его дискорд : Киритас#6666.")
	await ctx.send(embed = emb)

#Mute
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def mute(ctx,member: nextcord.Member,):
	await ctx.channel.purge(limit = 1)

	mute_role = nextcord.utils.get(ctx.message.guild.roles, name = "MUTE")

	await member.add_roles(mute_role)
	await ctx.send(f"Юзер {member.mention} Успешно был замьючен!")

#Unmute
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def unmute(ctx,member: nextcord.Member,):
	await ctx.channel.purge(limit = 1)

	unmute_role = nextcord.utils.get(ctx.message.guild.roles, name = "MUTE")

	await member.remove_roles(unmute_role)
	await ctx.send(f"Юзер {member.mention} Успешно был размьючен!")

	# Connect

client.run ('ODkzMDg4NTk5OTA0NDg5NDky.G24AjW.o6yrLjbranjo434BYtlqCXZSiewR0Cyt3Qo7Nw')
