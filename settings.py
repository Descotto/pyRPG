
WIDTH = 800
HEIGHT = 800
FPS = 60
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

UP_BTN_X = 100 
DOWN_BTN_X = 100
LEFT_BTN_X = 45          
RIGHT_BTN_X = 155
ATTACK_BTN_X = 700          
MAGIC_BTN_X = 600
SWITCH_A_BTN_X = 400
SWITCH_M_BTN_X = 300

UP_BTN_Y = 600
DOWN_BTN_Y = 700
LEFT_BTN_Y = 650
RIGHT_BTN_Y = 650
ATTACK_BTN_Y = 600
MAGIC_BTN_Y = 650
SWITCH_A_BTN_Y = 700
SWITCH_M_BTN_Y = 700





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