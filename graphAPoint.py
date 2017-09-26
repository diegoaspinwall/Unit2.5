#Diego Aspinwall
#9-26-17
#graphAPoint.py

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

blackLinex = LineAsset(0,400,blackOutline)
blackLiney = LineAsset(400,0,blackOutline)
xt = LineAsset(0,10,blackOutline)
yt = LineAsset(10,0,blackOutline)
xpt = float(input('X = '))
ypt = float(input('Y = '))
redCircle = CircleAsset(2,blackOutline,red)

if xpt<0:
    xreal = 200-(abs(xpt)*40)
else:
    xreal = 200+xpt*40
if ypt<0:
    yreal = 200+ypt*40
else:
    yreal = 200-(abs(ypt)*40)

Sprite(blackLinex, (200,0))
Sprite(blackLiney, (0,200))
Sprite(xt, (40,195))
Sprite(xt, (80,195))
Sprite(xt, (120,195))
Sprite(xt, (160,195))
Sprite(xt, (240,195))
Sprite(xt, (280,195))
Sprite(xt, (320,195))
Sprite(xt, (360,195))
Sprite(yt, (195,40))
Sprite(yt, (195,80))
Sprite(yt, (195,120))
Sprite(yt, (195,160))
Sprite(yt, (195,240))
Sprite(yt, (195,280))
Sprite(yt, (195,320))
Sprite(yt, (195,360))
Sprite(redCircle, (xreal,yreal))
App().run()