
WIDTH = 1133
HEIGHT = 744
FPS = 30
TILESIZE = 64

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = './assets/chrono/font/joystix.ttf'
UI_FONT_SIZE = 18

# controllers
BTN_HEIGHT = 32
BTN_WIDTH = 32

UP_BTN_X = WIDTH * 0.09
DOWN_BTN_X = 100
LEFT_BTN_X = 45
RIGHT_BTN_X = 155
ATTACK_BTN_X = 1033
MAGIC_BTN_X = 933
SWITCH_BTN_X = 933
SWITCH_M_BTN_X = 603

UP_BTN_Y = 450
DOWN_BTN_Y = 550
LEFT_BTN_Y = 500
RIGHT_BTN_Y = 500
ATTACK_BTN_Y = 450
MAGIC_BTN_Y = 500
SWITCH_BTN_Y = 600
SWITCH_M_BTN_Y = 550





# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'


# weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic':'./assets/chrono/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic':'./assets/chrono/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic':'./assets/chrono/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic':'./assets/chrono/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic':'./assets/chrono/weapons/sai/full.png'}
}


# magic
magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic':'./assets/chrono/particles/flame/fire.png'},
    'heal': {'strength': 5, 'cost': 20, 'graphic':'./assets/chrono/particles/heal/heal.png'}
}

# enemies
monster_data = {
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound': './assets/chrono/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw', 'attack_sound': './assets/chrono/audio/attack/claw.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder', 'attack_sound': './assets/chrono/audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70, 'exp': 120, 'damage': 6, 'attack_type': 'leaf_attack', 'attack_sound': './assets/chrono/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
}