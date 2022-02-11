import pygame
from debug import debug
from player import Player
from settings import TILESIZE, WORLD_MAP
from tile import Tile

class level:
    def __init__(self):

        #pegar a base do display
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    
        self.criar_map()


    def criar_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for colunm_index, col in enumerate(row):
                x = colunm_index * TILESIZE   
                y = row_index * TILESIZE    
                if col == 'x':
                    #como ficaria o jogo se o snake fizesse >>>>> 
                    #self.player = Player((x,y),[self.visible_sprites])
                    Tile((x,y),[self.visible_sprites])
                if col == 'p':
                    #como ficaria o jogo se o snake fizesse >>>>> 
                    #Tile((x,y),[self.visible_sprites])
                    self.player =  Player((x,y),[self.visible_sprites])
                

    def run (self):

        #Atualizar e desenhar o joguin
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)