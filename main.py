import discord
from discord.ext import commands
import os


prefix = '>'#تعديل مهم حط البرفكس حقكك
client = commands.Bot(command_prefix= f"{prefix}")
client.remove_command('help')





from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')

@client.command()
async def ping(ctx,  member:discord.Member = None):
  member = member if member else ctx.author
  embed = discord.Embed(description=f'**pong! {round(client.latency * 1000)}ms**',
  color=0x00ff00 ,
  timestamp=ctx.message.created_at
  )
  embed.set_author(name=f'{client.user.display_name}#{client.user.discriminator}', icon_url=client.user.avatar_url)
  embed.set_thumbnail(url=member.avatar_url)
  embed.set_footer(text=f'{member.display_name} ', icon_url=member.avatar_url)  
  await ctx.send(embed=embed)

@client.command(aliases=['id'])
async def userinfo(ctx, member: discord.Member = None):
  member = member if member else ctx.author #!                 "Wåň"; "핏기 없는"#0090
  roles = [role for role in member.roles]
  embed = discord.Embed(colour=member.color,timestamp=ctx.message.created_at,
  description = f'👤 | **user**: {member.mention}' #!                 "Wåň"; "핏기 없는"#0090

)
  embed.set_author(name=f"user info - {member}")
  embed.set_thumbnail(url=member.avatar_url) #!                 "Wåň"; "핏기 없는"#0090
  #embed.set_footer=(text=f"requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  embed.add_field(name="🆔 | id: ",value=member.id)
  embed.add_field(name="📛 | guild name: ", value=member.display_name)
  embed.add_field(name='👏 | created at: ', value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
  embed.add_field(name='😍 | joined at: ', value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")) #!                 "Wåň"; "핏기 없는"#0090

  embed.add_field(name=f'👮‍♂️ | roles ({len(roles)})', value=" ".join([role.mention for role in roles]))

  embed.add_field(name='🏅 | top role: ', value=member.top_role.mention)
  embed.add_field(name="🤖 | bot?", value=member.bot)

  await ctx.send(embed=embed) #!                 "Wåň"; "핏기 없는"#0090

#جميع الحقوق محفوضه !                 "Wåň"; "핏기 없는"#0090
client.remove_command('help')
prefix = ">" # تعديل مهم حط برفكس بوتك
@client.command()
async def help(ctx):
    help = discord.Embed(title="Help List",
    description=f"""**
    {prefix}Ping => To Know The Bot Response
    
    {prefix}id => To get information about anyone
    
    {prefix}invite => gives you invite link of the BOT

    {prefix}serverinfo => Get info about the server
    
    {prefix}kick => kick selected member

    {prefix}ban => ban selected member
    
    {prefix}say => make bot say what you want requires 'manage_messages' permission
    **""",
    color=0x00ff00)
    await ctx.send(embed=help)
@client.event
async def on_command_error(ctx, error):
 await ctx.channel.purge(limit=1)

 emebd = discord.Embed(description=f'{client.command_prefix}help ({error}) :x:')


 await ctx.send(embed=emebd)
 await ctx.sleep(5)
 await ctx.channel.purge(limit=1)
@client.command()
async def invite(ctx):
  embed = discord.Embed(
    description='''**invite => [invite bot](https://discord.com/oauth2/authorize?client_id={}&scope=bot&permissions=2146958847)**
**support => [<@743060751220080730>]({})**'''.format(client.user.id, 'INVITE LINK'))
  await ctx.send(embed=embed)
@client.command()
async def serverinfo(ctx):
    embed = discord.Embed(title='server info')
    embed.add_field(name='Name', value=ctx.guild.name)
    embed.add_field(name='guild id', value=ctx.guild.id)
    embed.add_field(name='Owner', value=ctx.guild.owner)
    embed.add_field(name='Members', value=ctx.guild.member_count)
    embed.add_field(name='region', value=ctx.guild.region)
    embed.add_field(name='afk channel', value=ctx.guild.afk_channel)
    embed.add_field(name='afk timeout', value=ctx.guild.afk_timeout)
    embed.add_field(name='max presences', value=ctx.guild.max_presences)
    embed.add_field(name='description', value=ctx.guild.description)
    embed.add_field(name='verification level', value=ctx.guild.verification_level)
    embed.add_field(name='premium tier', value=ctx.guild.premium_tier)
    embed.add_field(name='premium subscription count', value=ctx.guild.premium_subscription_count)
    embed.add_field(name='channels', value=len(ctx.guild.channels))
    embed.add_field(name='voice channels', value=len(ctx.guild.voice_channels))
    embed.add_field(name='text channels', value=len(ctx.guild.text_channels))
    embed.add_field(name='system channel', value=ctx.guild.system_channel)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_author(name='server', icon_url=ctx.guild.icon_url)
    embed.set_footer(text='made by Makenone', icon_url='')
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('🔒C | hannel locked {}'.format(channel.mention))
@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('🔓C | hannel unlocked {}'.format(channel.mention))            
@client.event
async def on_ready():
    activity = discord.Streaming(name=f"{client.command_prefix}help",url='https://twitch.tv/makenonee', type=1)
    await client.change_presence(status=discord.Status.dnd, activity=activity)
    print("I'am ready")
    print('Please wait a few seconds')
    print("================")
    print(f"""my name : {client.user.name} 
my id : {client.user.id}
my tag : {client.user.discriminator}
my prefix : {prefix}
================""")
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
    await ctx.send(" Successfully Banned" + member.name + " ✅ ")
    await member.ban(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):

            await ctx.guild.unban(user)
            await ctx.send("Successfully UnBanned" + member.name + " ✅ ")
            return

        await ctx.send(member+"User dosent exists")
@client.command()
@commands.has_permissions(kick_members=True)
async def kick (ctx,member : discord.Member,*,reason= "No reason provided"):
    await ctx.send(" Successfully Kicked " + member.name + " ✅ ")
    await member.kick(reason=reason)
@client.command()
async def sug(ctx,* , sugg):
  channel = client.get_channel(756054951335297024) # id channel
  await ctx.channel.purge(limit=1)
  embed = discord.Embed(title='New Suggestion By {}'.format(ctx.author.display_name))
  embed.add_field(name='Suggestion: ', value=sugg)
  embed.set_footer(text='UserID: ( {} ) | sID: ( {} )'.format(ctx.author.id, ctx.author.display_name), icon_url=ctx.author.avatar_url)
  await ctx.send('☑️ Your Suggestion Has Been Sent To <#{}> !'.format(channel.id))
  suggg = await channel.send(embed=embed)
  await suggg.add_reaction('👍')
  await suggg.add_reaction('👎')
@sug.error
async def sug_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.channel.purge(limit=1)
      await ctx.send('**Please Type Your Suggestion!**')       
@client.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx,*,arg, amount=1):
  await ctx.channel.purge(limit=amount)
  await ctx.send(arg)
@commands.has_permissions(manage_messages=True)
@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You Must type words next the command "say" to make bot say it')
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send("Error Missing permissions `manage_messages`")  
  
client.run(TOKEN)


#بتسوي ملف اسمه .env و حط بيه TOKEN=توكن بوتك
#اذا ما بتستخدم استضافه مجانيه احذف كلمه TOKEN من اخر كود و حط client.run('توكن بوتك')
#و اذا بتحب تحمل برنامج البايثون https://youtu.be/WTRKeSoynKI 