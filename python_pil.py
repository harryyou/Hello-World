from PIL import Image,ImageFont,ImageDraw
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

sourcePath = r"F:\\tmp\\"
outputPath = r"F:\\tmp\\pictures\\"
fontPath = r"C:\\Windows\\Fonts\\"

sourceFile = "qq.jpg"
outFile = "qqmessage.jpg"

#Open the picture and build canvas!
image = Image.open(sourcePath + sourceFile,'r')
draw = ImageDraw.Draw(image)

#The size of the picture decided Font size!
fontsize = min(image.size)/4

#Font instance!
fontobj = ImageFont.truetype(font = fontPath + "Arial.ttf",size = fontsize,index = 0,encoding = '',filename = None)

#Use draw method to add text!
draw.text((image.size[0]-fontsize,0), text = "5", fill = (255,0,0), font = fontobj, anchor = None)

#save picture!
image.save(outputPath + outFile)
