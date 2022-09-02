import os
from datetime import datetime

import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands
from pytz import timezone

import constants

client = commands.Bot(command_prefix=constants.COMMAND_PREFIX)
scheduler = AsyncIOScheduler(timezone=constants.TIMEZONE)


@client.event
async def on_ready():
    print(f'Start bot {client.user}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        pass
    elif isinstance(error, commands.errors.MissingAnyRole):
        await ctx.send('Permission denied.')
    else:
        print(error)
        await ctx.send(f'Something wrong. Please contact {constants.AUTHOR}')


@client.command()
async def echo(ctx: commands.context.Context):
    print('=' * 5, datetime.now(), '=' * 5)
    print(f'Get request: {ctx.message.content}')
    await ctx.send(ctx.message.content[5:])
    return


@client.command()
@commands.has_any_role(*constants.BAN_ROLES)
async def ban(ctx: commands.context.Context, member: discord.Member, reason: str=None):
    print('=' * 5, datetime.now(), '=' * 5)
    print(f'Get request: {ctx.message.content}')
    await member.ban(reason=reason)
    await ctx.send(f'User {member} is banned.')
    return


@client.command()
@commands.has_any_role(*constants.KICK_ROLES)
async def kick(ctx: commands.context.Context, member: discord.Member, reason: str=None):
    print('=' * 5, datetime.now(), '=' * 5)
    print(f'Get request: {ctx.message.content}')
    await member.kick(reason=reason)
    await ctx.send(f'User {member} is kicked.')
    return


@client.command()
async def text_channel(ctx: commands.context.Context):
    print('=' * 5, datetime.now(), '=' * 5)
    print(f'Get request: {ctx.message.content}')
    guild: discord.Guild = ctx.message.guild
    pieces = ctx.message.content.split(' ')
    if len(pieces) == 1:
        await ctx.send('Please input channel name.')
        return
    await guild.create_text_channel(' '.join(pieces[1:]), )
    return


@client.command()
async def broadcast(ctx: commands.context.Context, channel: discord.TextChannel):
    print('=' * 5, datetime.now(), '=' * 5)
    print(f'Get request: {ctx.message.content}')
    print(f'Channel: {channel}')
    pieces = [x for x in ctx.message.content.split(' ') if x]

    if len(pieces) < 8:
        await ctx.send('Please input channel, crontab setting and broadcast message.')
        await ctx.send('Like: broadcast #channel * * * * * test per minute')
        return
    try:
        trigger=CronTrigger.from_crontab(' '.join(pieces[2:7]))
    except ValueError:
        await ctx.send('Wrong crontab setting input, please try again.')
        await ctx.send('If no idea about crontab, refer to https://en.wikipedia.org/wiki/Cron')
        return
    message_content = ' '.join(pieces[7:])
    print(f'Job setting {trigger}')
    print(f'Content: {message_content}')
    scheduler.add_job(channel.send, trigger=trigger, args=(message_content,))
    print('Job created.')
    await ctx.send(f'Job created at {channel.name}.')
    return

scheduler.start()
client.run(os.getenv('TOKEN'))
