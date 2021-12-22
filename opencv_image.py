import cv2

# image 파일 읽기
img = cv2.imread('nct.jpg')

#img = cv2.resize(img, (800,600))

edge = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

cv2.imshow('nct', img)
cv2.imshow('edge', edge)
cv2.imshow('edge2', edge2)
cv2.imshow('edge3', edge3)

#입력대기
cv2.waitKey(0)

cv2.destroyAllWindows()
