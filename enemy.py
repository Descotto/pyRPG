import pygame
from settings import *
from entity import Entity
from support import *

class Enemy(Entity):
    def __init__(self, monster_name,pos,groups, obstacle_sprites):
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # graphics setup
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        # movement
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        # stats
        self.monster_name = monster_name
        self.monster_info = monster_data[self.monster_name]
        self.health = self.monster_info['health']
        self.exp = self.monster_info['exp']
        self.speed = self.monster_info['speed']
        self.attack_damage = self.monster_info['damage']
        self.resistance = self.monster_info['resistance']
        self.attack_radius = self.monster_info['attack_radius']
        self.attack_type = self.monster_info['attack_type']

    def import_graphics(self,name):
        self.animations = {'idle': [], 'move': [], 'attack': []}
        main_path = f'./assets/chrono/monsters/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_player_distance_direction(self,player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()
        return (distance, direction)

    def get_status(self,player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius:
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def update(self):
        
        self.move(self.speed)

    def enemy_update(self,player):
        pass