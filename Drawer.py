import cv2


class Drawer:

    @staticmethod
    def draw_lines(frame):
        width = frame.shape[1]
        height = frame.shape[0]
        cv2.line(frame, (0, height // 2), (width, height // 2), (0, 255, 0), 1)
        cv2.line(frame, (width // 2, 0), (width // 2, height), (0, 255, 0), 1)
        cv2.circle(frame, (width // 2, height // 2), 50, (0, 255, 0), 1)
