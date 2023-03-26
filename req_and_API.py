import discord
import asyncio
import datetime as DT
import random
import requests

# Команды, связанные с request'ами и API 
def forImport1(bot):
  
  @bot.command() # Пример запроса
  async def лиса(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = response.json()
    e = discord.Embed(color = 0xff9900)
    e.set_image(url = json_data['link'])
    await ctx.send(embed = e)
  
  @bot.command() # Пример запроса
  async def котик(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = response.json()
    e = discord.Embed(color = 0xa0a0a0)
    e.set_image(url = json_data['link'])
    await ctx.send(embed = e)
  
  @bot.command() # Пример запроса
  async def собака(ctx):
    response = requests.get('https://some-random-api.ml/img/dog')
    json_data = response.json()
    e = discord.Embed(color = 0xffff00)
    e.set_image(url = json_data['link'])
    await ctx.send(embed = e)
  
  @bot.command() # Пример запроса
  async def панда(ctx):
    response = requests.get('https://some-random-api.ml/img/panda')
    json_data = response.json()
    e = discord.Embed(color = 0xffffff)
    e.set_image(url = json_data['link'])
    await ctx.send(embed = e)
  
lastReqName = None
lastReq = None
def forImport2(bot):
  @bot.command() # Пример API
  async def поиск(ctx, *args):
    # params = dict(appid='4EFC2F2CA1F9547B3C048B40C33A6A4FEF1FAF3B', sources='image', query='apple')
    # response = requests.get('http://api.search.live.net/json.aspx', params=params)
    # await ctx.send(f'{response}\n{response.text}')
    if not args:
      await ctx.send('Но в команде нет запроса на поиск. Пожалуйста, введите "!поиск манга", если хотите найти гифку по запросу "манга".')
      return
  
    global lastReqName
    global lastReq
    arg = ' '.join(args)
    if lastReqName != arg:
      params = dict(key='GQF8EU2MB6KS', contentfilter='off', q=arg, limit='30')#(api_key='EaiVNtb0K1OCOW4jMqAC5xcDN7bKCx8A', q=arg,rating='r',lang='ru',limit='20')
      response = requests.get('https://g.tenor.com/v1/search', params=params)#('http://api.giphy.com/v1/gifs/search', params=params)
  
      # if not response or not response.json()['pagination']['count']:
      if not response:
        await ctx.send('Что-то не так. Количество запросов иссякло или ничего не было найдено. Хнык-хнык...')
        return
      lastReqName = arg
      lastReq = response.json()
    
    try:
      await ctx.send(random.choice(lastReq['results'])['media'][0]['gif']['url'])
    except:
      await ctx.send("По этому запросу результатов не найдено...")
    # await ctx.send(random.choice(lastReq['data'])['embed_url'])
  
    # e = discord.Embed(color = 0xffffff)
    # e.set_image(url = json_data['link'])
    # await ctx.send(embed = e)
  
  
  
  @bot.command() # Ядерное оружие (первые реакции)
  async def уничтожение(ctx):
    yas = '☑️'
    nay = '❌'
    valid_reactions = [yas, nay]
  
    message = await ctx.send("Вы уверены, что хотите использовать ядерное оружие?")
    for i in valid_reactions:
      await message.add_reaction(i) 
  
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in valid_reactions
    try:
      reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
      # await message.clear_reactions()
  
      if str(reaction.emoji) == yas:
        embed = discord.Embed(title="Код: 759245 Активирован. Уничтожение канала запущено.")
        embed.set_image(url="https://i.gifer.com/3Tt5.gif")
        await ctx.send(embed=embed)
      else:
        await ctx.send('Операция отменена. Благодарим за использование наших ракетных линий "Большая Мамка".\n "Большая мамка" - А от кого ещё может так прилететь?')
  
    except asyncio.TimeoutError:
      await ctx.send('Время ожидания вышло! \n Операция отменена.')
      await message.clear_reactions()