import requests, json
import discord
from discord.ext import commands, tasks
from discord import channel, embeds
from datetime import datetime

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print('bot is ready')
    arbloop.start()
    global guadagni
    guadagni = []


@tasks.loop(seconds = 60)
async def arbloop():

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    channel = client.get_channel(850734532209410059) 

    embed=discord.Embed(title=("Orario ",current_time) , color=discord.Color.dark_green())

    r = requests.get("https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=NANO-USDT%22)
    r2 = requests.get("https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=NANO-KCS%22)
    r3 = requests.get("https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=KCS-USDT%22)

    obHUSDT = r.json()
    obHBTC = r2.json()
    obBUSDT = r3.json()



    obHUSDT = obHUSDT['data']['bids'][:1][0][0]
    obHBTC = obHBTC['data']['asks'][:1][0][0]
    obBUSDT = obBUSDT['data']['asks'][:1][0][0]

    print("\n")
    print(obHUSDT)
    valoreusdt = float(obHUSDT) * 10 
    embed.add_field(name="Valore 10 HTR / USDT", value=valoreusdt, inline=False)
    print("\n")
    print(obHBTC)
    obHBTC = float(obHBTC) * 10
    embed.add_field(name="Valore 10 HTR / BTC", value=obHBTC, inline=False)
    print("\n")
    print(obBUSDT)
    valoreBTC = float(obHBTC) * float(obBUSDT)
    embed.add_field(name="Valore da BTC / USDT", value=valoreBTC, inline=False)
    print("\n")
    guadagno = (valoreBTC - valoreusdt)
    embed.add_field(name="Guadagno", value=guadagno, inline=False)

    guadagni.append(guadagno)

    embed.add_field(name="Guadagno complessivo", value=sum(guadagni), inline=False)

    embed.set_thumbnail(url = "https://i.picsum.photos/id/870/536/354.jpg?blur=2&grayscale&hmac=A5T7lnprlMMlQ18KQcVMi3b7Bwa1Qq5YJFp8LSudZ84%22)
    embed.set_footer(text="WAGMI")

    await channel.send(embed=embed)


client.run('')
