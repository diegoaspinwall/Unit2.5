#Diego Aspinwall
#9-22-17
#yield.py

from ggame import *

black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)

blackoutline = LineStyle(10,black)

yellowtriangle = PolygonAsset([(80,0), (0,120), (160,120)], blackoutline, yellow)

Sprite(yellowtriangle)
App().run()