import pygame
from pygame.locals import *
import sys
from vec import Vec2
import math

pygame.display.init()

screen = pygame.display.set_mode((800,600), 0, 32)
background = pygame.image.load('background.png').convert()
arrow = pygame.image.load('red32x16arrow.png').convert_alpha()

clock = pygame.time.Clock()

position = Vec2(400, 300)
speed = 300.0
rotation = 0.0
rotation_speed = 360.0

mousedown = False
autofollow = False




while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_q or event.key == K_ESCAPE:
				sys.exit()
			if event.key == K_f:
				autofollow = not autofollow
		if event.type == MOUSEBUTTONDOWN:
			mousedown = True
		if event.type == MOUSEBUTTONUP:
			mousedown = False

	keys_pressed = pygame.key.get_pressed()

	rotation_dir = 0.0
	movement_dir = 0.0

	if keys_pressed[K_a]:
		rotation_dir = 1
	elif keys_pressed[K_d]:
		rotation_dir = -1
	if keys_pressed[K_w]:
		movement_dir = 1
	elif keys_pressed[K_s]:
		movement_dir = -1
	

	if mousedown or autofollow:
		temp = Vec2.from_pts(position, pygame.mouse.get_pos())
		if temp.get_magnitude() > 20.0: #makes us go "past" the mouse
			rotation = math.atan2(temp.x, temp.y) * (180.0 / math.pi)		
		movement_dir = 1 #move towards the mouse

	screen.blit(background, (0,0))
	arrow_rotated = pygame.transform.rotate(arrow, rotation)
	w,h = arrow_rotated.get_size()
	arrow_draw_position = Vec2(position.x - w / 2, position.y - h / 2)
	screen.blit(arrow_rotated, (arrow_draw_position.x,arrow_draw_position.y))

	this_time = clock.tick(60)
	this_seconds = this_time / 1000.0

	rotation += rotation_dir * rotation_speed * this_seconds

	#magic
	heading_x = math.sin(rotation * math.pi / 180.0)
	heading_y = math.cos(rotation * math.pi / 180.0)
	heading = Vec2(heading_x, heading_y)
	heading *= movement_dir

	position += heading * speed * this_seconds

	pygame.display.update()
