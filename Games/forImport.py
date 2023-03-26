import discord
import asyncio
import datetime as DT
import random


# from discord import DiscordComponents, Button
# from discord_buttons_plugin import  *
async def deleteMsg(msg, secs):  # Удаление сообщения
    await asyncio.sleep(secs)
    await msg.delete()


def gameChannel(bot, channel):  # Каналы для игр
    return channel in (bot.get_channel(925761710575484929),
                       bot.get_channel(924241644339994666))


import Games.TicTacToe as ttt  # Tic Tac Toe или Крестики-нолики

gameTTT = []
stateTTT = 0
firstNameTTT = ''
secondNameTTT = ''
boxsize = winsize = 3
msgTTT1 = None
msgTTT2 = None


def forImport1(bot):
    @bot.command()  # Вход в игру крестики-нолики
    async def крестики(ctx, *args):
        if not gameChannel(bot, ctx.channel):
            return
        global stateTTT
        global firstNameTTT
        global secondNameTTT
        global gameTTT
        global boxsize, winsize
        global msgTTT1, msgTTT2
        if stateTTT == 0:
            firstNameTTT = '{0}'.format(ctx.author)
            stateTTT = 1
            boxsize = winsize = 3
            if args and args[0].isdigit():
                boxsize = int(args[0])
                if len(args) > 1 and args[1].isdigit():
                    winsize = int(args[1])
            if boxsize < 3 or boxsize > 10:
                boxsize = 3
                winsize = 3
            elif winsize > boxsize or winsize < 3:
                winsize = 3
            await ctx.send(
                f'Первый игрок в крестики-нолики принят: {firstNameTTT}\nПоле {boxsize}x{boxsize}, с выйгрышем по линии длиной в {winsize}\nОжидание второго игрока...'
            )

        elif stateTTT == 1:
            secondNameTTT = '{0}'.format(ctx.author)
            stateTTT = 2
            gameTTT = ttt.TTT(boxsize, winsize)
            gameTTT.firstName = firstNameTTT
            gameTTT.secondName = secondNameTTT
            await ctx.send(
                f'Второй игрок в крестики-нолики принят: {secondNameTTT}\nПоле {boxsize}x{boxsize}, с выйгрышем по линии длиной в {winsize}\nТеперь можно начинать. Чтобы сделать ход на вторую строку, первый столбец необходимо ввести "!крестики 2 1". Первым ходит {firstNameTTT} с меткой "Х". Начинаем!'
            )
            msgTTT1 = await ctx.send(
                f'Каков ваш ход за X, {firstNameTTT[:-5]}?',
                file=discord.File("Games/AreaTTT.png"))

        else:
            if args and args[0].lower() == 'сброс':
                stateTTT = 0
                await ctx.send(
                    f'Прошлая игра завершилась. Для новой игры используйте команду "!крестики X Y".'
                )
                return

            if not args or not (len(args) > 1 and args[0].isdigit()
                                and args[1].isdigit()):
                await ctx.send(
                    f'Идёт игра между {firstNameTTT} и {secondNameTTT}. Ожидалась команда "!крестики Х Y", где Х - номер строки, Y - номер столбца. Для сброса текущей игры введите "!крестики сброс".'
                )
                return

            if msgTTT2:
                await msgTTT2.delete()
            msgTTT2 = msgTTT1
            msgTTT1 = await ctx.send(gameTTT.tictac(int(args[0]), int(args[1]),
                                                    '{0}'.format(ctx.author)),
                                     file=discord.File("Games/AreaTTT.png"))


numOfButtonGames = 0

import Games.LowerTheTower as ltt  # Lower The Tower или Башни

stateLTT = 0
gameLTT = None
msgLTT1 = None
msgLTT2 = None
userLTT = None
buttonsLTTConfirm = False
buttonsLTT = None


