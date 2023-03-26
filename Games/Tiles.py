import random
from PIL import Image, ImageDraw, ImageFont
size = 40
lsize = 5
stysize = 15
stxsize = 3
box = size + lsize

class Tiles:
  __len = 4
  __wid = 4
  __isrand = False

  __area = [] # Число
  __emptySlots = 16
  
  __isend = False
  def isEnd(self):
    return self.__isend
  
  __score = 0
  def theScore(self):
    return self.__score

  __ismoved = True # Двигались ли плитки
  def isMoved(self):
    return self.__ismoved

  
  def __init__(self):
    self.newGame()


  def newGame(self):
    seed = random.randint(0, 2147483647)
    random.seed(seed)
    log(f'Новая игра (seed: {seed})') # Часть логирования

    self.__emptySlots = self.__len*self.__wid
    self.__isend = False
    self.__area = []
    for i in range(self.__len):
      self.__area.append([])
      for j in range(self.__wid):
        self.__area[i].append(0)
    self.randAdd()
    self.createPng()

  
  def randAdd(self):
    rand = random.randint(1, self.__emptySlots)
    num = 0
    for i in range(self.__len):
      for j in range(self.__wid):
        if self.__area[i][j] > 0:
          continue
        num += 1
        if num == rand:
          x = random.choice([2,2,2,2,2,2,2,2,2,4])
          self.__score += x
          self.__area[i][j] = x
          self.__emptySlots -= 1
          log(f'Генерация {x} в клетке на {i} {j}') # Часть логирования
          return


  def nextMove(self, arrow): # 0=влево, 1=вверх, 2=вниз, 3=вправо
    if self.isEnd():
      return
    self.__ismoved = False # пока не было движений
    
    if arrow == 0: # влево
      for i in range(0, self.__len):
        for j in range(1, self.__wid):
          if self.__area[i][j] == 0:
            continue
          for k in range(j, 0, -1):
            if self.__area[i][k-1] == 0:
              self.__area[i][k-1] = self.__area[i][k]
              self.__area[i][k] = 0
              self.__ismoved = True
              continue
            if self.__area[i][k] == self.__area[i][k-1]:
              self.__area[i][k-1] *= 2
              self.__area[i][k] = 0
              self.__emptySlots += 1
              self.__ismoved = True
              continue
            break

    elif arrow == 1: # вверх
      for j in range(0, self.__wid):
        for i in range(1, self.__len):
          if self.__area[i][j] == 0:
            continue
          for k in range(i, 0, -1):
            if self.__area[k-1][j] == 0:
              self.__area[k-1][j] = self.__area[k][j]
              self.__area[k][j] = 0
              self.__ismoved = True
              continue
            if self.__area[k][j] == self.__area[k-1][j]:
              self.__area[k-1][j] *= 2
              self.__area[k][j] = 0
              self.__emptySlots += 1
              self.__ismoved = True
              continue
            break

    elif arrow == 2: # вниз
      for j in range(0, self.__wid):
        for i in range(self.__len-2, -1, -1):
          if self.__area[i][j] == 0:
            continue
          for k in range(i, self.__len-1):
            if self.__area[k+1][j] == 0:
              self.__area[k+1][j] = self.__area[k][j]
              self.__area[k][j] = 0
              self.__ismoved = True
              continue
            if self.__area[k][j] == self.__area[k+1][j]:
              self.__area[k+1][j] *= 2
              self.__area[k][j] = 0
              self.__emptySlots += 1
              self.__ismoved = True
              continue
            break

    else: # вправо
      for i in range(0, self.__len):
        for j in range(self.__wid-2, -1, -1):
          if self.__area[i][j] == 0:
            continue
          for k in range(j, self.__wid-1):
            if self.__area[i][k+1] == 0:
              self.__area[i][k+1] = self.__area[i][k]
              self.__area[i][k] = 0
              self.__ismoved = True
              continue
            if self.__area[i][k] == self.__area[i][k+1]:
              self.__area[i][k+1] *= 2
              self.__area[i][k] = 0
              self.__emptySlots += 1
              self.__ismoved = True
              continue
            break

    msg = ''
    if arrow == 0: # Часть логирования
      msg = 'Ход влево'
    elif arrow == 1:
      msg = 'Ход вверх'
    elif arrow == 2:
      msg = 'Ход вниз'
    else:
      msg = 'Ход вправо'
    if not self.isMoved():
      msg += ' не совершён'
    log(msg) # Часть логирования

    if self.isMoved():
      self.randAdd()
      self.createPng()
      self.checkEnd()

  
  def checkEnd(self):
    if self.__emptySlots:
      return

    for i in range(1, self.__len - 1): # Проверка пар центров
      for j in range(1, self.__wid - 1):
        if self.__area[i][j] in (self.__area[i][j+1], self.__area[i][j-1], self.__area[i+1][j], self.__area[i-1][j]):
          return
          
    for i in range(self.__len - 1): # Проверка пар границ по длине
      if self.__area[i][0] == self.__area[i+1][0] or self.__area[i][self.__wid-1] == self.__area[i+1][self.__wid-1]:
        return
          
    for j in range(self.__wid - 1): # Проверка пар границ по ширине
      if self.__area[0][j] == self.__area[0][j+1] or self.__area[self.__len-1][j] == self.__area[self.__len-1][j+1]:
        return

    
    
    self.__isend = True
    log(f'Игра окончена c {self.theScore()} очками')

  
  def createPng(self):
    allLen = self.__len * box + lsize
    allWid = self.__wid * box + lsize
    img = Image.new('RGBA', (allWid, allLen), '#C44C22')
    idraw = ImageDraw.Draw(img)
    
    for i in range(self.__len):
      y = box*i+lsize
      for j in range(self.__wid):
        x = box*j+lsize
        if not self.__area[i][j]:
          idraw.rectangle((x,y,x+size,y+size), '#FBA872')
          continue
        col = '#FB9A3B'
        if self.__area[i][j] > 16:
          if self.__area[i][j] < 512:
            col = '#FF7F00'
          elif self.__area[i][j] < 8192:
            col = '#EC612A'
          elif self.__area[i][j] != 131072:
            col = '#AE3113'
          else:
            col = '#000000'
        text = str(self.__area[i][j])
        idraw.rectangle((x,y,x+size,y+size), col)
        idraw.text((x+stxsize*(7-len(text)),y+stysize), text,'#FFFFFF')
  
    img.save('Games/AreaT.png')


  def userMove(self, arrow):
    self.nextMove(arrow)


  def generateArea(self, a):  # для отладки
    self.__emptySlots = 0
    self.__score = 0
    for i in range(self.__len):
      for j in range(self.__wid):
        self.__area[i][j] = a[i][j]
        self.__score += a[i][j]
        if a[i][j] == 0:
          self.__emptySlots += 1
    self.createPng()



import datetime as DT
def log(msg):
  with open('Games/game.log', 'a') as f:
    if msg.startswith('Новая игра'):
      f.write('\n'*2)
    f.write(f'{DT.datetime.now().replace(microsecond=0)} - T: {msg}\n')