
import discord
from discord.ext import commands


settings = {
'token' : '',
'botname' : '',
'id' : "id",
'prefix' : "PREFIX"
}

bot = commands.Bot(command_prefix = settings['prefix'],intents = discord.Intents.all())
client = discord.Client()
bot.remove_command('help')





@bot.command()
async def nuclear(ctx):
    from components import boom,boom_wave
    from radiation import radiation,dust
    from aftermath_of_the_explosion import mutation

    await boom(ctx)
    
    await boom_wave(ctx)

    await radiation(ctx)

    await dust(ctx)
    
    await mutation(ctx)








bot.run(settings["token"])
