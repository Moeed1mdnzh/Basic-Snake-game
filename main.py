import pygame
from Frontend import Frontend
import Board
import random
import time
frontend = Frontend()
none = None
class main:
	def __init__(self,key=pygame.key.get_pressed(),buttons=Board.buttons(),game_over=pygame.font.SysFont("arial",60),speed=[0,0]):
		#defining necessary variables
		global none
		self.key = key
		self.buttons = buttons
		self.l = self.buttons[0]
		self.r = self.buttons[1]
		self.d = self.buttons[2]
		self.u = self.buttons[3]
		self.game_over = game_over
		self.speed = speed
		self.foodc = [random.randint(50,450),random.randint(50,450)]
		self.xsnake = 250
		self.ysnake = 250
		self.NotgameOver = False
		self.fill = Board.board.fill
		self.n = 1
		self.slength = []
	def keys(self):
		#defining keys for movements
		self.key = pygame.key.get_pressed()
		if self.key[self.l]:
			self.speed[0] = 30
			self.speed[1] = 0
		elif self.key[self.r]:
			self.speed[0] = -30
			self.speed[1] = 0
		elif self.key[self.d]:
			self.speed[0] = 0
			self.speed[1] = -30
		elif self.key[self.u]:
			self.speed[0] = 0
			self.speed[1] = 30
		for s in Board.returnSnake(self.xsnake).items():
			if s[1]:
				pass
			else:
				self.NotgameOver= True
				if none != None:
					gameOver().playerChoice()
		for s in Board.returnSnake(self.ysnake).items():
			if s[1]:
				pass
			else:
				self.NotgameOver = True
				if none != None:
					gameOver().playerChoice()
	def snake_in_food(self,xs,ys):
		if True:
			if xs[1] in range(xs[0],xs[0]+30) and ys[1] in range(ys[0],ys[0]+30):
				self.foodc = [random.randint(50,450),random.randint(50,450)]
				frontend.c_score = str(int(frontend.c_score)+1) 
				self.n += 1
			elif xs[1]+20 in range(xs[0],xs[0]+30) and ys[1]+20 in range(ys[0],ys[0]+30):
				self.foodc = [random.randint(50,450),random.randint(50,450)]
				frontend.c_score = str(int(frontend.c_score)+1) 
				self.n += 1
	def add_snake(self,snake_length):
		for i in snake_length:
			pygame.draw.rect(Board.board,(80,120,0),[i[0],i[1],30,30])
class Game(main):
	#The game
	def gameLoop(self):
		while not self.NotgameOver:
			pygame.time.delay(100)
			self.xV = self.xsnake
			self.yV = self.ysnake
			self.xsnake -= self.speed[0]
			self.ysnake -= self.speed[1]
			frontend.render_display([self.xsnake,self.foodc[0]],[self.ysnake,self.foodc[1]])
			self.keys()
			self.snake_head = []
			self.snake_head.append(self.xsnake)
			self.snake_head.append(self.ysnake)
			self.slength.append(self.snake_head)
			if len(self.slength) > self.n:
				del self.slength[0]
			self.add_snake(self.slength)
			self.snake_in_food([self.xsnake,self.foodc[0]],[self.ysnake,self.foodc[1]])
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				pygame.display.update()
			pygame.display.update()
			self.fill((255,255,255))


class gameOver(Game):
	def playerChoice(self):
		#Here we want to see if the player wants to continue playing
		none = None
		self.Font1 = pygame.font.SysFont('arial',60,'light')
		self.Font2 = Font2=pygame.font.SysFont('arial',25,'light')
		self.color = (255,255,255)
		self.text1 = self.Font1.render("YOU LOST",True,self.color)
		self.text2 = [self.Font2.render("R-Replay",True,self.color),self.Font2.render("Q-Quit",True,self.color)]
		self.q,self.r = pygame.K_q,pygame.K_r
		self.choice = True
		while self.choice:
			self.key = pygame.key.get_pressed()
			Board.board.fill((0,0,0))
			Board.board.blit(self.text1,(150,180))
			Board.board.blit(self.text2[0],(250,250))
			Board.board.blit(self.text2[1],(250,290))
			if self.key[self.q]:
				self.Quit()
				pygame.quit()
				quit()
			elif self.key[self.r]:
				frontend.c_score = '0'
				Game().gameLoop()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				pygame.display.update()
			pygame.display.update()

	def Quit(self):
		self.choice = False


if __name__ == "__main__":
	game = Game()
	game.gameLoop()
	gameOver().playerChoice()
