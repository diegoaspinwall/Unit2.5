#Diego Aspinwall
#9-26-17
#graphAPoint.py

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

blackLinex = LineAsset(0,400,blackOutline)
blackLiney = LineAsset(400,0,blackOutline)
x1 = LineAsset(0,10,blackOutline)
x2 = LineAsset(0,10,blackOutline)
x3 = LineAsset(0,10,blackOutline)
x4 = LineAsset(0,10,blackOutline)
x5 = LineAsset(0,10,blackOutline)
x6 = LineAsset(0,10,blackOutline)
x7 = LineAsset(0,10,blackOutline)
x8 = LineAsset(0,10,blackOutline)

Sprite(blackLinex, (200,0))
Sprite(blackLiney, (0,200))
Sprite(x1, (40,195))
App().run()