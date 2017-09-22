#Diego Aspinwall
#9-22-17
#germany.py

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)
gold = Color(0xFFD700,1)

blackOutline = LineStyle(1,black)
redOutline = LineStyle(1,red)
goldOutline = LineStyle(1,gold)

redRectangle = RectangleAsset(200,75,redOutline,red)
blackRectangle = RectangleAsset(200,75,blackOutline,black)
goldRectangle = RectangleAsset(200,75,goldOutline,gold)

Sprite(blackRectangle)
Sprite(redRectangle, (0,75))
Sprite(goldRectangle, (0,150))
App().run()