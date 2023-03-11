import cv2
import os


def find_features(img1):
    correct_matches_dct = {}
    directory = 'train/objects/'
    for image in os.listdir(directory):
        img2 = cv2.imread(directory+image, 0)
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)
        correct_matches = []
        for m, n in matches:
            if m.distance < 0.95 * n.distance:
                correct_matches.append([m])
                correct_matches_dct[image.split('.')[0]] = len(correct_matches)
    correct_matches_dct = dict(sorted(correct_matches_dct.items(), key=lambda item: item[1], reverse=True))

    if len(correct_matches_dct) != 0:
        return list(correct_matches_dct.keys())[0]
    else:
        return "Unsigned"


def find_contours(image):
    # blurred_image = cv2.GaussianBlur(image, (3, 3), 0)
    edges = cv2.Canny(image, 45, 195)
    # blurred_image = cv2.GaussianBlur(image, (3, 3), 0)
    # edges = cv2.Canny(blurred_image, 127, 255)

    contours, hierarchy = cv2.findContours(image=edges, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)

    return contours


def find_coordinates(contours, image):
    # figure_coordinates = {"circle": [], "square": [], "triangle": [], "Unsigned": []}
    figure_coordinates = {"coin": [], "lighter": [], "headphones": [], "Unsigned": []}
    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        if h > 50 and w > 60:
            img_crop = image[y - 50:y + h + 50, x - 50:x + w + 50]
            figure_name = find_features(img_crop)
            figure_coordinates[figure_name].append((x, y, x + w, y + h))

    return figure_coordinates


def draw_rectangles_around_figures(figure_coordinates, image):
    image_copy = image.copy()
    for key, value in figure_coordinates.items():
        for v in value:
            if key == "coin":
                rec = cv2.rectangle(image_copy, (v[0], v[1]), (v[2], v[3]), (255, 100, 0), 2)
                cv2.putText(rec, key, (v[0], v[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 8, 127), 1)

    # cv2.imwrite('results/second_algorithm/5_1_result2.jpg', image_copy)
    # cv2.imshow('rectas', image)
    cv2.imshow('rectangles', image_copy)
    cv2.waitKey(0)


if __name__ == "__main__":
    image_original = cv2.imread("results/second_algorithm/5_1.jpg")

    scale_percent = 40
    width = int(image_original.shape[1] * scale_percent / 100)
    height = int(image_original.shape[0] * scale_percent / 100)
    dim = (width, height)
    image = cv2.resize(image_original, dim, interpolation=cv2.INTER_AREA)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contours = find_contours(gray_image)
    objects_location = find_coordinates(contours, gray_image)
    draw_rectangles_around_figures(objects_location, image)
