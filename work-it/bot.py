import discord
from discord.ext import commands
from datetime import datetime
import calendar
import time
import pytz
import os
from dotenv import load_dotenv

tasks = {}
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


def date_validate(date_text):
    try:
        if date_text != datetime.strptime(date_text,
                                          "%d-%m-%Y").strftime('%d-%m-%Y'):
            return False
        else:
            return True
    except ValueError:
        return False


def time_validate(time_text):
    timeformat = "%H:%M"
    try:
        if(datetime.strptime(time_text, timeformat)):
            return True
        else:
            return False
    except ValueError:
        return False


def tscalc(date):
    local = pytz.timezone("Asia/Kolkata")
    naive = datetime.strptime(date, "%H:%M %d-%m-%Y")
    local_dt = local.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    timestamp = int(datetime.timestamp(utc_dt))
    return timestamp


def check_tscal(cts, uts):
    if(int(uts) >= int(cts)):
        return True
    return False


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    IST = pytz.timezone('Asia/Kolkata')


@bot.event
async def on_member_join(member):
    await message.channel.send(f'Hi {member.name}, welcome to koalas channel')


@bot.command()
async def hi(ctx):
    await ctx.send("hi {}".format(ctx.author))


@bot.command()
async def task(ctx, *args):
    if(args[0] == 'add'):
        times = args[::-1][0:4][::-1]
        title = ' '.join(args[::-1][4:-1][::-1])
        c_timestamp = str(calendar.timegm(time.gmtime()))
        values = list(times)
        s_timestamp = tscalc(values[0] + ' ' + values[1])
        e_timestamp = tscalc(values[2] + ' ' + values[3])
        if(date_validate(values[1]) and date_validate(values[3]) and
           time_validate(values[0]) and time_validate(values[2]) and
           check_tscal(c_timestamp, e_timestamp)) is True:
            values.extend([title, c_timestamp])
            tasks[c_timestamp] = {
                                'title': values[4],
                                'start_time': values[0],
                                'start_date': values[1],
                                'end_time': values[2],
                                'end_date': values[3],
                                'id': values[5]}
            await ctx.send('task added successfully')
        else:
            await ctx.send('Check the format and re-enter')
    elif(args[0] == 'view'):
        if len(tasks) == 0:
            await ctx.send('Bingoo! have a kitkat')
        else:
            for i in tasks.values():
                e = discord.Embed(title=i['title'], description=i['id'])
                e.add_field(name='start_time', value=i['start_time'],
                            inline=True)
                e.add_field(name='start_date', value=i['start_date'],
                            inline=True)
                e.add_field(name='* * * * *', value='* * * * *', inline=False)
                e.add_field(name='end_time', value=i['end_time'], inline=True)
                e.add_field(name='end_date', value=i['end_date'], inline=True)
                await ctx.send(embed=e)
    elif(args[0] == 'complete'):
        if len(tasks) == 0:
            await ctx.send('Hurray! all up to date')
        elif(len(args) == 2):
            try:
                tasks.pop(args[1])
            except:
                await ctx.send('id not found!')
        else:
            await ctx.send('you may want to type !task complete <id>')
    elif(args[0] == 'snooze'):
        if len(tasks) == 0:
            await ctx.send('Hurray! all up to date')
        elif(len(args) == 3):
            try:
                if(date_validate(args[2])):
                    tasks[args[1]]['end_date'] = args[2]
                else:
                    await ctx.send('Check the format and re-enter')
            except:
                await ctx.send('id not found!')
        else:
            await ctx.send('you may want to type !task snooze <id> <new_date>')
    else:
        await ctx.send("You may want to enter 'add' , 'complete' , 'view' ")
bot.run(TOKEN)
