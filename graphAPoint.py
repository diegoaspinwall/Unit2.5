#Diego Aspinwall
#9-26-17
#graphAPoint.py

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

blackLinex = LineAsset(0,400,blackOutline) 
blackLiney = LineAsset(400,0,blackOutline) 

Sprite(blackLinex, (200,0))
Sprite(blackLiney, (0,200))
App().run()