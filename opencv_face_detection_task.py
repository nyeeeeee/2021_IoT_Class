import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Camera open failed')
    exit()

face_cascade = cv2.CascadeClassifier('./xml/face.xml') 

#fourcc(four character code) : DIVX(avi), MP4(mp4), X264(h264)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') #('D', 'I', 'V', 'X')
out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))

while True :
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

    if cv2.waitKey(10) == 13: #ENTER 입력까지 무한반복
        break
    
    cv2.imshow('frame', frame)

cap.release()
out.release()
cv2.destroyAllWindows()