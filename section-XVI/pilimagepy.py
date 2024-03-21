from PIL import Image

hulk = Image.open('D://Computer Science//Courses//Udemy//jose portila-python//python programs//section-XVI//hulk.jpg')
# special file type: PIL.JpegImagePlugin.JpegImageFile
print(f"{hulk.size} {hulk.format_description} ")

# croping images with python
x = 90
y = 0
w = 338/1.4
h = 190

# hulk.crop((x,y,w,h)).show()
# hulk.rotate(90)
# hulk.resize(700,200)

# rgba values goes from 0(transparent) - 255(opaque)
hulk.putalpha(145)
hulk.show()


