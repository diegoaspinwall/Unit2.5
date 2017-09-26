#Diego Aspinwall
#9-26-17
#warmup5.py

from ggame import *

blue = Color(0x0000FF,1)
yellow = Color(0x00FFFF,1)

yellowoutline = LineStyle(1,yellow)

yellowdiamond = PolygonAsset([(100,0),(0,100),(100,200),(200,100)],yellowoutline,yellow)
text = TextAsset('Diego',fill=blue,style='bold 40pt Times')

Sprite(yellowdiamond)
Sprite(text, (50,50))
App().run()

