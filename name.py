#Diego Aspinwall
#9-22-17
#name.py

from ggame import *

name = input('Enter name: ')
RGB = input('Enter RGB code: ')

color = Color('0x'+RGB,1)
black = Color(0x000000,1)

colorOutline = LineStyle(1,color) 

text = TextAsset(name,fill=black,style='bold 40pt Times')
backcolor = RectangleAsset(800,400,colorOutline,color)

Sprite(backcolor)
Sprite(text, (350,150))
App().run()