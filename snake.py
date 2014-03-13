import pygame
from pygame.locals import *
import random
import math
import time


class SnakeWorld:
  """ This defines the boundaries of the entire playing field as a 640 x 460 rectangle and defines the borders with width 20 x 20"""
  def __init__(self):
    self.blocks=[]
    for x in range(10,630,10):
      for y in range(10,470,10):
        block = Block((255,255,255),10,10,x,y)
        self.blocks.append(block)
    self.food=Food((0,255,0),10,10,random.randrange(10,630,10),random.randrange(10,470,10))
    self.head=Head((0,0,255),10,10,340,240)
    self.headRect=pygame.Rect(self.head.x,self.head.y,self.head.width,self.head.height)
    self.foodRect=pygame.Rect(self.food.x,self.food.y,self.food.width,self.food.height)
    self.boardRect=pygame.Rect(10,10,630,470)
    
  def update(self):
    self.head.update()
    self.headRect=pygame.Rect(self.head.x,self.head.y,self.head.width,self.head.height)
    self.foodRect=pygame.Rect(self.food.x,self.food.y,self.food.width,self.food.height)
    
class Block:
  """This defines the block object for the grid"""
  def __init__(self,color,height,width,x,y):
    self.color = color
    self.height = height
    self.width = width
    self.x = x
    self.y = y
    
class Head:
  def __init__(self,color,height,width,x,y):
    self.color = color
    self.height = height
    self.width = width
    self.x = x
    self.y = y
    self.vx=10.0
    self.vy=0.0
    
  def update(self):
    self.x+=self.vx
    self.y+=self.vy
    
class Tail:
  def __init__(self,color,height,width,x,y):
    self.color = color
    self.height = height
    self.width = width
    self.x = x
    self.y = y
    
class Food:
  """This defines the food object for the grid"""
  def __init__(self,color,height,width,x,y):
    self.color = color
    self.height = height
    self.width = width
    self.x = x
    self.y = y    
    
class PyGameWindowView:
  """This defines the color of the viewing window for the game """
  def __init__(self,model,screen):
        self.model = model
        self.screen = screen
  def draw(self):
    self.screen.fill(pygame.Color(0,0,0))
    for block in self.model.blocks:
      pygame.draw.rect(self.screen, pygame.Color(block.color[0],block.color[1],block.color[2]),pygame.Rect(block.x,block.y,block.width,block.height))
    pygame.draw.rect(self.screen, pygame.Color(self.model.food.color[0],self.model.food.color[1],self.model.food.color[2]),pygame.Rect(self.model.food.x,self.model.food.y,self.model.food.width,self.model.food.height))
    pygame.draw.rect(self.screen, pygame.Color(self.model.head.color[0],self.model.head.color[1],self.model.head.color[2]),pygame.Rect(self.model.head.x,self.model.head.y,self.model.head.width,self.model.head.height))
      
class PyGameController:
    def __init__(self,model):
        self.model = model
        
    def handle_keyboard_event(self,event):
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            if self.model.head.vx==10.0:
                return
            else:
      		self.model.head.vx = -10.0
      		self.model.head.vy = 0.0
        if event.key == pygame.K_RIGHT:
            if self.model.head.vx==-10.0:
                return
            else:
      		self.model.head.vx = 10.0
      		self.model.head.vy = 0.0
        if event.key == pygame.K_UP:
            if self.model.head.vy==10.0:
                return
            else:
      		self.model.head.vx = 0.0
      		self.model.head.vy = -10.0
        if event.key == pygame.K_DOWN:
            if self.model.head.vy==-10.0:
                return
            else:
      		self.model.head.vx = 0.0
      		self.model.head.vy = 10.0
      
      
if __name__ == '__main__':
    pygame.init()
    size = (640,480)
    screen = pygame.display.set_mode(size)

    model = SnakeWorld()
    view = PyGameWindowView(model,screen)
    controller = PyGameController(model)
    
    running = True
    while running:
      	for event in pygame.event.get():
        	if event.type == QUIT:
          		running = False
        	if event.type == KEYDOWN:
          		controller.handle_keyboard_event(event)
        view.draw()
        model.update()
        time.sleep(.1)
        pygame.display.flip()

    pygame.quit()
    
