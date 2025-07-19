import os
import disnake
from config import config
from dotenv import load_dotenv
from disnake.ext import commands

load_dotenv()

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=disnake.Status.online)

    print("==============================")
    print(f'Bot - {bot.user}')
    print(f'API Version - disnake - {disnake.__version__}')
    print("==============================")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

try:
    bot.run(config['token'])
except KeyboardInterrupt:
    print("Выход из программы...")
