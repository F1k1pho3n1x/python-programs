from os import listdir
from PIL import Image, ImageDraw
from random import choice

# colors = ["#b6359c", "#ef0a6a", "#0000FF", "#ffffff", "#282828"] Combo1
# colors = ["#8f3be6", "#292929", "#ececec"] Combo2

colors = ["#292929", "#292929", "#3F2929"]
img_size = (1080, 1080)
square_size = 40 # width // square_size must be whole

image = Image.new('RGB', img_size)

for j in range(0, img_size[0] // square_size):
    for i in range(0, img_size[1] // square_size):
        x0 = i * square_size
        y0 = j * square_size
        x1 = (i + 1) * square_size
        y1 = (j + 1) * square_size
        square = ((i * square_size, j * square_size), ((i + 1) * square_size, (j + 1) * square_size))
        img_draw = ImageDraw.Draw(image)
        img_draw.rectangle(square, fill=choice(colors))

#image.show()

files = listdir()
item_id = max([int(x.split(".")[0].split("_")[1]) for x in files if x.__contains__("export")]) + 1
image.save(f"export_{item_id}.png", "PNG")
