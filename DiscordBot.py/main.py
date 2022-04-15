import discord 
import datetime
from discord.ext import commands
from discord.ext.commands import guild_only
import json
client = commands.Bot(command_prefix = ".")

## Needs improvement for typing commands only in this channel 
Command_Channel = client.get_channel(526716659290079232)

## Permission for using the bot 
Permisions_id = client.get_user(526716659290079232)

## Command for printing a message when the bot is activated
@client.event
async def on_ready():
    TimeOfDay = datetime.datetime.now()
    print("Bot is Online.")
    print("DATE:",TimeOfDay.strftime("%x"))
    print("TIME:",TimeOfDay.strftime("%X"))

## Command for testing sends message Hello 
@commands.has_role(791392687030140959) # Role families for testing
@client.command()
async def hello(ctx):
    embed=discord.Embed(title="Greetings", description="Hello Friend", color=0xFF3357)
    embed.set_image(url = "https://cdn.discordapp.com/attachments/791322414200913953/836273139251806238/Hello.jpg")
    await ctx.send(f"{ctx.author.mention}", embed = embed)



## Command for sending announcements on channel needs improvement
@commands.has_role(791392687030140959) # Role families for testing
@client.command()
async def announcement(ctx, message):
    embed=discord.Embed(title="SERVER ANNOUNCEMENT", description="```{}```".format(message), color=0xFF3357)
    channel = client.get_channel(834417042652266527)
    await channel.send(embed=embed)

## Command for sending announcements on channel needs improvement
@client.command()
async def ip(ctx):
    embed=discord.Embed(title="SERVER IP", description="```connect deadsilence.gr```", color=0x7289da)
    channel = client.get_channel(834417042652266527)
    await channel.send(embed=embed)

## Command for removing bans from a user
@client.command()
async def unban(ctx, member: discord.Member, reason, id: int):
    User = await ctx.fetch_user(id)
    await member.unban(reason=reason)
    await ctx.guild.unban(User)
    await ctx.send("Unbaned user : {}".format(User))

    
## Command for adding roles from a user and sending a message
@commands.has_role(791392687030140959) # Role families for testing
@client.command()
async def addrole(ctx, member : discord.Member, role : discord.Role):
    embed=discord.Embed(title="Roll Added", description="Roll :{} Added to : {} By User :".format(role,member,), color=0xFF3357)
    channel = client.get_channel(834417042652266527)
    await channel.send(embed = embed)
    await member.add_roles(role)

## Command for removing roles from a user and sending a message 
@commands.has_role(791392687030140959) # Role families for testing
@client.command()
async def removerole(ctx, member : discord.Member , role : discord.Role):
    embed=discord.Embed(title="Greetings", description="Hello Bro :)", color=0xFF3357)
    await ctx.send("```Role : {} Removed from user : {}```".format(role,member))
    await member.remove_roles(role)

## Command for clearing the chat 
@commands.has_role(791392687030140959) # Role families for testing
@client.command()
async def clear(ctx, ammount = 100):
    await ctx.channel.purge(limit = ammount)

## Command for kicking users
@commands.has_role(791392687030140959) # Role families for testing
@client.command()
async def kick(ctx, member : discord.Member, reason):
    await member.kick(reason = reason)
    await ctx.send("```User : {} has been kicked for Reason : {}```".format(member, reason))

## Command for banning users
@commands.has_role(791392687030140959) # Role families for testing
@client.command()
async def ban(ctx, member : discord.Member, reason):
    await member.ban(reason=reason)
    await ctx.send("'''User : {} has been banned fro Reason : {}'''".format(member, reason))

@client.command()
async def reaction_role(ctx, emoji, role: discord.Role, *, message):
    embed = discord.Embed(description = message)
    message = await ctx.channel.send(embed = embed)
    await message.add_reaction(emoji)

## Testing for announcements
@client.command()
async def embed(ctx):
    embed=discord.Embed(title="Sample Embed", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
    await ctx.send(embed=embed)




client.run("NzkxMzA4NTQ3MjMyMTA0NTE4.X-NRgw.3ujtrvu2GdKxV6vKHO9MIUq_ofs")