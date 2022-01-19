import cv2


class VideoCamera(object):
    def __init__(self):
        # caap using webcam
        self.video = cv2.VideoCapture('http:192.168.0.2:4747/video')


    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # encode it jpg to jpeg
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()