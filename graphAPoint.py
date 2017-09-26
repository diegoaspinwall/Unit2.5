#Diego Aspinwall
#9-26-17
#graphAPoint.py

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

blackLine = LineAsset(0,200,blackOutline) 

Sprite(blackLine, (200,0))
App().run()