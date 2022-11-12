"""

ssosossmms
"""
import pygame
clock = pygame.time.Clock()

# tạo timer cho man
man_jump = pygame.USEREVENT + 1
pygame.time.set_timer(man_jump, 200)

# tao timer
spawnpip = pygame.USEREVENT
pygame.time.set_timer(spawnpip, 1200)  # ?
