from Camera import BinoCamera
from Drawer import Drawer
from FaceDetector import FaceDetector
from DistancePredictor import DistancePredictor
from Controller import Controller
import cv2
import numpy as np


def main():
    bino_cam = BinoCamera(0, True)
    bino_cam.set_width_height((2560, 720))
    face_detector = FaceDetector()
    # The width of frame is the half of camera width.
    distance_predictor = DistancePredictor(90, bino_cam.get_width_height()[0] / 2, bino_cam.get_width_height()[1], 60)
    distance = 0
    distance_threshold = 2000.0    #mm
    monitor_flag = True

    while True:
        if not bino_cam.capture():
            break

        Drawer.draw_lines(bino_cam.get_lframe())
        Drawer.draw_lines(bino_cam.get_rframe())
        left_face = face_detector.detect_face(bino_cam.get_lframe())
        right_face = face_detector.detect_face(bino_cam.get_rframe())

        if left_face:
            Drawer.dotted_rectangle(bino_cam.get_lframe(), (left_face.get_x(), left_face.get_y()),
                                    (left_face.get_x() + left_face.get_width(),
                                     left_face.get_y() + left_face.get_height()), (0, 0, 255), 2)

        if right_face:
            Drawer.dotted_rectangle(bino_cam.get_rframe(), (right_face.get_x(), right_face.get_y()),
                                    (right_face.get_x() + right_face.get_width(),
                                     right_face.get_y() + right_face.get_height()), (0, 0, 255), 2)

        if left_face and right_face:
            distance = distance_predictor.predict_distance((left_face.get_x(), left_face.get_y()), (right_face.get_x(), right_face.get_y()))
        Drawer.text(bino_cam.get_lframe(), "Distance(m): %.2fm" % (distance / 1000), (20, 40), 1.0, (0, 0, 255), 2)
        print(distance / 1000)

        if 0 < distance < distance_threshold and monitor_flag:
            Controller.set_top_window("Unity 2019.1.8f1 - mainScene.unity - Learn unity editor script - PC, Mac & Linux Standalone <DX11>")
            monitor_flag = False

        cv2.imshow("I am a good stuff v1.0 @ FPS: %d" % bino_cam.get_fps(), np.hstack((bino_cam.get_lframe(), bino_cam.get_rframe())))
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
