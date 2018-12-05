import time, picamera
camera=picamera.PiCamera()
        
class Camera:
    def __init__(self):
        camera.resolution = (1920, 1080)

    def takevideo(self):
        global camera
        camera.start_preview()
        time.sleep(3)
        #camera.start_recording('video.h264')
        #time.sleep(9)
        #camera.stop_recording()
        camera.capture("image1.jpg")
        camera.stop_preview()

