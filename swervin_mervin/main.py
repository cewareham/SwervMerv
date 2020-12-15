# Swervin' Mervin'
# v0.1
# (c) Andrew Buntine
# https://github.com/buntine/swervin_mervin

import pygame, sys, math
from pygame.locals import *
from projection import *
from rendering import *

pygame.init()

# Game variables.
fps            = 50
position       = 0
dimensions     = (640, 480)
segment_height = 150
rumble_length  = 3
speed          = 1
draw_distance  = 100
road_width     = 1500
top_speed      = (segment_height / (1.0/fps))
acceleration   = top_speed / 9.0
field_of_view  = 100 # Degrees
camera_height  = 1400
camera_depth   = 1 / math.tan((field_of_view / 2) * math.pi / 180);
player_x       = 0
direction_x    = 0
player_z       = camera_height * camera_depth
colours        = {"white": pygame.Color(255, 255, 255),
                  "light": {"road": pygame.Color(193, 193, 193),
                            "grass": pygame.Color(61, 212, 76),
                            "rumble": pygame.Color(223, 215, 1),
                            "line": pygame.Color(255, 255, 255)},
                  "dark": {"road": pygame.Color(173, 173, 173),
                           "grass": pygame.Color(50, 186, 62),
                           "rumble": pygame.Color(192, 186, 0),
                           "line": pygame.Color(255, 255, 255)}}

segments       = build_segments(segment_height, rumble_length, colours)
track_length   = len(segments) * segment_height

fps_clock = pygame.time.Clock()
window    = pygame.display.set_mode(dimensions)

while True:
    window.fill(colours["white"])

    position += (0.02 * speed)
    speed += (acceleration * 0.02) # TODO: Might need actually time diff instead of 0.02 guess.
    player_x += direction_x

    while position >= track_length:
        position -= track_length

    while position < 0:
        position += track_length

    if speed > top_speed:
        speed = top_speed

    base_segment = find_segment(position, segments, segment_height)

    for s in range(draw_distance):
        index              = (base_segment["index"] + s) % len(segments)
        segment            = segments[index]
        projected_position = position

        # Past end of track and looped back.
        if segment["index"] < base_segment["index"]:
            projected_position -= track_length

        project_line(segment, "top", (player_x * road_width), camera_height, projected_position, camera_depth, dimensions, road_width)
        project_line(segment, "bottom", (player_x * road_width), camera_height, projected_position, camera_depth, dimensions, road_width)

        # Segment is behind us.
        if segment["bottom"]["camera"]["z"] <= camera_depth:
            continue

        render_grass(window, segment, dimensions)
        render_road(window, segment, dimensions, rumble_length)
        render_player(window, segment, dimensions)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                direction_x = -(0.02 * 2 * (speed / top_speed))
            elif event.key == K_RIGHT:
                direction_x = (0.02 * 2 * (speed / top_speed))
        else:
            direction_x = 0

    # Prevent player from going too far off track.
    if player_x < -1.8:
        player_x = -1.8

    if player_x > 1.8:
        player_x = 1.8


    pygame.display.update()
    fps_clock.tick(fps)
