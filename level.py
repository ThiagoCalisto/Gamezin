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
        self.visible_sprites = YsortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

    
        self.criar_map()


    def criar_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for colunm_index, col in enumerate(row):
                x = colunm_index * TILESIZE   
                y = row_index * TILESIZE    
                if col == 'x':
                    #como ficaria o jogo se o snake fizesse >>>>> 
                    #self.player = Player((x,y),[self.visible_sprites])
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    #como ficaria o jogo se o snake fizesse >>>>> 
                    #Tile((x,y),[self.visible_sprites])
                    self.player =  Player((x,y),[self.visible_sprites],self.obstacle_sprites)
                

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

    def custom_draw(self,player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)