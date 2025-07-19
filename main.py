import os
import disnake
from flask import Flask
from config import config
from dotenv import load_dotenv
from disnake.ext import commands

load_dotenv()
app = Flask(__name__)

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents)

@app.route("/")
def home():
    return "Bot is running!"

# Запускаем Flask сервер в потоке
def run_flask():
    app.run(host="0.0.0.0", port=3000)

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

# Запускаем бота
bot.loop.create_task(run_flask())

try:
    bot.run(config['token'])
except KeyboardInterrupt:
    print("Выход из программы...")
