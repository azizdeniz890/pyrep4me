import cv2
resim = cv2.imread('guss.jpg', cv2.IMREAD_GRAYSCALE)

threshold_value = 120
esikliresim = cv2.threshold(resim, threshold_value, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('with threshold', esikliresim)
cv2.waitKey(0)
cv2.destroyAllWindows()
