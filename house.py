#Diego Aspinwall
#9-20-17
#house.py

from ggame import *

lblue = Color(0x0080FF,1)
red = Color(0xFF0000,1)
clear = Color(0xFF0000,0)
brown = Color(0x663300,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

redRectangle = RectangleAsset(400,200,blackOutline,red)
brownTriangle = PolygonAsset([(200,0),(0,200),(400,200)],blackOutline,brown)
lblueRectangle = RectangleAsset(50,75,blackOutline,lblue)
clearRectangle = RectangleAsset(50,50,blackOutline,clear)


Sprite(redRectangle, (0,200))
Sprite(brownTriangle)
Sprite(lblueRectangle, (50,325))
Sprite(clearRectangle, (125,225))

App().run()