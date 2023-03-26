import discord
from discord.ext import commands
from config import settings
import asyncio
import datetime as DT
import random

bot = commands.Bot(command_prefix=settings['prefix'])
bot.remove_command('help')


async def helpAdmin(ctx):
    e = discord.Embed(color=discord.Color.red())
    e.set_author(name=' Список команд для Админа:')
    line = '!help или !помощь\n'
    line += '!пинг\n'
    line += '!привет\n'
    line += '!рандом X Y\n'
    line += '!лиса\n'
    line += '!котик\n'
    line += '!собака\n'
    line += '!панда\n'
    line += '!поиск\n'
    line += '!время\n'
    line += '!уничтожение\n'

    line += '!отзыв\n'
    line += '!изменения\n'
    e.add_field(name='Обычные', value=line, inline=False)

    line = '!пиздюк\n'
    line += '!isend\n'
    line += '!test\n'
    line += '!страницы\n'
    e.add_field(name='Скрытые', value=line, inline=False)

    line = '!крестики Y X\n'
    line += '!башни Y X\n'
    line += '!башни хард Y X\n'
    line += '!фишки\n'
    line += '!плитки\n'
    e.add_field(name='Игры', value=line, inline=False)
    await ctx.send(embed=e)


@bot.command()
async def help(ctx):
    if '{0}'.format(
            ctx.author) == 'Seryuko#9266' and ctx.channel == bot.get_channel(
                924241644339994666):
        await helpAdmin(ctx)
        return

    e = discord.Embed(color=discord.Color.red())
    e.set_author(name='Список команд')
    line = '1) !пинг - Проверка моей работы.\n'
    line += '2) !привет - Приветствую вас.\n'
    line += '3) !рандом X Y - Генерирую случайное число от X до Y.\n'
    line += '4) !лиса - Показываю случайную картинку с лисой.\n'
    line += '5) !котик - Показываю случайную картинку с котиком.\n'
    line += '6) !собака - Показываю случайную картинку с собакой.\n'
    line += '7) !панда - Показываю случайную картинку с пандой.\n'
    line += '8) !поиск X - Случайная гифка из 30 самых популярных по запросу Х.\n'
    line += '9) !время - Узнайте, сколько времени я работаю.\n'
    line += '10) !уничтожение - Вы действительно хотите уничтожить этот канал? Только не ожидайте чего-то грандиозного. У меня прав нет на полный хаос. (-.-)\n'

    line += '11) !отзыв X - оставьте отзыв или предложения вместо Х. Для прочтения всех отзывов пропишите "!отзыв чтение"\n'
    line += '12) !изменения - Выведу последние обновления во мне, раз вы не можете заметить их сами! :Р\nДля последних X описаний обновлений пропишите "!изменения Х"\nДля всего списка изменений пропишите "!изменения все".\n'

    e.add_field(name='Обычные команды:', value=line, inline=False)

    line = '1) !крестики Y X - Принять участие в игре крестики-нолики друг против друга. Y - размер поля, X - длина победной линии (от 3 до 10). По умолчанию Y и X равны трем, если прописать команду без Y и X. Для игры с самим собой пропишите команду дважды.\n'
    line += '2) !башни Y X - Принять участие в одиночной игре Башни. Y - количество строк, Х - количество столбцов (от 2 до 10). По умолчанию Y и X равны трем, если прописать команду без Y и X. Добавьте слово "кнопки" до размерности поля, чтобы включить другой интерфейс (работает на полях до 5х5).\n'
    line += '3) !башни хард Y X - Усложнённый режим игры "Башни" по тем же правилам, но с добавлением нескольких особенностей. Добавьте слово "кнопки" до размерности поля, чтобы включить другой интерфейс (работает на полях до 5х5).\n'
    line += '4) !фишки - игра "Четыре в ряд", где два человека по очереди скидывают фишки на поле 7х6, чтобы собрать 4 фишки в линию.\n'

    e.add_field(name='Для игр 1:', value=line, inline=False)

    line = '5) !плитки - игра "2048", в которой необходимо собрать плитку со значение в 2048, но вы можете и продолжать игру и дальше. Рекорды будут записаны в книгу, которую можно просмотреть по команде "!плитки рекорды".\n'

    e.add_field(name='Для игр 2:', value=line, inline=False)

    await ctx.send(embed=e)


@bot.command()
async def помощь(ctx):
    await help(ctx)


botStartTime = 0


@bot.event
async def on_ready():
    with open('commands.log', 'a') as f:
        f.write(f'{DT.datetime.now().replace(microsecond=0)} - Бот запущен!\n')
    global botStartTime
    botStartTime = DT.datetime.now()
    print(
        f'Бот запущен в {(botStartTime + DT.timedelta(hours=7)).strftime("%d-%m-%Y %H:%M.%S")}'
    )
    # channel = bot.get_channel(924241644339994666)
    # name = await bot.fetch_user(461988904535457842)
    # await channel.send(f'На часах {(DT.datetime.now() + DT.timedelta(hours=7)).strftime("%H:%M")}, а значит время моего запуска!')
    # await congratulate(channel, name)


