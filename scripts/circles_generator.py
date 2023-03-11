from PIL import Image, ImageDraw
import random
import numpy as np
import cv2

def add_salt_paper(image, prob):
    noise_img = np.zeros(image.shape, np.uint8)
    threshold = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rndm = random.random()
            if rndm < prob:
                noise_img[i][j] = 0
            elif rndm > threshold:
                noise_img[i][j] = 255
            else:
                noise_img[i][j] = image[i][j]
    return noise_img


def create_intersection_circles(background_width, background_height, number_of_rows, diameter_rows, width):
    im = Image.new("L", (background_width, background_height), 255)
    draw = ImageDraw.Draw(im)

    for i in range(number_of_rows):
        x1 = random.randint(0, background_width - 100)
        y1 = random.randint(0, background_height - 100)
        x2 = x1 + diameter_rows
        y2 = y1 + diameter_rows
        draw.ellipse((x1, y1, x2, y2), 255, 0, width=width)
        print(x1, y1, x2, y2)

    return im



if __name__ == "__main__":
    im_circles = create_intersection_circles(800, 600, 10, 60, 5)
    im_circles.save("results/second_algorithm/2.jpg")
    im_circles.show()

    # image = cv2.imread("E:/Python_projects/VKR/results/second_algorithm/test_with_triangles.jpg")
    # noise_img = np.array(add_salt_paper(image, 0.05))
    # cv2.imshow("noise_circles", noise_img)
    # cv2.imwrite('results/second_algorithm/1.jpg', noise_img)
    # cv2.waitKey(0)