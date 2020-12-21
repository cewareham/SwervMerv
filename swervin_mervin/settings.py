# Game constants.

from pygame import Color
import math

FPS               = 60
FRAME_RATE        = (1.0 / FPS)
DIMENSIONS        = (640, 480)
SEGMENT_HEIGHT    = 260
RUMBLE_LENGTH     = 3
DRAW_DISTANCE     = 200
ROAD_WIDTH        = 2100
LANES             = 4
BOUNDS            = 1.8
CENTRIFUGAL_FORCE = 0.266
TOP_SPEED         = (SEGMENT_HEIGHT / (1.0/FPS)) * 1.6
OFFROAD_TOP_SPEED = TOP_SPEED / 2.0
ACCELERATION      = TOP_SPEED / 5.0
DECELERATION      = 2.3
FIELD_OF_VIEW     = 100 # Degrees
CAMERA_HEIGHT     = 1400
CAMERA_DEPTH      = 1 / math.tan((FIELD_OF_VIEW / 2) * math.pi / 180);
BOTTOM_OFFSET     = 5
PLAYER_Z          = (CAMERA_HEIGHT * CAMERA_DEPTH)
COLOURS           = {"white": Color(255, 255, 255),
                     "sky":   Color(142, 169, 232),
                     "light": {"road":   Color(193, 193, 193),
                               "grass":  Color(61, 212, 76),
                               "rumble": Color(255, 51, 51),
                               "line":   Color(255, 255, 255)},
                     "dark":  {"road":   Color(188, 188, 188),
                               "grass":  Color(55, 199, 66),
                               "rumble": Color(255, 255, 255),
                               "line":   Color(255, 255, 255)}}
SPRITES           = {"straight": {
                       "path": "straight.png",
                       "width": 80,
                       "height": 41},
                     "left": {
                       "path": "left.png",
                       "width": 80,
                       "height": 45},
                     "right": {
                       "path": "right.png",
                       "width": 80,
                       "height": 45},
                     "uphill_straight": {
                       "path": "uphill_straight.png",
                       "width": 80,
                       "height": 45},
                     "uphill_left": {
                       "path": "uphill_left.png",
                       "width": 80,
                       "height": 45},
                     "uphill_right": {
                       "path": "uphill_right.png",
                       "width": 80,
                       "height": 45},
                     "downhill_straight": {
                       "path": "downhill_straight.png",
                       "width": 80,
                       "height": 41},
                     "downhill_left": {
                       "path": "downhill_left.png",
                       "width": 80,
                       "height": 45},
                     "downhill_right": {
                       "path": "downhill_right.png",
                       "width": 80,
                       "height": 45},
                     "column": {
                       "path": "column.png",
                       "width": 80,
                       "height": 126}}
