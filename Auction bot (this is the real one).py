import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'My ping is {round(client.latency * 1000)}ms!')

@client.command(aliases=['auction','bid','newbid'])
async def NewBid(ctx,*,question):
    ResponseToBid = 'Okay we are making the auction right now.'
    CurrentBid=0
    if (int()>CurrentBid):
        await ctx.send(f'NewBid = {question}\n {Response}')
    else:
        await ctx.sent(f'too low man')


@client.event
async def on_member_join(member):
    print(f'{member} has joined.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left.')

@client.command()
async def popcorn(ctx):

    urls = [ "https://media2.giphy.com/media/RHiD0K65NxxLO/giphy.gif?cid=790b7611f617aec860c69cc43c8ef66f94b986fba6d06ea4&rid=giphy.gif",
                "https://media1.giphy.com/media/tFK8urY6XHj2w/giphy.gif?cid=790b76119612bc4781736548a9b55c630970008757dd7ed3&rid=giphy.gif",
                "https://media2.giphy.com/media/12aW6JtfvUdcdO/giphy.gif?cid=790b7611451e6853c981e4168cde3bb8bbdbea65680b5a52&rid=giphy.gif",
                "https://media2.giphy.com/media/NipFetnQOuKhW/giphy.gif?cid=790b761141bcb041ab7f8985ab9bcce5f91eb76b78888ada&rid=giphy.gif",
                "https://media3.giphy.com/media/aFEMFqZpDrkRy/giphy.gif?cid=790b7611a67a6eeb849081ba37ce19be4f5a28ed1c48bf9b&rid=giphy.gif",
                "https://media1.giphy.com/media/guFC9FLnHXYfS/giphy.gif?cid=790b7611a71e6db5d55bb6dc83614c01e17426423dbdbbc1&rid=giphy.gif",
                "https://media2.giphy.com/media/9RcIx27XA7qhi/giphy.gif?cid=790b7611cb9f8f10269c16714d6a2af77af45b16424472c3&rid=giphy.gif",
                "https://media0.giphy.com/media/vfKUbxZts6FI4/giphy.gif?cid=790b76116ba8e0f9fa218ea3796b91c806fecd3b2e416420&rid=giphy.gif",
                "https://media3.giphy.com/media/QUH3GZEnUfcd2/giphy.gif?cid=790b76119e996ca00740deb95785b4ae2bd7c16b5ed676e7&rid=giphy.gif"]
    embed = discord.Embed(colour=discord.Colour.blue(), title="Don't mind me",)

    embed.set_author(name="Tank Memefactory", icon_url="https://img1.wsimg.com/isteam/ip/f2e2fc8f-eb6e-47ba-8d30-f500f492aeae/1569205327-23.16.39.126.png/:/cr=t:0%25,l:0%25,w:100%25,h:100%25")
    # embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/665737773197819934.png?v=1")
    embed.set_image(url=f"{random.choice(urls)}")


    embed.set_footer(text="Powered By fuckin TANK", icon_url="https://cdn.discordapp.com/icons/593648497530634251/a_538923c2814452363e069843b8c3769e.gif?size=2048")
    await ctx.send(embed=embed)

print[response]


client.run('NjkzOTU5MDYyNzQzODEwMTA4.XoPu9Q.VCJurER0TA3-mgUMEQTjf-B0ZTo')
