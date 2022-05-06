import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size
from tiles import Tile, StaticTile
from enemy import Enemy

class Level:
    def __init__(self,level_data,surface):
        #general setup
        self.display_surface = surface
        self.world_shift = 0

        #player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        #terrain setup
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

        #enemy
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies')

    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index,val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type =='terrain':
                        terrain_tile_list = import_cut_graphics('Project/Real_Code/graphics/terrain/terrain_tiles.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)
                        sprite_group.add(sprite)
                    
                    if type == 'enemies':
                        sprite = Enemy(tile_size,x,y)

        return sprite_group
    
    def player_setup(self,layout):
        for row_index, row in enumerate(layout):
            for col_index,val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    print('player goes here')
                if val == '1':
                    hat_surface = pygame.image.load('Project/Real_Code/graphics/character/hat.png').convert_alpha
                    sprite = StaticTile(tile_size,x,y,hat_surface)
                    self.goal.add(sprite)

    def run(self):
        #run the entire game / level
        self.terrain_sprites.update(self.world_shift)
        self.terrain_sprites.draw(self.display_surface)
        
        #enemy
        self.enemy_sprites.update(self.world_shift)
        self.enemy_sprites.draw(self.display_surface)

        #player sprites
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)