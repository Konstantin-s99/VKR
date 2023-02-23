from PIL import Image, ImageDraw
import random

def create_intersecting_circles(background_width, background_height, number_of_rows, diameter_rows):
    im = Image.new("L", (background_width, background_height), 255)
    draw = ImageDraw.Draw(im)

    for i in range(number_of_rows):
        x1 = random.randint(0, background_width - 100)
        y1 = random.randint(0, background_height - 100)
        x2 = x1 + diameter_rows
        y2 = y1 + diameter_rows
        draw.ellipse((x1, y1, x2, y2), 255, 0, width=5)
        print(x1, y1, x2, y2)

    im.show()


create_intersecting_circles(1000, 800, 10, 100)