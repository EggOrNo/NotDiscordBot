class C4:
  __wid = 7
  __len = 6
  __winsize = 4
  __area = []
  firstName = ''
  secondName = ''
  __state = 0
  
  __isend = 0
  def isEnd(self):
    return self.__isend


  def __init__(self):
    self.newGame()
    

  def newGame(self):
    self.__isend = 0
    self.__state = 0
    self.__area = []
    for i in range(self.__len):
      self.__area.append([])
      for j in range(0, self.__wid):
        self.__area[i].append(0)
    createPng(self.__len, self.__wid)


  def nextMove(self, x):
    if self.isEnd() != 0:
      if self.isEnd() == 1:
        return f'Игра уже завершена! Выйграл первый игрок - {self.firstName}.'
      elif self.isEnd() == 2:
        return f'Игра уже завершена! Выйграл второй игрок - {self.secondName}.'
      else:
        return 'Игра уже завершена! Это ничья.'

    if self.__area[0][x]:
      return f'Столбец {x+1} занят! Повторите попытку'

    y=0
    while y+1 < self.__len and self.__area[y+1][x] == 0:
      y+=1
    if self.__state % 2 == 0:
      self.__area[y][x] = 1
      newDraw(x, y, False)
    else:
      self.__area[y][x] = 2
      newDraw(x, y, True)
    self.__state += 1
    

    for i in range(0, self.__len - self.__winsize + 1):
      for j in range(0, self.__wid - self.__winsize + 1): # Проверяются все коробки winsize на winsize

        for k1 in range(i, i + self.__winsize): # Горизонтальные линии
          if self.__area[k1][j] == 0:
            continue
          check = True
          for k2 in range(j + 1, j + self.__winsize):
            if self.__area[k1][j] != self.__area[k1][k2]:
              check = False
              break
          if check:
            self.__isend = self.__area[k1][j]
            break

        for k1 in range(j, j + self.__winsize): # Вертикальные линии
          if self.__area[i][k1] == 0:
            continue
          check = True
          for k2 in range(i + 1, i + self.__winsize):
            if self.__area[i][k1] != self.__area[k2][k1]:
              check = False
              break
          if check:
            self.__isend = self.__area[i][k1]
            break

        if self.__area[i][j] != 0:
          check = True
          for k1 in range(1, self.__winsize): # Диагональ левая верхняя
            if self.__area[i][j] != self.__area[i + k1][j + k1]:
              check = False
              break
          if check:
            self.__isend = self.__area[i][j]
            break

        if self.__area[i][j + self.__winsize - 1] != 0:
          check = True
          for k1 in range(1, self.__winsize): # Диагональ правая верхняя
            if self.__area[i][j + self.__winsize - 1] != self.__area[i + k1][j + self.__winsize - 1 - k1]:
              check = False
              break
          if check:
            self.__isend = self.__area[i][j + self.__winsize - 1]
            break
        
        if self.isEnd() != 0:
          break
      if self.isEnd() != 0:
          break
    

    if self.isEnd() == 0: # Простая проверка ничьи
      z = 1
      for i in self.__area:
        for j in i:
          if j == 0:
            z = 0
      if z:
        self.__isend = 3
    
    if self.isEnd() != 0: # Проверка завершилась ли игра этим ходом
      if self.isEnd() == 1:
        return f'Игра завершена! Выйграл первый игрок - {self.firstName}'
      elif self.isEnd() == 2:
        return f'Игра завершена! Выйграл второй игрок - {self.secondName}'
      else:
        return 'Игра завершена! Это ничья'

    return f'Ход в {x+1} столбце выполнен.'



  def userMove(self, x): # Должен возвращать значение
    text = ''
    if self.__state % 2 == 0:
      text += self.nextMove(x)
      if text.startswith('Столбец'): 
        return f'{text} за красных, {self.firstName}.'
      if self.isEnd() == 0:
        text += f'\nКаков ваш ход за жёлтые фишки, {self.secondName}?'
    
    else:
      text += self.nextMove(x)
      if text.startswith('Столбец'):
        return f'{text} за жёлтых, {self.secondName}.'
      if self.isEnd() == 0:
        text += f'\nКаков ваш ход за красные фишки, {self.firstName}?'
    
    return text


size = 44
l = 4
lsize = l + 2
box = size + l
import Image, ImageDraw
def createPng(bLen, bWid):
  img = Image.new('RGBA', (box*bWid+l, box*bLen+l), '#B0B0B0')
  idraw = ImageDraw.Draw(img)
  
  for i in range(bLen):
    for j in range(bWid):
      idraw.rectangle( (j*box+l, i*box+l, (j+1)*box, (i+1)*box), fill='#808080')
      idraw.ellipse( (j*box+lsize, i*box+lsize, (j+1)*box+l-lsize, (i+1)*box+l-lsize), fill='#C0C0C0')
  img.save('Games/AreaC4.png')
  
def newDraw(x, y, second):
  x = box * x
  y = box * y
  color1 = '#AA0000' if second is False else '#AAAA00'
  color2 = '#DD0000' if second is False else '#DDDD00'

  img = Image.open('Games/AreaC4.png')
  idraw = ImageDraw.Draw(img)
  idraw.ellipse( (x+lsize, y+lsize, x+box+l-lsize, y+box+l-lsize), fill=color1)
  idraw.ellipse( (x+lsize+l, y+lsize+l, x+box-lsize, y+box-lsize), fill=color2)
  img.save('Games/AreaC4.png')