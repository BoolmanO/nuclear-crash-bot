import asyncio
import discord
from discord.ext import commands


from components import boom,boom_wave
	
from radiation import radiation,dust
    
from aftermath_of_the_explosion import mutation



settings = {
'token' : 'TOKEN',
'botname' : 'GT',
'id' : "ID",
'prefix' : "GMD"
}

bot = commands.Bot(command_prefix = settings['prefix'],intents = discord.Intents.all())
client = discord.Client()
bot.remove_command('help')

async def nuke_dust(ctx):

	loop = asyncio.get_event_loop()
    
	asyncio.ensure_future(dust(ctx,))
	for i in range(20):
		asyncio.ensure_future(dust(ctx,))
	
	asyncio.ensure_future(dust(ctx,))
	asyncio.ensure_future(dust(ctx,))
	asyncio.ensure_future(dust(ctx,))
	
	
	#for i in range(100):
		#asyncio.ensure_future(dust(ctx,))
		
	loop.run_forever()
	
async def nuke_boom_wave(ctx):
	
	loop = asyncio.get_event_loop()
	
	for i in range(20):
		asyncio.ensure_future(boom_wave(ctx,))
	asyncio.ensure_future(boom_wave(ctx,))	
	asyncio.ensure_future(boom_wave(ctx,))
	asyncio.ensure_future(boom_wave(ctx,))
	asyncio.ensure_future(boom_wave(ctx,))
	asyncio.ensure_future(boom_wave(ctx,))
	asyncio.ensure_future(boom_wave(ctx,))
	asyncio.ensure_future(boom_wave(ctx,))
	asyncio.ensure_future(boom_wave(ctx,))
	
	loop.run_forever()
	
async def nuke_radiation(ctx):
	
	loop = asyncio.get_event_loop()
	
	for i in range(10):
		asyncio.ensure_future(radiation(ctx,))
	asyncio.ensure_future(radiation(ctx,))
	
	asyncio.ensure_future(radiation(ctx,))
	asyncio.ensure_future(radiation(ctx,))
	asyncio.ensure_future(radiation(ctx,))

    
    
	loop.run_forever()


async def nuke_boom(ctx):


	asyncio.ensure_future(boom(ctx,))
	asyncio.ensure_future(boom(ctx,))
	
	asyncio.ensure_future(boom(ctx,))
	asyncio.ensure_future(boom(ctx,))
	asyncio.ensure_future(boom(ctx,))







@bot.command()
async def nuclear(ctx):
  
    
    #loop = asyncio.get_event_loop()



    await nuke_boom(ctx)
    
    await nuke_boom_wave(ctx)

    await nuke_radiation(ctx)

    await nuke_dust(ctx)

    
    
    #await loop.run_forever()








bot.run(settings["token"])
