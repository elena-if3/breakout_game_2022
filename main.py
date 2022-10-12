from numpy import dtype
import pgzrun

# -- CONSTANTS

WIDTH = 800
HEIGHT = 600
ROWS = 7


# -- global variables

# ** bricks **

all_bricks = []
for y in range(0, ROWS*30, 30):
    for x in range(0, WIDTH, 100):
        brick = Actor("brick", anchor=["left", "top"])
        brick.pos = [x, y]
        all_bricks.append(brick)

# ** player **

player = Actor("player")
player.pos = [WIDTH/2, HEIGHT - 50]

# ** ball **

ball = Actor("ball")
ball.pos = [WIDTH/2, HEIGHT - 100]

# ** ball speed **

ball_speed = [360, -360]


# -- functions

# the items that are drawn at the top of my function will appear on screen *under* the items that are drawn 
# at the bottom of my code (in this case, the player will appear over the bricks)
def draw():
    screen.clear()
    for brick in all_bricks:
        brick.draw()
    player.draw()
    ball.draw()


def invert_horizontal_speed():
    ball_speed[0] *= -1

def invert_vertical_speed():
    ball_speed[1] *= -1

def update(dt):   # pass --- just to fill the function (while waiting for further instructions)
    if dt > 0.5:
        return

    # *** ball movement ***
    pos = ball.pos
    mvt_x = ball_speed[0] * dt
    mvt_y = ball_speed[1] * dt
    pos = [pos[0] + mvt_x, pos[1] + mvt_y]

    if pos[0] > WIDTH - 10:
        pos[0] = WIDTH - 10
    elif pos[0] < 10:
        pos[0] = 10
    
    if pos[1] > HEIGHT - 10:
        pos[1] = HEIGHT - 10
    elif pos[1] < 10:
        pos[1] = 10

    ball.pos = pos

    # *** collision with screen ***
    if ball.pos[0] <= 10 or ball.pos[0] >= WIDTH - 10:
        invert_horizontal_speed()
    
    if ball.pos[1] <= 10 or ball.pos[1] >= HEIGHT -10:
        invert_vertical_speed()

    # *** collision with player ***

    if ball.colliderect(player):
        invert_vertical_speed()

    # *** collision with bricks ***

    for brick in all_bricks:
        if ball.colliderect(brick):
            invert_vertical_speed()
            all_bricks.remove(brick)

def on_mouse_move(pos):
    if pos[0] <= 75:
        x = 75
    elif pos[0] >= WIDTH - 75:
        x = WIDTH - 75        
    else:
        x = pos[0]
    y = player.pos[1]
    player.pos = [x, y]

def on_key_down(key):
    if key == keys.SPACE:
        invert_horizontal_speed()


pgzrun.go()
