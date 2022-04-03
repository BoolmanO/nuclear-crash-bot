
import discord
from discord.ext import commands


settings = {
'token' : '',
'botname' : '',
'id' : 123,
'prefix' : ""
}

bot = commands.Bot(command_prefix = settings['prefix'],intents = discord.Intents.all())
client = discord.Client()
bot.remove_command('help')





@bot.command()
async def nuclear(ctx):
    from components import boom,boom_wave
    from radiation import radiation,dust
    from aftermath_of_the_explosion import mutation

    while True:
        try:
    
            await boom_wave(ctx)
            await boom(ctx)
            await radiation(ctx)
            await dust(ctx)
            await mutation(ctx)

        except Exception as e:
            print("FINALLY")
            print(e)
            break







bot.run(settings["token"])