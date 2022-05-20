import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

client = discord.Client()
client = commands.Bot(command_prefix="-")

@client.command()
async def play(ctx, url: str):
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Família')
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  await voiceChannel.connect()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#comandos do bot
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  #variavel pra facilitar a criação de novas funçoes
  msg = message.content

  if message.author.id == 690610432188350546:
    await message.channel.send('Vai se fude hubbão')
  #mandando o luis calar a boca
  elif message.author.id == 310400853720825857:
    await message.channel.send('Cala a boca careca')
  elif msg.startswith('!carol'):
    await message.channel.send('cméquiéh')

async def on_member_join(member):
  channel = client.get_channel(600805747881934879)
  embed = discord.Embed(title="Cuidado rapaziada ", description=f"{member.mention} chego")
  await channel.send(embed=embed)
keep_alive()
client.run(os.getenv('token'))
