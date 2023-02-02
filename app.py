import pygame, time, beat_tracker
import numpy as np
from random import randint
from copy import deepcopy
import sys

RES = WIDTH, HEIGHT = 800, 600
TILE = 8
W, H = WIDTH // TILE, HEIGHT // TILE
FPS_default = 10
started = False
paused = False
TEMPO = beat_tracker.tempo
# divide patterns into big (amplitude peak) and small (normal beats) patterns?
# how to make glider-thick circles? it's nice if there could be a formula.
# time and activation time, amplitude, fps as tempo
# dialog for file selection
    
pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

def check_cell(current_field, x, y):
    count = 0
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            if current_field[j][i]:
                count += 1
    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0
        
def toggle_pause():
    paused = not paused

next_field = [[0 for i in range(W)] for j in range(H)]
# how do I update it according to the song beat?
#current_fieldFuncs = {
#    0: (current_field, [randint(0,1)]),
#    1: (current_field, [(i-5) % 33]),
#    2: (current_field, [(i*j) % randint(10,25)]),
#    3: (current_field, [(i*j**2) % randint(10,25)]),
#    4: (current_field, [1-j % 2, j > 30]),
#    5: (current_field, [np.sqrt(i*i + 32) % 2, 3*i % 15]),
#    6: (current_field, [H/2-20 <= i <= W/2+20, H/2-20 <= j <= H/2+20]),
#    7: (current_field, [i == j + W // 8, i + j == W * 7 // 8]),
#    8: (current_field, [i == W // 2, j == H // 2]),
#    9: (current_field, [i < W // 2, j % 3])
#    }
init_templ = randint(1,7)

if init_templ == 1:
    current_field = [[1 if i < W // 2 and j % 6 else 0 for i in range(W)] for j in range(H)]
if init_templ == 2:
    current_field = [[1 if not (i-5) % 33 else 0 for i in range(W)] for j in range(H)]
if init_templ == 3:
    current_field = [[1 if not (i*j) % randint(10,25) else 0 for i in range(W)] for j in range(H)]
if init_templ == 4:
    current_field = [[1 if not (i*j**2) % randint(10,25) else 0 for i in range(W)] for j in range(H)]
if init_templ == 5:
    current_field = [[1 if 1-j % 2 or j > 30 else 0 for i in range(W)] for j in range(H)]
if init_templ == 6:
    current_field = [[1 if not np.sqrt(i*i + 32) % 2 or not 3*i % 15 else 0 for i in range(W)] for j in range(H)]
if init_templ == 7:
    current_field = [[1 if W/2-20 <= i <= W/2+20 and H/2-20 <= j <= H/2+20 else 0 for i in range(W)] for j in range(H)]

while True: 

    surface.fill(pygame.Color('aliceblue'))
    # draw grid on surface
    [pygame.draw.line(surface, pygame.Color('black'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('black'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                started = True
            elif event.key == pygame.K_p:
                toggle_pause()
            else:
                pass
    
    if paused:
        continue
    
    if started and not paused: 
            for x in range (1, W-1):
                for y in range(1, H-1):
                    if current_field[y][x]:
                        pygame.draw.rect(surface, pygame.Color('blueviolet'), (x * TILE, y * TILE, TILE -1 , TILE -1))
                    next_field[y][x] = check_cell(current_field, x, y)
            current_field = deepcopy(next_field)
        
    pygame.display.flip()

    if 50 <= TEMPO <= 240:
        if TEMPO <= 80:
            speed = TEMPO/8
        elif 80 < TEMPO:
            speed = TEMPO/12
        clock.tick(speed)
    else:
        clock.tick(FPS_default)
    clock_display = round(clock.get_fps(), 2)
    pygame.display.set_caption(f"Conway's game of life. FPS: {clock_display}")
        
    time.sleep(0.001)   



    

