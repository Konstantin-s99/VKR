import cv2

image = cv2.imread("E:/Python_projects/VKR/test.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(image=binary_image, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

sel_contours = []
boundRect = []

for i in range(len(contours)):
    if i % 2 == 1:
        sel_contours.append(contours[i])
        boundRect.append(cv2.boundingRect(contours[i]))

image_copy = image.copy()

cv2.drawContours(image=image_copy, contours=sel_contours, contourIdx=-1, color=(255, 0, 0), thickness=2,
                 lineType=cv2.LINE_AA)

# Один квадрат
# c_0 = contours[1]
# x, y, w, h = cv2.boundingRect(c_0)
# image_copy2 = image.copy()
# cv2.rectangle(image_copy2, (x, y), (x+w, y+h), color = (255, 0, 0), thickness = 2)
# cv2.imshow('b', image_copy2)

# Несколько квадратов
image_copy2 = image.copy()
for i in range(len(boundRect)):
    cv2.rectangle(image_copy2, (int(boundRect[i][0]), int(boundRect[i][1])),
                  (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])),
                  color=(255, 0, 0), thickness=2)

cv2.imshow('binary image', binary_image)
cv2.imshow('contours', image_copy)
cv2.imshow('rectangles', image_copy2)
# cv2.imwrite('test_result.jpg', image_copy2)
cv2.waitKey(0)