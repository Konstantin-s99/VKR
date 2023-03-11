import cv2


def thresh_callback(val):
    # max_thresh = val
    min_thresh = cv2.getTrackbarPos('Canny min thresh:', source_window)
    max_thresh = cv2.getTrackbarPos('Canny max thresh:', source_window)
    edges = cv2.Canny(gray_image, min_thresh, max_thresh)

    cv2.imshow("Contours", edges)

# image = cv2.imread("E:/Python_projects/VKR/test_noise.jpg")
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # blurred = cv2.GaussianBlur(gray_image, (3, 3), 0)
# # blurred = cv2.blur(image, (3, 3))
# blurred = cv2.medianBlur(image, 5)
# edges = cv2.Canny(blurred, 25, 255)
# contours, hierarchy = cv2.findContours(image=edges, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
#
# boundRect = []
# for i in range(len(contours)):
#     boundRect.append(cv2.boundingRect(contours[i]))
#
# image_copy = image.copy()
# for i in range(len(boundRect)):
#     cv2.rectangle(image_copy, (int(boundRect[i][0]), int(boundRect[i][1])),
#                   (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])),
#                   color=(255, 0, 0), thickness=2)
#
# cv2.imshow('image', image)
# cv2.imshow('blurred', blurred)
# cv2.imshow('edges', edges)
# cv2.imshow('rectangles', image_copy)
# cv2.waitKey(0)
##################################################
image_original = cv2.imread("results/second_algorithm/5_1.jpg")

scale_percent = 40
width = int(image_original.shape[1] * scale_percent / 100)
height = int(image_original.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(image_original, dim, interpolation=cv2.INTER_AREA)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
# blurred_image = cv2.blurred = cv2.medianBlur(gray_image, 5)

cv2.imshow("coins", gray_image)

source_window = 'Source'
cv2.namedWindow(source_window)
max_thresh = 255
initial_max_threshold = 195
initial_min_threshold = 45

cv2.createTrackbar('Canny max thresh:', source_window, initial_max_threshold, max_thresh, thresh_callback)
cv2.createTrackbar('Canny min thresh:', source_window, initial_min_threshold, max_thresh, thresh_callback)

thresh_callback(initial_max_threshold)

cv2.waitKey(0)