def forImport2(bot):
    @bot.command()
    async def башни(ctx, *args):
        if not gameChannel(bot, ctx.channel):
            return
        global gameLTT
        global stateLTT
        global msgLTT1
        global msgLTT2
        global userLTT
        global buttonsLTT
        global buttonsLTTConfirm
        global numOfButtonGames

        if stateLTT == 0:
            ishard = False
            msgLTT1 = None
            msgLTT2 = None
            buttonsLTTConfirm = False
            numOfButtonGames += 1

            if args and args[0].lower() == 'сброс':
                await ctx.send(
                    'Игра уже сброшена. Чтобы начать игру напишите "!башни Y X", где Y - количество строк, а Х - количество столбцов, или "!башни хард Y X" для сложного режима.'
                )
                return

            elif args and args[0].lower() == 'хард':
                ishard = True
                if len(args) > 1 and args[1].lower() == 'кнопки':
                    await ctx.send('Данная функция временно недоступна... -.-')
                    return
                    # buttonsLTTConfirm = True
                    # await buttonsLTTgame(bot, ctx, args)
                    # return
                if len(args) > 2 and args[1].isdigit() and args[2].isdigit():
                    y = int(args[1])
                    x = int(args[2])
                    if y < 2 or y > 10:
                        y = 3
                    if x < 2 or x > 10:
                        x = 3
                else:
                    y = 3
                    x = 3

            elif args:
                if args[0].lower() == 'кнопки':
                    await ctx.send('Данная функция временно недоступна... -.-')
                    return
                    # buttonsLTTConfirm = True
                    # await buttonsLTTgame(bot, ctx, args)
                    # return
                if len(args) > 1 and args[0].isdigit() and args[1].isdigit():
                    y = int(args[0])
                    x = int(args[1])
                    if y < 2 or y > 10:
                        y = 3
                    if x < 2 or x > 10:
                        x = 3
            else:
                y = 3
                x = 3

            stateLTT = 1
            userLTT = '{0}'.format(ctx.author)
            gameLTT = ltt.LTT(y, x, ishard)
            if ishard:
                ishard1 = 'Сложные '
                ishard2 = '\nВ сложном режиме синие башни влияют на те, что соприкасаются с рёбрами, красные - на те, что находятся по диагоналям, а зелёные - и на все направления.\n'
            else:
                ishard1 = ''
                ishard2 = ''
            await ctx.send(
                f'Игрок в {ishard1}Башни принят: {userLTT}. \nПоле размером {y}х{x}.\nКаждый квадрат является башней. Белые рамки говорят, что башня поднята, башни без неё считаются опущенными. Опустите все башни, чтобы вокруг них не было белой рамки. {ishard2}Для выполнения хода напишите "!башни 2 3", чтобы изменить положение башни во второй строке и третьем столбце. \nЕсли хотите сбросить игру напишите "!башни сброс".'
            )
            await ctx.send(file=discord.File('Games/AreaLTT.png'))

        elif stateLTT == 1:
            if not args:
                await ctx.send(
                    'Ожидалась команда "!башни Х Y" для хода или "!башни сброс" для сброса текущей игры.'
                )

            elif args[0].lower() == 'сброс':
                stateLTT = 0
                await ctx.send(
                    f'Игра Башни была сброшена. Прошлая игра остановилась на {gameLTT.numMoves()} ходу. Возможно, минимум ходов равен {gameLTT.numChanges()}. Для новой игры необходимо прописать команду "!башни".'
                )
                if buttonsLTTConfirm:
                    for i in buttonsLTT:
                        for j in i:
                            j.disabled = True
                    await msgLTT1.edit(content="", components=buttonsLTT)

            elif '{0}'.format(ctx.author) == userLTT:
                if buttonsLTT:
                    await ctx.send(
                        'Для игры используйте кнопки. Для сброса игры необходимо прописать команду "!башни сброс".'
                    )
                    return
                if len(args) < 2 or not (args[0].isdigit()
                                         and args[1].isdigit()):
                    await ctx.send(
                        'Я ожидал увидеть "!башни 2 1", чтобы вы изменили положение башни во второй строке, первом столбце. \nЕсли хотите сбросить игру, то необходимо прописать команду "!башни сброс".'
                    )
                    return

                maxY, maxX = gameLTT.lenWid()
                y = int(args[0])
                x = int(args[1])
                if y > maxY or x > maxX:
                    await ctx.send(
                        f'Вы указали ход больше, чем поле в игре. Пожалуйста, не выходите за рамки {maxY} строк и {maxX} столбцов.'
                    )
                    return

                gameLTT.userMove(y, x)
                line = f'Башня в {y} строке {x} столбце была'
                if gameLTT.userCheck(y - 1, x - 1):
                    line += ' опущена.'
                else:
                    line += ' поднята.'
                if gameLTT.isEnd():
                    line += f'\nВы выйграли на {gameLTT.numMoves()} ходу!\nВозможно, минимум ходов равен {gameLTT.numChanges()}.'
                    stateLTT = 0
                temp = await ctx.send(line)
                if msgLTT2:
                    for i in msgLTT2:
                        await i.delete()
                msgLTT2 = msgLTT1
                msgLTT1 = [
                    temp, await
                    ctx.send(file=discord.File('Games/AreaLTT.png'))
                ]

            else:
                await ctx.send(
                    'В Башни уже кто-то играет. Если хотите сбросить игру, то необходимо прописать команду "!башни сброс".'
                )


