import cv2

image = cv2.imread("results/test_int_coins1.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
edges = cv2.Canny(blurred_image, 200, 255)

contours, hierarchy = cv2.findContours(image=edges, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)

boundRect = []
for i in range(len(contours)):
    rect = cv2.boundingRect(contours[i])
    width = rect[2]
    high = rect[3]
    if high > 70 and width > 30:
        boundRect.append(rect)

image_copy2 = image.copy()
for i in range(len(boundRect)):
    cv2.rectangle(image_copy2, (int(boundRect[i][0]), int(boundRect[i][1])),
                  (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])),
                  color=(255, 0, 0), thickness=2)

cv2.imshow("coins", image)
cv2.imshow("edges", edges)
cv2.imshow('rectangles', image_copy2)
cv2.imwrite("results/test_int_coins1_result.jpg", image_copy2)
cv2.waitKey(0)
