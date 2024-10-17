'''
from PIL import Image

area = (230,155,1110,770)
size = (640,200)

lion_img = Image.open("Lion.jpg")
fruit_img = Image.open("fruit.png")

print(lion_img.size, lion_img.format, lion_img.mode)
print(fruit_img.size, fruit_img.format, fruit_img.mode)

fruit_resz = fruit_img.resize(size)

lion_cropped = lion_img.crop(area)

lion_img.show()
fruit_img.show()

lion_cropped.save("Lion_cropped.jpg")
fruit_resz.save("fruit_resized.png")

from PIL import Image

size = (128, 128)

lion_img = Image.open("Lion.jpg")

lion_rotated = lion_img.rotate(90)

lion_converted = lion_img.convert("L")

lion_transpose = lion_img.transpose(Image.FLIP_LEFT_RIGHT)

lion_img.thumbnail(size)

print("lion_converted.mode =", lion_converted.mode)

print("lion_img.size =", lion_img.size)

lion_converted.show()
lion_transpose.show()
lion_rotated.save("lion_rotated.jpg")
lion_img.save("lion_thumb.jpg")

from PIL import Image
from PIL import ImageDraw

canvas_size = (200,200)
rect_area = [(0,0),(100,100)]
line_cor = [(0,200),(200,0)]
circle_area = [(100,100),(200,200)]

new_img = Image.new("RGB", canvas_size, "orange")

draw_imgs = ImageDraw.Draw(new_img)

draw_imgs.rectangle(rect_area,fill = "red",outline = "yellow")

draw_imgs.line(line_cor, fill = "blue", width = 4)

draw_imgs.ellipse(circle_area, fill = "green", outline = "red")

new_img.show()
draw_imgs.show("imagedraw.jpg")
'''
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

lion_img = Image.open("Lion.jpg")
c3coding_img = Image.open("c3coding_rt.jpg")
c3coding_img.thumbmail(120,120)
draw = ImageDraw.Draw(lion_img)

stx, sty = (150,285)
c3x, c3y = c3coding_img.size
msg1 = "the               is"
msg2 = "the best!"


mfont = ImageFont.truetype("FRACM.TTF", 40)

m2font = ImageFont.truetype("BROADW.TTF", 52)

draw.text((70,280), msg1,(255,255,0), font = mfont,align = "Left")
draw.text((70,330), msg2,(255,0,0), font = mfont,align = "Left")

lion_imgpaste(c3coding.img(stx,sty stx+c3x,sty+c3x))

lion_img.show()
lion_img.save("c3coding.jpg")