# async def buttonsLTTgame(bot, ctx, args):
#   DiscordComponents(bot)
#   global gameLTT
#   global stateLTT
#   global msgLTT1
#   global msgLTT2
#   global userLTT
#   global buttonsLTT
#   global numOfButtonGames
#   thisNumOfButtonGames = numOfButtonGames
#   timeout = 600.0 # Время ожидания ответа

#   ishard = False
#   x, y = 3, 3
#   if args[0].lower() == 'хард':
#     ishard = True
#     if len(args)>3 and args[2].isdigit() and args[3].isdigit():
#       y = int(args[2])
#       x = int(args[3])

#   elif len(args)>2 and args[1].isdigit() and args[2].isdigit():
#       y = int(args[1])
#       x = int(args[2])

#   if y < 2 or y > 5:
#     y = 3
#   if x < 2 or x > 5:
#     x = 3
#   stateLTT = 1
#   userLTT = '{0}'.format(ctx.author)
#   gameLTT = ltt.LTT(y, x, ishard)
#   reacts = ['✖️','✔️','❌','☑️']
#   if ishard:
#     ishard1 = 'Сложные '
#     ishard2 = '\nВ сложном режиме синие башни влияют на те, что соприкасаются с рёбрами, красные - на те, что находятся по диагоналям, а зелёные - и на все направления.\n'
#   else:
#     ishard1 = ''
#     ishard2 = ''
#   await ctx.send(f'Игрок в {ishard1}Башни принят: {userLTT}. \nПоле размером {y}х{x}.\nКаждый квадрат является башней. Смайлики крестиками ({reacts[2]}) говорят, что башня поднята, а башни без них считаются опущенными. Опустите все башни - уберите все крестики, чтобы выйграть. {ishard2}Для выполнения хода нажмите на кнопки. \nЕсли хотите сбросить игру напишите "!башни сброс".', file=discord.File('Games/AreaLTT.png'))

#   ids = []
#   buttonsLTT = []
#   react = {"id": None, "name": reacts[0], "animated": False}
#   for j in range(y):
#     buttonsLTT.append([])
#     for i in range(x):
#       ids.append(f'buttonLTT{numOfButtonGames}{j}{i}')
#       type = ButtonType().Primary
#       if gameLTT.userCheckC(j,i) == 1:
#         type = ButtonType().Danger
#       elif gameLTT.userCheckC(j,i) == 2:
#         type = ButtonType().Success

#       if gameLTT.userCheck(j,i):
#         buttonsLTT[j].append(Button(label=" ", emoji=None, custom_id=ids[j*x+i], style=type))
#       else:
#         buttonsLTT[j].append(Button(label=None, emoji=react, custom_id=ids[j*x+i], style=type))

#   msgLTT1 = await ctx.send('Используйте эти кнопки для управления!', components=buttonsLTT)

