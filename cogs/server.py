import disnake
from disnake.ext import commands

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.slash_command(description = "server")
    async def user(self, inter):
        await inter.response.send_message(f"Your tag: {inter.author}\nYour ID: {inter.author.id}")


def setup(bot):
    bot.add_cog(Server(bot))