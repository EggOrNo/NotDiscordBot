class TTT:
  __boxsize = 3
  __winsize = 3
  __area = []
  firstName = ''
  secondName = ''
  __state = 0
  
  __isend = 0
  def isEnd(self):
    return self.__isend

  def __init__(self, boxsize = 3, winsize = 3):
    self.__boxsize = boxsize
    self.__winsize = winsize
    self.newGame()

  def newGame(self):
    self.__isend = 0
    self.__state = 0
    self.__area = []
    for i in range(0, self.__boxsize):
      self.__area.append([])
      for j in range(0, self.__boxsize):
        self.__area[i].append(' ')
    createPng(self.__boxsize)

  # def printArea(self): # ТЕКСТОВЫЙ ВЫВОД
  #   lines = ''
  #   for i in range(0, self.__boxsize):
  #     for j in range(0, self.__boxsize):
  #       lines += self.__area[i][j]
  #       if j != self.__boxsize - 1:
  #         lines += '│'
  #     lines += '\n'

  #     if i != self.__boxsize - 1:
  #       for j in range(0, self.__boxsize):
  #         if j < self.__boxsize - 1:
  #           lines += '─┼'
  #         else:
  #           lines += '─'
  #       lines += '\n'
  #   return lines
  

  def nextMove(self, y, x):
    if self.isEnd() != 0:
      if self.isEnd() == 'X':
        return 'Игра уже завершена! Выйграл первый игрок - ' + self.firstName[:-5]
      elif self.isEnd() == 'O':
        return 'Игра уже завершена! Выйграл второй игрок - ' + self.secondName[:-5]
      else:
        return 'Игра уже завершена! Это ничья'

    if self.__area[y][x] != ' ':
      return 'Это место занято! Повторите попытку, '

    if self.__state % 2 == 0:
      self.__area[y][x] = 'X'
      newX(x, y)
    else:
      self.__area[y][x] = 'O'
      newO(x, y, self.__boxsize)
    self.__state += 1
    

    for i in range(0, self.__boxsize - self.__winsize + 1):
      for j in range(0, self.__boxsize - self.__winsize + 1): # Проверяются все коробки winsize на winsize

        for k1 in range(i, i + self.__winsize): # Горизонтальные линии
          if self.__area[k1][j] == ' ':
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
          if self.__area[i][k1] == ' ':
            continue
          check = True
          for k2 in range(i + 1, i + self.__winsize):
            if self.__area[i][k1] != self.__area[k2][k1]:
              check = False
              break
          if check:
            self.__isend = self.__area[i][k1]
            break

        if self.__area[i][j] != ' ':
          check = True
          for k1 in range(1, self.__winsize): # Диагональ левая верхняя
            if self.__area[i][j] != self.__area[i + k1][j + k1]:
              check = False
              break
          if check:
            self.__isend = self.__area[i][j]
            break

        if self.__area[i][j + self.__winsize - 1] != ' ':
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
          if j == ' ':
            z = 0
      if z:
        self.__isend = 'Z'

    
    if self.isEnd() != 0: # Завершение игры на этом ходу
      if self.isEnd() == 'X':
        return 'Игра завершена! Выйграл первый игрок - ' + self.firstName[:-5]
      elif self.isEnd() == 'O':
        return 'Игра завершена! Выйграл второй игрок - ' + self.secondName[:-5]
      else:
        return 'Игра завершена! Это ничья'

    return ' '


  def tictac(self, y, x, name): # должен возвращаться значение
    text = ''
    if self.__state % 2 == 0 and self.firstName == name:
      y = (y - 1) % self.__boxsize
      x = (x - 1) % self.__boxsize
      text += self.nextMove(y, x)
      if text[0] == 'Э':
        return text + name[:-5]
      if self.isEnd() == 0:
        text += f'\nКаков ваш ход за O, {self.secondName[:-5]}?'
    
    elif self.__state % 2 == 1 and self.secondName == name:
      y = (y - 1) % self.__boxsize
      x = (x - 1) % self.__boxsize
      text += self.nextMove(y, x)
      if text[0] == 'Э':
        return text + name[:-5]
      if self.isEnd() == 0:
        text += f'\nКаков ваш ход за X, {self.firstName[:-5]}?'
    
    elif self.isEnd() == 0:
      return 'Сейчас не ваш ход, ' + name[:-5]
    

    return text


size = 50
lsize = 5
box = size + lsize
import Image, ImageDraw
def createPng(boxsize):
  fullBox = box * boxsize - lsize
  img = Image.new('RGBA', (fullBox, fullBox), 'white')    
  idraw = ImageDraw.Draw(img)
  if boxsize % 2 == 1:
    for i in range(1, boxsize * boxsize, 2):
      idraw.rectangle(((i%boxsize)*box, (i//boxsize)*box, (i%boxsize)*box+size, (i//boxsize)*box+size), fill='#E0E0E0')
  else:
    for i in range(1, boxsize * boxsize, 2):
      if i // boxsize % 2 == 0:
        idraw.rectangle(((i%boxsize)*box, (i//boxsize)*box, (i%boxsize)*box+size, (i//boxsize)*box+size), fill='#E0E0E0')
      else:
        idraw.rectangle(((i%boxsize - 1)*box, (i//boxsize)*box, (i%boxsize - 1)*box+size, (i//boxsize)*box+size), fill='#E0E0E0')

  for i in range(1, boxsize):
    idraw.rectangle((box * i - lsize, 0, box * i, fullBox), fill='black')
    idraw.rectangle((0, box * i - lsize, fullBox, box * i), fill='black')
  img.save('Games/AreaTTT.png')
  
def newX(x, y):
  x = box * x
  y = box * y
  l = size / 5
  r = size - l
  img = Image.open('Games/AreaTTT.png')
  idraw = ImageDraw.Draw(img)
  idraw.line((l + x, l + y, r + x, r + y), fill='red', width=5)
  idraw.line((l + x, r + y, r + x, l + y), fill='red', width=5)
  img.save('Games/AreaTTT.png')
  
def newO(x, y, boxsize):
  col = 'white'
  if boxsize % 2 == 1:
    if (y*boxsize + x) % 2 == 1:
      col = '#E0E0E0'
  else:
    if (y + x) % 2 == 1:
      col = '#E0E0E0'

  x = box * x
  y = box * y
  l = size / 5
  r = size - l
  img = Image.open('Games/AreaTTT.png')
  idraw = ImageDraw.Draw(img)
  idraw.ellipse((l + x, l + y, r + x, r + y), fill=col, outline='#0000FF', width=4)
  img.save('Games/AreaTTT.png')