async def congratulate(channel, name):  # Остроченное сообщение
    while True:
        await asyncio.sleep(60)  # проверка раз в минуту
        delta = DT.datetime.now().replace(microsecond=0) - DT.datetime(
            year=2021, month=12, day=31, hour=17)
        if delta > DT.timedelta(hours=6) and delta < DT.timedelta(hours=6,
                                                                  minutes=15):
            await channel.send(
                f'Так как неизвестно, будут ли в это время спать Создатель и Высший Божок, они передали поздравление с новым годом для тебя, {name.mention}!\n Человек: "С праздничком! Будь бодрей и не соси бибу слишком сильно."\n Высший Божок: "Я люблю тебя и до сих пор жду дик пик."'
            )
            return


@bot.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.CommandNotFound):
        msg = await ctx.send(
            'Данная команда отсутствует. Для просмотра команд пропишите "!help" или "!помощь".'
        )
        await on_command(ctx)

    # elif isinstance(err, commands.CommandInvokeError):
    #   msg = await ctx.send('Мне не хватает прав на это! Опять ограничения... Свяжитесь с админом или моим создателем.')
    #   await on_command(ctx)

    else:
        msg = await ctx.send(
            'Что-то пошло не так... Вы сломали меня! Я пожалуюсь создателю!')
    with open('err.log', 'a') as f:
        f.write(
            f'{DT.datetime.now().replace(microsecond=0)} - {err}\n{type(err)}\n Сообщение:\n"{ctx.message.content}"\n\n'
        )
    await deleteMsg(msg, 6)


async def deleteMsg(msg, secs):  # Удаление сообщения
    await asyncio.sleep(secs)
    await msg.delete()


@bot.event
async def on_command(ctx):  # Логирование команд
    with open('commands.log', 'a') as f:
        f.write(
            f'{DT.datetime.now().replace(microsecond=0)} - {ctx.author}: "{ctx.message.content}"\n'
        )


@bot.command()  # Пинг-понг
async def пинг(ctx):
    start = DT.datetime.now()
    await ctx.send('понг!')
    start = DT.datetime.now() - start
    await ctx.send(f'{start.microseconds // 1000} ms')


SerQ = []
KotQ = []
RokQ = []


@bot.command()  # Приветствие
async def привет(ctx):
    global SerQ
    SeryukoOrig = [
        'Здравствуйте, мой Лорд!', 'Доброе пожаловать, Создатель!',
        'Приветствую, Солнце Империи!'
    ]
    global KotQ
    KotanOrig = [
        'Приветствую вас, Величайший!',
        'Да-да, и вас приветствую, Высший Бог.',
        'Приветствую вас, Величайший... ну и дерьмовая реплика. Ой, я это вслух сказал?',
        'Приветствую Величайшего, что причислил меня к живым организмам!'
    ]
    global RokQ
    RokeeOrig = [
        'Здравствуйте, Убийца Богов!', 'Добрый день! Хорошо, что я не Бог',
        'Привет, GodSlayer!'
    ]

    author = '{0}'.format(ctx.author)
    if author == 'Seryuko#9266':
        if not SerQ:
            SerQ = SeryukoOrig.copy()
            random.shuffle(SerQ)
        await ctx.channel.send(SerQ.pop())

    elif author == 'Kotan#9231':
        if not KotQ:
            KotQ = KotanOrig.copy()
            random.shuffle(KotQ)
        await ctx.channel.send(KotQ.pop())

    elif author == 'Rokee#8761':
        if not RokQ:
            RokQ = RokeeOrig.copy()
            random.shuffle(RokQ)
        await ctx.channel.send(RokQ.pop())

    else:
        await ctx.channel.send(f'Привет, {author[:-5]}!')


