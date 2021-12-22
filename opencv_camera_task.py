import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('task.avi', fourcc, 30, (640, 480))

while True :
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame) #일반 동영상

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #gray
    cv2.imshow('gray', gray)

    edge = cv2.Canny(frame, 50, 100) #edge
    cv2.imshow('edge', edge)

    out.write(frame)

    #ENTER 입력까지 무한반복
    if cv2.waitKey(10) == 13:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()