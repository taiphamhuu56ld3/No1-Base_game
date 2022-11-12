"""
Control the view
"""
from typing import Tuple, List
import random

import pygame

from pygame.surface import Surface
from pygame.rect import Rect

GREY = (120, 120, 120)
WHITE = (255, 255, 255)
MAX_SCREEN_X = 1200
MAX_SCREEN_Y = 600
MAN_HIGH = 200/2
MAN_WIDTH = 100/2
pipe_heigth = [MAX_SCREEN_Y - 350, MAX_SCREEN_Y - 50]

# Initialization
pygame.init()
screen = pygame.display.set_mode((MAX_SCREEN_X, MAX_SCREEN_Y))


bg = pygame.image.load(r"assets\maxresdefault.jpg").convert()

floor = pygame.image.load(r"assets\floor.png").convert()

# Background


def background():
    # screen.fill(GREY)
    # screen.fill(WHITE)
    screen.blit(bg, (0, 0))


# Tạo ống
pip_surface = pygame.image.load(r"assets\pipe-green.png").convert_alpha()
pip_surface = pygame.transform.scale2x(pip_surface)
pipe_list: List[Rect] = []

# Man running
man_run1 = pygame.image.load(r"assets\ma_2.1-removebg-preview.png")
man_run2 = pygame.image.load(r"assets\ma_3.1-removebg-preview.png")
man_run3 = pygame.image.load(r"assets\ma_4.1-removebg-preview.png")
man_run_list: Tuple[Surface, Surface, Surface] = (man_run1, man_run2, man_run3)
MAN_INDEX = 0
man_run = man_run_list[MAN_INDEX]

# lấy font chữ
game_font = pygame.font.Font(r"assets\SEASRN__.ttf", 40)


def draw_floor(_floor_x_pos: float):
    screen.blit(floor, (_floor_x_pos, MAX_SCREEN_Y-50))
    screen.blit(floor, (_floor_x_pos + MAX_SCREEN_X, MAX_SCREEN_Y-50))

    return _floor_x_pos


def draw_man(_man_y_pos: float):  # unused
    screen.blit(man_run, (MAN_WIDTH, _man_y_pos))
    screen.blit(man_run, (MAN_WIDTH, _man_y_pos + 550))

    return _man_y_pos

def draw_man_rotated(rotated_man: Surface, man_run_rec:Rect):
    screen.blit(rotated_man, man_run_rec)

def man_animation(man_run_rec: Rect,
                  _man_run_list: Tuple[Surface, Surface, Surface],
                  _man_index: int):
    new_man = _man_run_list[_man_index]
    new_man_run_rec = new_man.get_rect(
        center=(int(MAN_WIDTH*2), man_run_rec.centery))

    return new_man, new_man_run_rec


def create_pipe(_pip_surface: Surface) -> Tuple[Rect, Rect]:
    random_pipe_pos = random.choice(pipe_heigth)
    bottom_pipe = _pip_surface.get_rect(midtop=(MAX_SCREEN_X, random_pipe_pos))
    top_pipe = _pip_surface.get_rect(
        midtop=(MAX_SCREEN_X, random_pipe_pos - 900))

    return bottom_pipe, top_pipe


def move_pipe(pipes: List[Rect]) -> List[Rect]:
    for pipe in pipes:
        pipe.centerx -= 9

    return pipes


def draw_pipe(pipes: List[Rect],
              _pip_surface: Surface) -> None:
    for pipe in pipes:
        if pipe.bottom >= MAX_SCREEN_Y:
            screen.blit(_pip_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(_pip_surface, False,  True)
            screen.blit(flip_pipe, pipe)

def score_display(_score: float, game_state: str, _high_score: float):
    if game_state == "main_game":
        score_surface = game_font.render(str(int(_score)), True, (0, 0, 255))
        score_rect = score_surface.get_rect(center=(1000, 100))
        screen.blit(score_surface, score_rect)

    elif game_state == "game_over":
        score_surface = game_font.render(
            f'Score: {(int(_score))}', True, (0, 0, 255))
        score_rect = score_surface.get_rect(center=(1000, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(
            f'High Score: {(int(_high_score))}', True, (0, 0, 255))
        high_score_rect = high_score_surface.get_rect(center=(1000, 160))
        screen.blit(high_score_surface, high_score_rect)

# Create end screen
game_over_surface = pygame.image.load(r"assets\message.png").convert_alpha()
game_over_rect = game_over_surface.get_rect(center=(310, 300))

def create_end_screen():
    screen.blit(game_over_surface, game_over_rect)
