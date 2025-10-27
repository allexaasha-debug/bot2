import discord
from discord.ext import commands
from passgen import gen_pass
import os,random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def create_password(ctx, n:int):
    await ctx.send(f'kamu ingin membuat password dengan {n} karakter, berikut passwordnya:')
    pwd = gen_pass(n)
    await ctx.send(pwd)

@bot.command()
async def add(ctx, a : int , b : int):
    result = a + b 
    await ctx.send(f'hasil, {a} + {b}, sama dengan {result}')
@bot.command()
async def subtact(ctx, a : int , b : int):
    result = a - b 
    await ctx.send(f'hasil, {a} - {b}, sama dengan {result}')
@bot.command()
async def divide(ctx, a : int , b : int):
    result = a / b 
    await ctx.send(f'hasil, {a} : {b}, sama dengan {result}')
@bot.command()
async def times(ctx, a : int , b : int):
    result = a * b 
    await ctx.send(f'hasil, {a} x {b}, sama dengan {result}')
@bot.command()
async def send_meme(ctx):
    myfolder = os.lisdir('memes')
    img = random.choice(myfolder)
    with open(f'memes/{img}', 'rb') as f:
        file = discord.file(f)
        
    await ctx.send('berikut meme untukmu!')
    await ctx.send(file=file)

@bot.command()
async def animal_meme(ctx):
    folder = 'animals'
    files = os.listdir(folder)
    img = random.choice(files)
    with open(f'{folder}/{img}', 'rb') as f:
        file = discord.File(f)
    await ctx.send("Berikut meme hewan untukmu!")
    await ctx.send(file=file)
