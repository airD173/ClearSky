import discord
from discord.ext import commands
import data
import embeds
from os import environ
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix = 'cs!')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Activity(name = 'cs!help', type = discord.ActivityType.listening))
    print('Logged in and ready as: ' + bot.user.name)

@bot.command()
async def weather(ctx, *, zipcode = None):
    print(ctx.message.author.name + ' used weather')
    zipcode = int(zipcode)
    alldata = data.main(zipcode)
    data1 = alldata[0]
    data2 = alldata[1]
    allembeds = embeds.main(data1, data2)
    f1 = allembeds[0]
    f2 = allembeds[1]
    f3 = allembeds[2]
    c1 = allembeds[3]
    c2 = allembeds[4]
    c3 = allembeds[5]
    page = 1
    unit = "f"

    message = await ctx.send(embed = f1)
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    await message.add_reaction('🇫')
    await message.add_reaction('🇨')
    @bot.event
    async def on_reaction_add(reaction, user):
        nonlocal message
        nonlocal page
        nonlocal unit
        if user.bot:
            return
        elif reaction.emoji == '◀':
            if page == 1:
                await reaction.remove(user)
            else:
                page -= 1
                await reaction.remove(user)
        elif reaction.emoji == '▶':
            if page == 3:
                await reaction.remove(user)
            else:
                page += 1
                await reaction.remove(user)
        elif reaction.emoji == '🇫':
            if unit == 'f':
                await reaction.remove(user)
            else:
                unit = 'f'
                await reaction.remove(user)
        elif reaction.emoji == '🇨':
            if unit == 'c':
                await reaction.remove(user)
            else:
                unit = 'c'
                await reaction.remove(user)  
        if unit == 'f' and page == 1:
            await message.edit(embed = f1)
        elif unit == 'f' and page == 2:
            await message.edit(embed = f2)
        elif unit == 'f' and page == 3:
            await message.edit(embed = f3)
        elif unit == 'c' and page == 1:
            await message.edit(embed = c1)
        elif unit == 'c' and page == 2:
            await message.edit(embed = c2)
        elif unit == 'c' and page == 3:
            await message.edit(embed = c3)

@bot.command()
async def invite(ctx):
    await ctx.send('<https://discord.com/oauth2/authorize?client_id=820035214788919307&permissions=10240&scope=bot>')

@bot.command()
async def help(ctx):
    print(ctx.message.author.name + ' used help')
    embed = discord.Embed(title = 'Help', description = 'All Commands', color = 0xf55742)
    embed.set_author(name = 'ClearSky')
    embed.add_field(name = 'cs!weather [zipcode]', value = 'Shows current weather and forecast', inline = False)
    embed.add_field(name = 'cs!invite', value = 'Get an invite link for the bot', inline = False)
    embed.add_field(name = 'cs!help', value = 'Shows this menu', inline = False)
    embed.set_thumbnail(url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Icon-round-Question_mark.svg/1200px-Icon-round-Question_mark.svg.png')
    embed.set_footer(text = 'Created by airD')
    await ctx.send(embed = embed)

bot.run(environ['TOKEN'])
