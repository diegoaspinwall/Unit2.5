#Diego Aspinwall
#9-26-17
#olympics.py - you know what it is

from ggame import *

green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
red = Color(0xFF0000,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)
fill = Color(0x000000,0)

blackOutline = LineStyle(5,black)
greenOutline = LineStyle(5,green)
redOutline = LineStyle(5,red)
blueOutline = LineStyle(5,blue)
yellowOutline = LineStyle(5,yellow)

blueCircle = CircleAsset(50,blueOutline,fill)
redCircle = CircleAsset(50,redOutline,fill)
greenCircle = CircleAsset(50,greenOutline,fill)
yellowCircle = CircleAsset(50,yellowOutline,fill)
blackCircle = CircleAsset(50,blackOutline,fill)

Sprite(blueCircle, (50,50))
Sprite(redCircle, (270,50))
Sprite(greenCircle, (215,100))
Sprite(yellowCircle, (105,100))
Sprite(blackCircle, (160,50))
App().run()
