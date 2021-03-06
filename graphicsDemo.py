#Diego Aspinwall
#9-20-17
#graphicsDemo.py - Intro to ggame

from ggame import *

green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
red = Color(0xFF0000,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color

redRectangle = RectangleAsset(200,100,blackOutline,red) #width, height, outline, fill
blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill
greenEllipse = EllipseAsset(100,50,blackOutline,green) #horiz_radius, vertical_radius, outline, fill
blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, lineStyle
redTriangle = PolygonAsset([(0,0),(120,180),(60,300)],blackOutline,red) #list of endpoints, outline, fill
text = TextAsset('Diego',fill=green,style='bold 40pt Times') #text, fill, style

Sprite(redRectangle)
Sprite(blueCircle,(50,50))
Sprite(greenEllipse,(200,400))
Sprite(blackLine)
Sprite(redTriangle)
Sprite(text, (300,200))
App().run()
