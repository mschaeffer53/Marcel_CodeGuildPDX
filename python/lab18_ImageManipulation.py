'''
Lab 18 - Image Manipulation
Marcel Schaeffer
10/10/17
'''
#import picture
from PIL import Image
import colorsys
img = Image.open(r'C:\Users\ducks\Pictures\Lenna.png')

width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        Y = (.299*r + .587*g + .114*b) #convert brightness
        Y = round(Y, 0)
        Y = int(Y)
        #print(Y)

        pixels[i, j] = (Y, Y, Y) #sign RBG to greyscale

img.show()


# #version 2
# #import picture
# from PIL import Image
# import colorsys
# img = Image.open(r'C:\Users\ducks\Pictures\Lenna.png')
#
# width, height = img.size
# pixels = img.load()
#
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#
#         h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
#         h = h - .3 #decrease hue
#         #h = h + .2 #increase hue
#         s = s + .2 #increase saturation
#         r, g, b = colorsys.hsv_to_rgb(h, s, v)
#         r = int(r * 255)
#         g = int(g * 255)
#         b = int(b * 255)
#
#         pixels[i, j] = (r, g, b) #sign RBG to greyscale
#
# img.show()


# #version 3 stick figure
# from PIL import Image, ImageDraw
#
# width = 500
# height = 500
#
# img = Image.new('RGB', (width, height))
#
# draw = ImageDraw.Draw(img)
#
#
# # the origin (0, 0) is at the top-left corner
#
# draw.rectangle(((0, 0), (width, height)), fill="white")
#
# # draw a rectangle from x0, y0 to x1, y1
# #draw.rectangle(((50, 50), (200, 200)), fill="lightblue")
#
# # draw a line from x0, y0, x1, y1
# # using the color pink
# color = (256, 128, 128)  # pink
# #draw.line((0, 0, width, height), fill=color)
# #draw.line((0, height, width, 0), fill=color)
# draw.line((250, 200, 250, 350), fill='black') #mid section
# draw.line((250, 275, 150, 175), fill='black') #left arm
# draw.line((250, 275, 350, 175), fill='black') #right arm
# draw.line((250, 350, 150, 450), fill='black') #left leg
# draw.line((250, 350, 350, 450), fill='black') #right leg
#
# circle_x = width/2
# circle_y = height/4
# circle_radius = 75
# draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black') #head
# #stick figure
# img.show()
