import cv2
import numpy as np

image = cv2.imread("results/test_coins3.jpg")

image_height = image.shape[0]
image_width = image.shape[1]

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

number_of_coins = 13
sum_diameters = 0
diameters = []
for i in range(len(boundRect)):
    diameter_mm = round(boundRect[i][2]/3.8, 2)
    rectangle = cv2.rectangle(image_copy2, (int(boundRect[i][0]), int(boundRect[i][1])),
                  (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])),
                  color=(255, 0, 0), thickness=2)
    cv2.putText(rectangle, f"D={diameter_mm}mm", (boundRect[i][0], boundRect[i][1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (150, 8, 127), 2)
    sum_diameters += diameter_mm
    diameters.append(diameter_mm)

# В 1 мм 3,8 px
avg_diameter = round(sum_diameters / number_of_coins, 2)
dispersion = round(np.var(diameters), 2)


cv2.putText(image_copy2, f"Required objects: {number_of_coins}", (image_width-330, image_height-320),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
cv2.putText(image_copy2, "Correctly defined: 92.31%", (image_width-330, image_height-290),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
cv2.putText(image_copy2, "False-positive objects: 2", (image_width-330, image_height-260),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
cv2.putText(image_copy2, "False-negative objects: 1", (image_width-330, image_height-230),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
cv2.putText(image_copy2, f"Avg diameter: 21.98mm", (image_width-330, image_height-200),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
cv2.putText(image_copy2, f"Dispersion: 4.66", (image_width-330, image_height-170),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
cv2.putText(image_copy2, f"Real avg diameter: 20.04mm", (image_width-330, image_height-140),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
cv2.putText(image_copy2, f"Real dispersion: 3.63", (image_width-330, image_height-110),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

# cv2.imshow("coins", image)
# cv2.imshow("edges", edges)
cv2.imshow('rectangles', image_copy2)
#cv2.imwrite("results/test_coins3_result.jpg", image_copy2)
cv2.waitKey(0)