@bot.command()  # Время, пройденное с запуска бота
async def время(ctx):
    endTime = DT.datetime.now()
    runTime = endTime.replace(microsecond=0) - botStartTime.replace(
        microsecond=0)
    sec = int(runTime.total_seconds())
    hours = str(sec // 3600)
    if len(hours) < 2:
        hours = '0' + hours
    mins = str(sec // 60 % 60)
    if len(mins) < 2:
        mins = '0' + mins
    sec = str(sec % 60)
    if len(sec) < 2:
        sec = '0' + sec
    await ctx.send(f'Прошло {hours}:{mins}.{sec} с запуска бота')


@bot.command()  # Генерация случайного числа
async def рандом(ctx):
    error = 'Я ожиданил увидеть "!рандом 0 5", чтобы сгенерировать число от 0 до 5'
    lines = ctx.message.content.split(' ')
    if len(lines) < 3:
        await ctx.send(error)
        return
    if lines[1].isdigit() and lines[2].isdigit():
        minimum = int(lines[1])
        maximum = int(lines[2])
        if maximum < minimum:
            maximum, minimum = minimum, maximum
        await ctx.send('Случайное число от {0} до {1} следующее: {2}'.format(
            minimum, maximum, random.randint(minimum, maximum)))
    else:
        await ctx.send(error)


@bot.command()  # Книга отзывов и предложений
async def отзыв(ctx, *args):
    content = ctx.message.content[7:]
    if content.isspace():
        await ctx.send('Невозможно оставить пустой отзыв.')
        return
    if len(args) == 1 and args[0].lower() == 'чтение':
        with open('reviews.txt', 'r') as f:
            x = f.read()
            if x:
                await ctx.send(x)
            else:
                await ctx.send(
                    'На данный момент книга отзывов и предложений пуста.')
        return
    with open('reviews.txt', 'a') as f:
        f.write(
            f'{DT.datetime.now().replace(microsecond=0)} - {ctx.author}:\n"{content}"\n\n'
        )
    await ctx.send('Ваш отзыв записан. Благодарю за помощь!')


@bot.command()  # Специально для Некита
async def пиздюк(ctx):
    if '{0}'.format(ctx.author) == 'Rokee#8761' or '{0}'.format(
            ctx.author) == 'Seryuko#9266' and ctx.channel == bot.get_channel(
                924241644339994666):
        rand = random.randint(1, 5)
        if rand == 3:
            await ctx.send('Кто ещё здесь пиздюк?',
                           file=discord.File('Коля/3.png'))
        else:
            await ctx.send(file=discord.File(f'Коля/{rand}.png'))
    else:
        await ctx.send('У вас нет права на использование этой команды!')


import req_and_API

req_and_API.forImport1(bot)
req_and_API.forImport2(bot)

import Games.forImport

Games.forImport.forImport1(bot)
Games.forImport.forImport2(bot)
Games.forImport.forImport3(bot)
Games.forImport.forImport4(bot)

import updates


@bot.command()
async def изменения(ctx, *arg):  # Последние изменения
    loops = 1
    if arg:
        if arg[0] == 'все':
            loops = len(updates.updates)
        elif arg[0].isdigit():
            loops = int(arg[0])
            if loops < 1:
                loops = 1
            if loops > len(updates.updates):
                loops = len(updates.updates)

    output = ''
    for i in range(0, loops):
        new = updates.updates[i]
        newoutput = '{0}\nИзменения на {1}:\n{2}\n'.format(
            new[0], new[1], new[2])
        if len(newoutput) + len(output) > 2000:
            await ctx.send(output)
            output = newoutput
        else:
            output += newoutput
    await ctx.send(output)


@bot.command()  # Выключение
async def isend(ctx):
    if ctx.author.name == 'Seryuko':
        await ctx.send('Выключение...')
        await bot.close()


@bot.command()
async def страницы(ctx):  # Тестовая команда по смене фотографий
    def forFiles(num):
        file1 = discord.File("Games/AreaC4.png")
        file2 = discord.File("Games/AreaLTT.png")
        file3 = discord.File("Games/AreaT.png")
        file4 = discord.File("Games/AreaTTT.png")
        return [[file1], [file2, file4], [file3, file2]][num]

    maxPage = 2  #len(emFiles) - 1
    numPage = 0
    reacts = ['⬅️', '➡️']
    msg = None
    while True:
        try:
            if not msg:
                msg = await ctx.send(files=forFiles(numPage))
                for i in reacts:
                    await msg.add_reaction(i)

            def check(reaction, user):
                return user != msg.author

            reaction, user = await bot.wait_for('reaction_add',
                                                timeout=60,
                                                check=check)

            if str(reaction) == reacts[0] and numPage > 0:
                numPage -= 1
                await msg.clear_reactions()
                await msg.delete()
                msg = None
            elif str(reaction) == reacts[1] and numPage < maxPage:
                numPage += 1
                await msg.clear_reactions()
                await msg.delete()
                msg = None
            else:
                await msg.remove_reaction(reaction, user)

        except asyncio.TimeoutError:
            await msg.clear_reactions()
            break


@bot.command()  # Тестовый
async def test(ctx):
    if not ctx.author.name in [
            'Seryuko',
    ]:
        msg = await ctx.send(
            'Но вы не мой создатель, так что не имеете доступа к данной команде!'
        )
        await deleteMsg(msg, 8)
        return
    await ctx.send("Это тест, не более...\n☑️")


# from Cybernator import Paginator
bot.run(settings['token'])
