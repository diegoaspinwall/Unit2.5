#Diego Aspinwall
#9-22-17
#yield.py

from ggame import *

black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)

blackoutline = LineStyle(7,black)

yellowtriangle = PolygonAsset([(20,0), (0,30), (40,30)], blackoutline, yellow)

Sprite(yellowtriangle)
App().run()