#   while not gameLTT.isEnd():
#     try:
#       interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id in ids, timeout=timeout)
#     except asyncio.TimeoutError:
#       if thisNumOfButtonGames != numOfButtonGames:
#         return
#       stateLTT = 0
#       await ctx.send(f'Игра "Башни" была сброшена так как время ожидания действия вышло. Она остановлена на {gameLTT.numMoves()} ходу!\nВозможно, минимум ходов равен {gameLTT.numChanges()}.')
#       for i in buttonsLTT:
#         for j in i:
#           j.disabled=True
#       await msgLTT1.edit(content="", components=buttonsLTT)
#       return

#     if '{0}'.format(interaction.user) != userLTT:
#       await interaction.send(f'На данный момент идёт игра пользователя {userLTT}. Для её сброса напишите "!плитки сброс".')
#       continue

#     y=int(interaction.custom_id[-2])+1
#     x=int(interaction.custom_id[-1])+1
#     gameLTT.userMove(y,x)
#     msg = f'Башня в {y} строке {x} столбце была'
#     if gameLTT.userCheck(y-1, x-1):
#       msg += ' опущена.'
#     else:
#       msg += ' поднята.'

#     for j in [y-2, y-1, y]:
#       if j < 0 or j >= len(buttonsLTT):
#         continue
#       for i in [x-2, x-1, x]:
#         if i < 0 or i >= len(buttonsLTT[j]):
#           continue
#         if gameLTT.userCheck(j,i):
#           buttonsLTT[j][i].emoji=None
#           buttonsLTT[j][i].label=" "
#         else:
#           buttonsLTT[j][i].emoji=react
#           buttonsLTT[j][i].label=None

#     if gameLTT.isEnd():
#       msg += f'\nВы выйграли на {gameLTT.numMoves()} ходу!\nВозможно, минимум ходов равен {gameLTT.numChanges()}.'
#       stateLTT = 0
#       for i in buttonsLTT:
#         for j in i:
#           j.disabled=True

#     await interaction.edit_origin(content=msg, components=buttonsLTT)

import Games.Connect4 as C4  # Connect 4 или Четыре в ряд

gameC4 = None
stateC4 = 0
msgC4 = None
firstNameC4 = ''
secondNameC4 = ''
numbersC4 = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣']


def forImport3(bot):
    @bot.command()  # Вход в игру крестики-нолики
    async def фишки(ctx, *args):
        if not gameChannel(bot, ctx.channel):
            return
        global gameC4
        global stateC4
        global msgC4
        global firstNameC4
        global secondNameC4
        global numbersC4

        if stateC4 == 0:
            stateC4 = 1
            firstNameC4 = ctx.author
            await ctx.send(
                f'Первый игрок в фишки принят: {firstNameC4.name}\nОжидание второго игрока...'
            )

        elif stateC4 == 1:
            stateC4 = 2
            secondNameC4 = ctx.author
            gameC4 = C4.C4()
            gameC4.firstName = firstNameC4.name
            gameC4.secondName = secondNameC4.name
            await ctx.send(
                f'Второй игрок в фишки принят: {secondNameC4.name}\nТеперь можно начинать. Для выйгрыша положите 4 фишки в ряд. Чтобы сделать ход на второй столбец, нажмите на вторую реакцию в следующем сообщении. Если никто не будет ходить более 10 минут, то игра закончится. Первым ходит {firstNameC4.name} с красными фишками. Начинаем!'
            )
            msgC4 = await ctx.send(
                f'Каков ваш ход за красные фишки, {firstNameC4.name}?')

            for i in numbersC4:
                await msgC4.add_reaction(i)
            msgC4Image = await ctx.send(file=discord.File("Games/AreaC4.png"))

            isfirst = True
            while not gameC4.isEnd():
                if isfirst:
                    move = await C4React(msgC4, firstNameC4)
                else:
                    move = await C4React(msgC4, secondNameC4)
                isfirst = not isfirst
                if move == 7:
                    await ctx.send(
                        'Прошло 10 минут с момента последнего действия. Теперь игра считается завершённой.'
                    )
                    break

                text = gameC4.userMove(move)
                await msgC4.edit(content=text)
                await msgC4Image.delete()
                msgC4Image = await ctx.send(
                    file=discord.File("Games/AreaC4.png"))

            await msgC4.clear_reactions()
            stateC4 = 0
            gameC4 = None

        else:
            if args and args[0].lower() == 'сброс':
                await msgC4.clear_reactions()
                stateC4 = 0
                gameC4 = None
                await ctx.send(
                    f'Текущая игра между {firstNameC4.name} и {secondNameC4.name} была сброшена! Для начала новой заново пропишите команду "!фишки".'
                )
            else:
                msg = await ctx.send(
                    f'Сейчас проходит игра между {firstNameC4.name} и {secondNameC4.name}. Она будет сброшена после 10 минут бездействия. Для ручного сброса пропишите команду "!фишки сброс".'
                )
                await deleteMsg(msg, 15)

    async def C4React(msg, name):
        global numbersC4
        timeout = 600.0  # Время ожидания ответа

        def check(reaction, user):
            return user == name and str(reaction.emoji) in numbersC4

        while True:
            try:
                reaction, user = await bot.wait_for('reaction_add',
                                                    timeout=timeout)
                if user != msg.author:
                    await msg.remove_reaction(reaction, user)
                if check(reaction, user):
                    return numbersC4.index(str(reaction.emoji))

            except asyncio.TimeoutError:
                return 7


