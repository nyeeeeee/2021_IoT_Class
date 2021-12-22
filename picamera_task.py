import picamera
import time

path = '/home/pi/src5/06_multimedia'

camera = picamera.PiCamera()

try : 
    camera.resolution = (640, 480)
    camera.start_preview()
    while True :
        s = input('photo : 1, video : 2, exit : 9 > ')
        now_str = time.strftime("%Y%m%d_%H%M%S")
        if s=='1' :
            print('사진 촬영')
            time.sleep(3)
            camera.capture('%s/photo_%s.jpg' % (path,now_str)) #사진
        elif s=='2' : 
            print('동영상 촬영')
            camera.start_recording('%s/video_%s.h264' % (path,now_str)) #동영상
            input('press enter to stop')
            camera.stop_recording()
        elif s=='9' : 
            break #종료
        else :
            print('incorrect command')       

finally :
    camera.stop_preview()