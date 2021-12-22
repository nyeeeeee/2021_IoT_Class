import cv2

img = cv2.imread('nct.jpg')
img = cv2.resize(img, (800,600))

# 흑백 이미지로 변환하기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('nct', img)
cv2.imshow('nct_GRAY', gray)

while True :
    if cv2.waitKey(0) == 13 : #아스키코드  ENTER-13, ESC-27, A-65, a-97
        break

cv2.imwrite('nct_GRAY.jpg', gray)

cv2.destroyAllWindows()