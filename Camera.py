import cv2
import numpy as np
from abc import ABC, abstractmethod


class Camera(ABC):

    def __init__(self, camera_idx, flip):
        self._cap = cv2.VideoCapture(camera_idx)
        self._flip = flip

    def set_width_height(self, width_height: tuple):
        self._cap.set(3, width_height[0])
        self._cap.set(4, width_height[1])

    def get_width_height(self) -> tuple:
        return self._cap.get(3), self._cap.get(4)

    def set_fps(self, fps: int):
        self._cap.set(cv2.CAP_PROP_FPS, fps)

    def get_fps(self) -> int:
        return self._cap.get(cv2.CAP_PROP_FPS)

    @abstractmethod
    def capture(self):
        pass


class BinoCamera(Camera):

    def __init__(self, camera_idx, flip=False):
        super().__init__(camera_idx, flip)
        self._lframe = np.array([])
        self._rframe = np.array([])

    def get_lframe(self):
        return self._lframe

    def get_rframe(self):
        return self._rframe
    
    def capture(self):
        """
        read the cap and split the frame into left-frame & right-frame
        :return:  True if successfully read the cap data, else False
        """
        ret, frame = self._cap.read()
        if not ret:
            return False
        if self._flip:
            frame = cv2.flip(frame, 0)
        self._lframe, self._rframe = np.split(frame, [int(self.get_width_height()[0] / 2)], axis=1)
        return True


class MonoCamera(Camera):

    def __init__(self, camera_idx, flip=False):
        super().__init__(camera_idx, flip)
        self._frame = np.array([])

    def get_frame(self):
        return self._frame

    def capture(self):
        """
        read the cap data
        :return:  True if successfully read the cap data, else False
        """
        ret, self._frame = self._cap.read()
        if self._flip:
            self._frame = cv2.flip(self._frame, 0)
        if not ret:
            return False
        return True


# Test Function
if __name__ == '__main__':

    # MonoCamera Test
    mono_cam = MonoCamera(0)
    print("(Width, Height) -> ", mono_cam.get_width_height())
    while True:
        if not mono_cam.capture():
            break
        cv2.imshow("test mono-cam@fps: %d" % mono_cam.get_fps(), mono_cam.get_frame())
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

    # BinoCmera Test
    bino_cam = BinoCamera(1, flip=True)
    print("(Width, Height) -> ", bino_cam.get_width_height())
    while True:
        if not bino_cam.capture():
            break
        cv2.imshow("test bino-cam-left@fps: %d" % bino_cam.get_fps(), bino_cam.get_lframe())
        cv2.imshow("test bino-cam-right@fps: %d" % bino_cam.get_fps(), bino_cam.get_rframe())
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

