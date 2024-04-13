#resmi al ve kırp roi select ile 
import cv2

resim = cv2.imread("amogus.jpg")

roi = cv2.selectROI(resim)

kırp= resim[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]

cv2.imshow("Kırpılan Bölge", kırp)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("kirpilmishal.jpg", kırp)

