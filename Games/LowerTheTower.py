import random
import Image, ImageDraw
size = 50
lsize = 5
box = size + lsize

class LTT:
  __len = 3
  __wid = 3
  __zone = 9
  __isrand = False

  __area = [] # True - опущен (выигрыш), False - поднят
  __areaC = [] # 0 - синие, 1 - красные, 2 - зелёные
  def userCheck(self, y, x):
    return self.__area[y%self.__len][x%self.__wid]
  def userCheckC(self, y, x):
    return self.__areaC[y%self.__len][x%self.__wid]
  
  def lenWid(self):
    return self.__len, self.__wid

  __isend = False
  def isEnd(self):
    return self.__isend
  
  __numChanges = 0
  def numChanges(self):
    return self.__numChanges

  __moves = 0
  def numMoves(self):
    return self.__moves

  def __init__(self, length, wid, ishard):
    self.__len = length
    self.__wid = wid
    self.__zone = length * wid
    self.newGame(ishard)


  def newGame(self, ishard):
    seed = random.randint(0, 2147483647)
    random.seed(seed)
    log(f'Новая игра с полем {self.__len}x{self.__wid} \nseed: {seed}')
    self.__isend = False
    self.__area = []
    self.__areaC = []
    for i in range(0, self.__len):
      self.__area.append([])
      self.__areaC.append([])

      if ishard:
        for j in range(0, self.__wid):
          self.__area[i].append(True) # True - опущен (выигрыш), False - поднят
          self.__areaC[i].append(random.choice([0, 0, 0, 1, 2])) # 0 - синие, 1 - красные, 2 - зелёные
      else:
        for j in range(0, self.__wid):
          self.__area[i].append(True) # True - опущен (выигрыш), False - поднят
          self.__areaC[i].append(0) # 0 - синие
    
    if ishard: # Если всё из синих башен на харде
      check = False
      for i in self.__areaC:
        for j in i:
          if j:
            check = True
            break
        if check:
          break
      if not check:
        self.newGame(ishard)
        return

    msg = '' # Часть логирования
    for i in self.__areaC:
      for j in i:
        msg+= str(j) + ' '
      msg+= '\n'
    msg = 'Цвета башен:\n' + msg 
    log(msg.strip())

    self.randomize()
    self.createPng()


  def randomize(self):
    minimal = [] # Часть логирования
    for i in range(0, self.__len):
      minimal.append([])
      for j in range(0, self.__wid):
        minimal[i].append(False) # True - был изменён

    self.__isrand = True
    circles = random.randint(self.__zone // 2, self.__zone)
    msg = f'Число изменений: {circles}\n' # Часть логирования

    for i in range(0, circles):
      y = random.randint(0, self.__len - 1)
      x = random.randint(0, self.__wid - 1)
      self.nextMove(y, x)
      minimal[y][x] = not minimal[y][x]
    
    self.checkEnd()
    self.__isrand = False
    
    if self.isEnd():
      self.randomize()
    else: # Часть логирования
      msg += 'Поле изменений:\n'
      self.__numChanges = 0
      for i in minimal:
        for j in i:
          if j:
            self.__numChanges += 1
            msg+= '1 '
          else:
            msg += '0 '
        msg.strip()
        msg += '\n'
      msg += f'Минимальное число изменений: {self.__numChanges}\n'
      msg += 'Начальное положение:\n'
      for i in self.__area:
        for j in i:
          if j:
            msg+= '1 '
          else:
            msg+= '0 '
        msg+= '\n'
      log(msg.strip())

  

  def nextMove(self, y, x):
    if self.isEnd():
      return
    
    if not self.__areaC[y][x]:
      self.blueMove(y, x)
    elif self.__areaC[y][x] == 1:
      self.redMove(y, x)
    elif self.__areaC[y][x] == 2:
      self.greenMove(y, x)

    if not self.__isrand:
      log(f'Ход {y} {x}') # Часть логирования
      self.__moves += 1
      self.createPng()
      self.checkEnd()

  def blueMove(self, y, x):
    if self.__areaC[y][x]:
      print('Но это не синий блок!')
      return
      
    self.change(y, x)
    if y == 0:
      self.change(y + 1, x)
    elif y == self.__len - 1:
      self.change(y - 1, x)
    else:
      self.change(y + 1, x)
      self.change(y - 1, x)
    
    if x == 0:
      self.change(y, x + 1)
    elif x == self.__wid - 1:
      self.change(y, x - 1)
    else:
      self.change(y, x + 1)
      self.change(y, x - 1)


  def redMove(self, y, x):
    if self.__areaC[y][x] != 1:
      print('Но это не красный блок!')
      return
      
    self.change(y, x)
    if y == 0:
      if x == 0:
        self.change(y+1, x+1)
      elif x == self.__wid - 1:
        self.change(y+1, x-1)
      else:
        self.change(y+1, x-1)
        self.change(y+1, x+1)
    
    elif y == self.__len - 1:
      if x == 0:
        self.change(y-1, x+1)
      elif x == self.__wid - 1:
        self.change(y-1, x-1)
      else:
        self.change(y-1, x-1)
        self.change(y-1, x+1)
    
    else:
      if x == 0:
        self.change(y+1, x+1)
        self.change(y-1, x+1)
      elif x == self.__wid - 1:
        self.change(y+1, x-1)
        self.change(y-1, x-1)
      else:
        self.change(y-1, x-1)
        self.change(y-1, x+1)
        self.change(y+1, x-1)
        self.change(y+1, x+1)


  def greenMove(self, y, x):
    if self.__areaC[y][x] != 2:
      print('Но это не зелёный блок!')
      return
      
    self.change(y, x)
    if y == 0:
      self.change(y+1, x)
      if x == 0:
        self.change(y, x+1)
        self.change(y+1, x+1)
      elif x == self.__wid - 1:
        self.change(y, x-1)
        self.change(y+1, x-1)
      else:
        self.change(y, x+1)
        self.change(y, x-1)
        self.change(y+1, x-1)
        self.change(y+1, x+1)
    
    elif y == self.__len - 1:
      self.change(y-1, x)
      if x == 0:
        self.change(y, x+1)
        self.change(y-1, x+1)
      elif x == self.__wid - 1:
        self.change(y, x-1)
        self.change(y-1, x-1)
      else:
        self.change(y, x+1)
        self.change(y, x-1)
        self.change(y-1, x-1)
        self.change(y-1, x+1)
    
    else:
      self.change(y+1, x)
      self.change(y-1, x)
      if x == 0:
        self.change(y, x+1)
        self.change(y+1, x+1)
        self.change(y-1, x+1)
      elif x == self.__wid - 1:
        self.change(y, x-1)
        self.change(y+1, x-1)
        self.change(y-1, x-1)
      else:
        self.change(y, x+1)
        self.change(y, x-1)
        self.change(y-1, x-1)
        self.change(y-1, x+1)
        self.change(y+1, x-1)
        self.change(y+1, x+1)



  def change(self, y, x):
    self.__area[y][x] = not self.__area[y][x]
  
  def checkEnd(self):
    for i in range(0, self.__len):
      for j in range(0, self.__wid):
        if not self.__area[i][j]:
          self.__isend = False
          return
    self.__isend = True
    if not self.__isrand:
      log(f'Игра окончена на {self.numMoves()}')

  def createPng(self):
    allLen = self.__len * box + lsize
    allWid = self.__wid * box + lsize
    img = Image.new('RGBA', (allWid, allLen), 'white')
    idraw = ImageDraw.Draw(img)

    for i in range(0, self.__wid + 1):
      idraw.rectangle((box*i, 0, box*i + lsize, allLen), fill='black')
    for i in range(0, self.__len + 1):
      idraw.rectangle((0, box*i, allWid, box*i + lsize), fill='black')
    
    for i in range(0, self.__wid):
      for j in range(0, self.__len):
        if self.__area[j][i]:
          col = '#3333DD'
          if self.__areaC[j][i] == 1:
            col = '#DD3333'
          elif self.__areaC[j][i] == 2:
            col = '#33DD33'
          idraw.rectangle((i*box+lsize, j*box+lsize, i*box+box, j*box+box), fill=col)
        else:
          t = lsize // 2 - 1
          idraw.rectangle((i*box-t+lsize, j*box-t+lsize, i*box+box+t, j*box+box+t), fill='#FFFFFF')

          col = '#3366FF'
          if self.__areaC[j][i] == 1:
            col = '#FF3333'
          elif self.__areaC[j][i] == 2:
            col = '#33FF33'
          idraw.rectangle((i*box+lsize, j*box+lsize, i*box+box, j*box+box), fill=col)

    img.save('Games/AreaLTT.png')

  def userMove(self, y, x):
    y = (y - 1) % self.__len
    x = (x - 1) % self.__wid
    self.nextMove(y, x)


import datetime as DT
def log(msg):
  with open('Games/game.log', 'a') as f:
    if msg.startswith('Новая игра'):
      f.write('\n'*2)
    f.write(f'{DT.datetime.now().replace(microsecond=0)} - LTT: {msg}\n')