import Games.Tiles as Tiles  # Игра "2048"

gameT = None
stateT = 0
msgT1 = None
msgT2 = None
userT = ''
movesT = ['⬅️', '⬆️', '⬇️', '➡️']


def forImport4(bot):
    return

    DiscordComponents(bot)

    @bot.command()  # Игра "2048"
    async def плитки(ctx, *args):
        if not gameChannel(bot, ctx.channel):
            return
        global gameT
        global stateT
        global msgT1
        global msgT2
        global userT
        global movesT
        global numOfButtonGames
        timeout = 600.0  # Время ожидания ответа

        if args and args[0] == 'рекорды':  # Для чтения рекордов
            lines = None
            with open('Games/Tiles.txt', 'r') as f:
                x = f.read()
                if not x:
                    await ctx.send('Рекордов нет, никто не играет...')
                    return
                lines = x.split('\n')
            msg = ''
            if len(lines) > 3:
                msg += 'Вот топ-3 результатов:\n'
                for i in range(3):
                    msg += f'{i+1}) {lines[i]}\n'
            else:
                msg += 'Вот результаты:\n'
                for i in range(len(lines)):
                    msg += f'{i+1}) {lines[i]}\n'
            await ctx.send(msg.strip())
            return

        async def writeRec(result, name):  # Для записи рекордов
            lines = None
            with open('Games/Tiles.txt', 'r') as f:
                x = f.read()
                if x:
                    lines = x.split('\n')
            if not lines:
                with open('Games/Tiles.txt', 'w') as f:  # если последнее место
                    f.write(f'{name} - {result} очков ({DT.date.today()})')
                    return
            for i in lines:
                if int(i.split(' ')[2]) < result:
                    text = ''
                    for j in lines:
                        if j == i:
                            text += f'{name} - {result} очков ({DT.date.today()})\n'
                        text += j + '\n'
                    with open('Games/Tiles.txt', 'w') as f:
                        f.write(text.strip())
                    return
            with open('Games/Tiles.txt', 'w') as f:  # если последнее место
                f.write('\n'.join(lines).strip() +
                        f'\n{name} - {result} очков ({DT.date.today()})')

        tempMoves = []
        for i in movesT:
            tempMoves.append({"id": None, "name": i, "animated": False})

        if stateT == 0:
            ids = [
                'buttonEmp1', 'buttonUp', 'buttonEmp2', 'buttonLeft',
                'buttonDown', 'buttonRight'
            ]
            numOfButtonGames += 1
            thisNumOfButtonGames = numOfButtonGames
            for i in range(len(ids)):
                ids[i] += str(numOfButtonGames)
            buttonEmp1 = Button(label=" ", custom_id=ids[0], disabled=True)
            buttonUp = Button(label=" ", custom_id=ids[1], emoji=tempMoves[1])
            buttonEmp2 = Button(label=" ", custom_id=ids[2], disabled=True)
            buttonLeft = Button(label=" ",
                                custom_id=ids[3],
                                emoji=tempMoves[0])
            buttonDown = Button(label=" ",
                                custom_id=ids[4],
                                emoji=tempMoves[2])
            buttonRight = Button(label=" ",
                                 custom_id=ids[5],
                                 emoji=tempMoves[3])

            stateT = 1
            userT = ctx.author
            gameT = Tiles.Tiles()
            msgT1 = await ctx.send(
                'Используйте эти кнопки для управления!',
                components=[[buttonEmp1, buttonUp, buttonEmp2],
                            [buttonLeft, buttonDown, buttonRight]])
            # if args and args[0]=='генерация': # для отладки
            #   gameT.generateGames/Area([
            #     [2**2,2**3,2**4,0],
            #     [2**8,2**7,2**6,2**5],
            #     [2**9,2**10,2**11,2**12],
            #     [2**16,2**15,2**14,2**13],
            #   ])

            msgT2 = await ctx.reply(file=discord.File('Games/AreaT.png'))

            while not gameT.isEnd():
                try:
                    interaction = await bot.wait_for(
                        "button_click",
                        check=lambda i: i.custom_id in ids,
                        timeout=timeout)

                except asyncio.TimeoutError:
                    if thisNumOfButtonGames != numOfButtonGames:
                        return
                    await ctx.send(
                        f'Текущая игра пользователя {userT.name} была сброшена с {gameT.theScore()} очками из-за длительного бездействия.'
                    )
                    await writeRec(gameT.theScore(), userT)
                    await msgT1.delete()
                    stateT = 0
                    return

                if interaction.user != userT:
                    await interaction.send(
                        f'На данный момент идёт игра пользователя {userT.name}. Для её сброса напишите "!плитки сброс".'
                    )
                    continue

                msg = ''
                if interaction.custom_id == ids[1]:
                    arrow = 1
                    msg += 'Плитки сдвинуты вверх. '
                elif interaction.custom_id == ids[3]:
                    arrow = 0
                    msg += 'Плитки сдвинуты влево. '
                elif interaction.custom_id == ids[4]:
                    arrow = 2
                    msg += 'Плитки сдвинуты вниз. '
                elif interaction.custom_id == ids[5]:
                    arrow = 3
                    msg += 'Плитки сдвинуты вправо. '

                gameT.userMove(arrow)
                if not gameT.isMoved():
                    msg = 'Плитки нельзя сдвинуть в данном направлении.'
                if gameT.isEnd():
                    msg += f'Игра завершена с {gameT.theScore()} очками!'

                await msgT2.delete()
                msgT2 = await interaction.send(
                    msg, file=discord.File('Games/AreaT.png'), ephemeral=False)

            await writeRec(gameT.theScore(), userT)
            await msgT1.delete()
            stateT = 0

        else:

            if args and args[0] == 'сброс':
                await ctx.send(
                    f'Текущая игра пользователя {userT.name} была сброшена с {gameT.theScore()} очками! Для начала новой используйте команду "!плитки".'
                )
                await writeRec(gameT.theScore(), userT)
                await msgT1.delete()
                stateT = 0
                return

            if args and args[0] == 'кнопки':
                await msgT1.delete()
                msgT1 = await ctx.send(
                    'Используйте эти кнопки для управления!',
                    components=[[buttonEmp1, buttonUp, buttonEmp2],
                                [buttonLeft, buttonDown, buttonRight]])
                return

            msg = await ctx.send(
                f'Для игры необходимо использовать кнопки. Если хотите сбросить игру пользователя {userT.name}, то напишите команду "!плитки сброс". Если необходимо поставить кнопки поближе к началу, используйте команду "!плитки кнопки".'
            )
            await deleteMsg(msg, 15)
            return
