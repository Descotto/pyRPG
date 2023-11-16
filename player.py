import pygame
from settings import *
from support import import_folder
from controls import *




class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, create_attack, destroy_attack):
        super().__init__(groups)
        self.image = pygame.image.load('./assets/chrono/player/down_idle/down_idle.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-26)

        # GRAPHICS SETUP
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # movement
        self.direction = pygame.math.Vector2()
        self.attacking = False
        self.attack_cooldown = 700
        self.attack_time = pygame.time.get_ticks()
        self.obsticle_sprites = obstacle_sprites

        # controls
        self.clicked = False
        
                         
                       

        # weapons
        self.create_attack = create_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.destroy_attack = destroy_attack
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 200

        # Stats
        self.stats = {'health': 100, 'energy':60, 'attack':10, 'magic':4,'speed':5}
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.exp = 1
        self.speed = self.stats['speed']

    def import_player_assets(self):
        character_path = './assets/chrono/player/'
        self.animations = {'up':[],'down':[],'left':[],'right':[],
                           'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
                           'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]} 
        
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
        

    def input(self):
        if not self.attacking:
            keys = pygame.key.get_pressed()
            # movement input
            if keys[pygame.K_w] or self.clicked == 'up':
                self.status = 'up'
                self.direction.y = -1
                self.clicked == False
            elif keys[pygame.K_s] or self.clicked == 'down':
                self.status = 'down'
                self.direction.y = 1
                self.clicked == False
            else:
                self.direction.y = 0
            if keys[pygame.K_a] or self.clicked == 'left':
                self.status = 'left'
                self.direction.x = -1
                self.clicked == False
            elif keys[pygame.K_d] or self.clicked == 'right':
                self.status = 'right'
                self.direction.x = 1
                self.clicked == False
            else:
                self.direction.x = 0

            # attack input
            if keys[pygame.K_SPACE] or self.clicked == 'attack':
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
                self.clicked == False

            if keys[pygame.K_RSHIFT] or self.clicked == 'magic':
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.clicked == False
                print('Magic')

            if keys[pygame.K_LEFT] or self.clicked == 'switch':
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()
                if self.weapon_index < len(list(weapon_data.keys())) -1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0
                self.weapon = list(weapon_data.keys())[self.weapon_index]
                self.clicked == False

 
    def get_status(self):

        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def check_clicked(self):
        self.control = ''    

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obsticle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obsticle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()

        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)



    def update(self):
        self.input()
        
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
