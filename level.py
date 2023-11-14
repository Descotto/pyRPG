import pygame
from settings import *
from tile import Tile
from player import Player
from support import *
from random import choice
from weapon import Weapon
from ui import UI



class Level:
    def __init__(self):
        # get display surface
        
        
        # sprite groups
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # attack_sprites
        self.current_attack = None
        
        # sprite_setup
        self.create_map()

        # user interface
        self.ui = UI()


    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('./assets/chrono/map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('./assets/chrono/map/map_Grass.csv'),
            'object': import_csv_layout('./assets/chrono/map/map_LargeObjects.csv')
        }
        graphics = {
            'grass': import_folder('./assets/chrono/grass'),
            'objects': import_folder('./assets/chrono/objects')
        }

        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                # print(row_index)
                # print(row)
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
                        if style == 'grass':
                            # create grass tile
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'grass',random_grass_image)

                        if style == 'object':
                            # create object tile
                            surf = graphics['objects'][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)

        self.player = Player((1700,450), [self.visible_sprites], self.obstacle_sprites, self.create_attack, self.destroy_attack)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def run(self):
        # update and draw game objects
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface  = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        #creating floor
        self.floor_surf = pygame.image.load('./assets/1 - level/graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
        # Create and add buttons to YSortCameraGroup
    

    def custom_draw(self,player):

        #getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #drawing the floor
        floor_upset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_upset_pos)

        # controls
        btn_x = floor_upset_pos  # X-coordinate of the btn's top-left corner
        btn_y = 100  # Y-coordinate of the btn's top-left corner
        btn_size = 32  # Size of the btn (width and height)
        btn_color = (255, 0, 0)
        
        

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)