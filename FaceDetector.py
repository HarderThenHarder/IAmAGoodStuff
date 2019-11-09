import cv2
from Face import Face


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
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.__face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)

        if len(faces) > 0:
            for face in faces:
                self.__face_list.append(Face(face))
            sorted(self.__face_list, key=lambda x: x.calculate_size(), reverse=True)
            return self.__face_list[0]

        return None


# Test function
if __name__ == '__main__':
    img = cv2.imread("assets/timg.jpg")
    face_detector = FaceDetector()
    face = face_detector.detect_face(img)
    rect = face.get_rect()
    cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 1)
    cv2.imshow("test face-detect", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()