import pygame
import os
import random

#Variables
width, height = 1000, 600
player_vel = 3
bg_x, bg_y = -500, -500
fps = 60
rock_w, rock_h = 50, 50
tree_w, tree_h = 75, 120
rock_list, tree_list = [], []
clock = pygame.time.Clock()

#Window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Indie Game")

#Player image
player_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_img.png")) , (25 * 1.5, 136/4 * 1.5))
#Background image
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_img.png")), (width + 2*(-bg_x), height + 2*(-bg_y)))
#Rock images
rock_img_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_1.png")), (rock_w, rock_h))
rock_img_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_2.png")), (rock_w, rock_h))
rock_img_3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_3.png")), (rock_w, rock_h))
rock_img_4 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_4.png")), (rock_w, rock_h))
rock_img_5 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_5.png")), (rock_w, rock_h))
rock_img_6 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_6.png")), (rock_w + 25, rock_h + 25))
rock_img_7 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rock_imgs", "rock_img_7.png")), (rock_w + 25, rock_h + 25))
#Tree images
tree_img_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tree_imgs", "tree_img_1.png")), (tree_w, tree_h))
tree_img_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tree_imgs", "tree_img_2.png")), (tree_w, tree_h))
tree_img_3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tree_imgs", "tree_img_3.png")), (59 * 2, 75 * 2))
tree_img_4 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tree_imgs", "tree_img_4.png")), (45 * 2, 69 * 2))
#tree_img_5 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tree_imgs", "tree_img_5.png")), (tree_w, tree_h))
#tree_img_6 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tree_imgs", "tree_img_6.png")), (tree_w, tree_h))
#Removing background of rocks, trees and player
rock_img_1.set_colorkey((255, 255, 255))
rock_img_2.set_colorkey((246, 246, 246))
rock_img_3.set_colorkey((255, 255, 255))
rock_img_4.set_colorkey((220, 240, 244))
rock_img_5.set_colorkey((220, 240, 244))
rock_img_6.set_colorkey((220, 240, 244))
rock_img_7.set_colorkey((220, 240, 244))

tree_img_1.set_colorkey((255, 255, 255))
tree_img_2.set_colorkey((255, 255, 255))
tree_img_3.set_colorkey((255, 255, 255))
tree_img_4.set_colorkey((255, 255, 255))
#tree_img_5.set_colorkey((255, 255, 255))
#tree_img_6.set_colorkey((255, 255, 255))

player_img.set_colorkey((255, 255, 255))

#Player object
class Player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = player_img
    def draw(self):
        """self.Rect = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w, self.h)
        pygame.draw.rect(win, (255, 0, 0), self.Rect)"""
        win.blit(self.img, (self.x, self.y))

#Rock object
class Rock:
    def __init__(self):
        self.x = random.randrange(1, bg_img.get_width() - 50)
        self.y = random.randrange(1, bg_img.get_height() - 50)
        self.img = random.choice([rock_img_4, rock_img_5, rock_img_6, rock_img_7])
    def draw(self):
        win.blit(self.img, (bg_x + self.x, bg_y + self.y))

class Tree:
    def __init__(self):
        self.x = random.randrange(1, bg_img.get_width() - 50)
        self.y = random.randrange(1, bg_img.get_height() - 50)
        self.img = random.choice([tree_img_1, tree_img_2, tree_img_3, tree_img_4])
    def draw(self):
        win.blit(self.img, (bg_x + self.x, bg_y + self.y))

#Creating player and rock objects
player = Player(width/2, height/2, 10, 10)
for i in range(20):
        rock = Rock()
        tree = Tree()
        rock_list.append(rock)
        tree_list.append(tree)

#Main loop
running = True
while running:

    clock.tick(fps)

    #Quitting the game if cross button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Filling window with black color
    win.fill((200, 200, 200))
    
    #Detecting movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.x - player.h > bg_x:
        bg_x += player_vel
    if keys[pygame.K_d] and player.x + player.h < bg_x + bg_img.get_width():
        bg_x -= player_vel
    if keys[pygame.K_w] and player.y - player.h > bg_y:
        bg_y += player_vel
    if keys[pygame.K_s] and player.y + player.h < bg_y + bg_img.get_height():
        bg_y -= player_vel

    #Drawing background
    win.blit(bg_img, (bg_x, bg_y))
    #Drawing player and rocks
    player.draw()
    for rock in rock_list:
        rock.draw()
    for tree in tree_list:
        tree.draw()
    
    pygame.display.update()