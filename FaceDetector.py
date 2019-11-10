import cv2
from Face import Face
from Camera import MonoCamera, BinoCamera
from Drawer import Drawer


class FaceDetector:

    def __init__(self):
        self.__face_cascade = cv2.CascadeClassifier("assets/haarcascade_frontalface_default.xml")
        self.__face_list = []

    def detect_face(self, frame):
        """
        return the Face Object with the max size
        :param frame: camera frame, np.array
        :return: Face Object
        """
        self.__face_list.clear()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.__face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        if len(faces) > 0:
            for face in faces:
                self.__face_list.append(Face(face))
            sorted(self.__face_list, key=lambda x: x.calculate_size(), reverse=True)
            return self.__face_list[0]
        return None


# Test function
if __name__ == '__main__':
    # Test Camera
    camera = MonoCamera(0)
    camera.set_width_height((1280, 720))
    face_detector = FaceDetector()

    while True:
        if not camera.capture():
            break
        frame = camera.get_frame()
        Drawer.draw_lines(frame)
        face = face_detector.detect_face(frame)
        if face:
            x, y, w, h = face.get_rect()
            Drawer.dotted_rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("test Face Recognize", frame)

        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

    # # Test Img
    # img = cv2.imread("assets/timg2.jpg")
    # face_detector = FaceDetector()
    # face = face_detector.detect_face(img)
    # if face:
    #     x, y, w, h = face.get_rect()
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
    # cv2.imshow("test Face Recognize", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

