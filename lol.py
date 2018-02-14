# Basic Pacman
import pygame, sys, os
from pygame.locals import *

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path

ghostcolor = {}
ghostcolor[0] = (255, 0, 0, 255)
ghostcolor[1] = (255, 128, 255, 255)
ghostcolor[2] = (128, 255, 255, 255)
ghostcolor[3] = (255, 128, 0, 255)
ghostcolor[4] = (50, 50, 255, 255)
ghostcolor[5] = (255, 255, 255, 255) # white, flashing ghost

pygame.init()

class game ():
    def __init__ (self):
        self.gmode = 0
    
class pacman ():

    def __init__ (self):
        self.x = 200
        self.y = 200
        self.velx = 0
        self.vely = 0
        self.speed = 6
        
        self.nearestRow = 0
        self.nearestCol = 0
        
        self.baseX = 0
        self.baseY = 0

        self.currentPath = ""

        self.pac_anim_left = {}
        self.pac_anim_right = {}
        self.pac_anim_up = {}
        self.pac_anim_down = {}
        self.pac_anim_exist = {}
        self.pac_anim_current = {}

        for i in range(1, 9):
            self.pac_anim_left[i] = pygame.image.load(os.path.join(image_path,"pacman","pacman_left_f" + str(i) + ".gif")).convert()
            self.pac_anim_right[i] = pygame.image.load(os.path.join(image_path,"pacman","pacman_right_f" + str(i) + ".gif")).convert()
            self.pac_anim_up[i] = pygame.image.load(os.path.join(image_path,"pacman","pacman_up_f" + str(i) + ".gif")).convert()
            self.pac_anim_down[i] = pygame.image.load(os.path.join(image_path,"pacman","pacman_down_f" + str(i) + ".gif")).convert()
            self.pac_anim_exist[i] = pygame.image.load(os.path.join(image_path,"pacman","pacman_exist.gif")).convert()

        self.pac_anim_current = self.pac_anim_right
        self.animFrame = 3
        
    def Draw (self):
        screen.blit(self.pac_anim_current[self.animFrame], (self.x,self.y))
        self.animFrame += 1
        if self.animFrame == 9:
            self.animFrame = 1

    def Move (self):
        self.x += self.velx
        self.y += self.vely
        
def CheckInputs():
    if pygame.key.get_pressed()[ pygame.K_RIGHT ]:
        player.pac_anim_current = player.pac_anim_right
        player.velx=player.speed
        player.vely=0
        
        
    elif pygame.key.get_pressed()[ pygame.K_LEFT ]:
        player.pac_anim_current = player.pac_anim_left
        player.velx=-player.speed
        player.vely=0
        
    elif pygame.key.get_pressed()[ pygame.K_UP ]:
        player.pac_anim_current = player.pac_anim_up
        player.velx=0
        player.vely=-player.speed
        
    elif pygame.key.get_pressed()[ pygame.K_DOWN ]:
        player.pac_anim_current = player.pac_anim_down
        player.velx=0
        player.vely=player.speed
    elif pygame.key.get_pressed()[ pygame.K_DOWN ]:
        player.pac_anim_current = player.pac_anim_down
        player.velx=0
        player.vely=player.speed


window_size = (800,500)
player_scale = (30,30)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pacman Multiplayer(lol)")
screen = pygame.display.get_surface()
bg = pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'bg1.png')), window_size).convert()
screen.blit(bg, (0,0))

player = pacman()
while 1:
    screen.blit(bg, (0,0))
    pygame.event.pump()
    CheckInputs()
    player.Move()
    player.Draw()
    pygame.time.delay(30)
    pygame.display.update()
