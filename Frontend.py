import pygame
import Board



class Frontend:
	def __init__(self,c_score='0',font=pygame.font.SysFont("arial",40),score="score : "):
		#defining necessary variables
		self.font = font
		self.score = score
		self.c_score = c_score

	def render_display(self,x,y):
		#displaying the score
		self.score_text = self.font.render(self.score + self.c_score,True,(0,0,0))
		Board.board.blit(self.score_text,(10,10))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		self.food(x[1],y[1])
		self.snake(x[0],y[0])
		Board.board.blit(self.score_text,(10,10))



	def snake(self,x,y):
		#our snake
		pygame.draw.rect(Board.board,(50,130,50),(x,y,30,30))

	def food(self,x,y):
		#our food
		pygame.draw.rect(Board.board,(200,200,0),(x,y,20,20))

