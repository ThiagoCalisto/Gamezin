from random import random
import pygame
from debug import debug
from player import Player
from settings import TILESIZE, WORLD_MAP
from tile import Tile
from support import *
from random import choice

class level:
    def __init__(self):

        #pegar a base do display
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = YsortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

    
        self.criar_map()


    def criar_map(self):
        layouts = {
            'boundary': import_csv_layout('./graphics/map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('./graphics/map/map_Grass.csv'),
            'object': import_csv_layout('./graphics/map/map_Objects.csv'),
        }
        graphics = {
            'grass': import_folder('./graphics/graphics/grass'),
            'object': import_folder('./graphics/graphics/objects')
        }

        for style,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for colunm_index, col in enumerate(row):
                    if col != '-1':
                        x = colunm_index * TILESIZE   
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),[self.visible_sprites, self.obstacle_sprites],'grass',random_grass_image)
                        if style == 'object':
                            surf = graphics['object'][int(col)]
                            Tile((x,y),[self.visible_sprites, self.obstacle_sprites],'object',surf)               
                #if col == 'x':
                    #como ficaria o jogo se o snake fizesse >>>>> 
                    #self.player = Player((x,y),[self.visible_sprites])
                    #Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                #if col == 'p':
                    #como ficaria o jogo se o snake fizesse >>>>> 
                    #Tile((x,y),[self.visible_sprites])
                    #self.player =  Player((x,y),[self.visible_sprites],self.obstacle_sprites)
        self.player =  Player((2000,1430),[self.visible_sprites],self.obstacle_sprites)
                

    def run (self):

        #Atualizar e desenhar o joguin
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YsortCameraGroup(pygame.sprite.Group):
    def __init__(self):

            #setup geral
            super().__init__()
            self.display_surface = pygame.display.get_surface()
            self.half_width = self.display_surface.get_size()[0] // 2
            self.half_height = self.display_surface.get_size()[1] // 2
            self.offset = pygame.math.Vector2(100,200)

            #criando o chao
            self.floor_surface = pygame.image.load('./graphics/graphics/tilemap/ground.png').convert()
            self.floor_rect = self.floor_surface.get_rect(topleft = (0, 0))

    def custom_draw(self,player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #desenhando o chao
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface,floor_offset_pos)

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)