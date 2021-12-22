import cv2

#카메라 장치 열기
cap = cv2.VideoCapture('output.avi') #동영상 재생

if not cap.isOpened():
    print('Camera open failed')
    exit() #바로 종료

# 카메라 사진 찍기
#ret, frame = cap.read() #정상여부 , 데이터
#cv2.imshow('frame', frame)
#cv2.imwrite('output.jpg', frame)
#cv2.waitKey(0)

#동영상 촬영하기
while True :
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    #1000->1초, 10->0.01초 
    if cv2.waitKey(10) == 13: #ENTER 입력까지 무한반복
        break

cap.release()
cv2.destroyAllWindows()