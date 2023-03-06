import cv2

image = cv2.imread("circles/test1.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 100, 200)

contours, hierarchy = cv2.findContours(image=edges, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)

img2 = cv2.imread("train/circle/circle.jpg")
img_train = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

image_copy = image.copy()

for i in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[i])
    img1 = gray_image[y - 20:y + h + 20, x - 20:x + w + 20]

    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img_train, None)
    kp2, des2 = orb.detectAndCompute(img1, None)

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(des1, des2)
    matches = sorted(matches, key=lambda x:x.distance)

    if matches[0].distance < 50:
        cv2.rectangle(image_copy, (x, y),
                      (x + w, y + h),
                      color=(255, 0, 0), thickness=2)
    # s = 0
    # for m in matches[0:3]:
    #     s += m.distance
    # print(s, matches[0].distance)
    print(matches[0].distance)

cv2.imshow('rects', image_copy)
cv2.waitKey(0)