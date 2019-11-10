import math


class DistancePredictor:

    def __init__(self, camera_fov, frame_width, frame_height, baseline):
        """
        :param camera_fov: camera's horizontal filed of view in degree.
        :param frame_width: the width of frame
        :param baseline: gap between left camera and right camera (mm)
        """
        self._baseline = baseline
        self._center = (int(frame_width / 2), int(frame_height / 2))
        self._focal = frame_width / (2 * math.tan(math.radians(camera_fov / 2)))

    def predict_distance(self, left_pos: tuple, right_pos: tuple) -> float:
        """
        :param left_pos: (x, y) of left frame.
        :param right_pos: (x, y) of right frame.
        :return: distance in mm
        """
        relative_left_x = left_pos[0] - self._center[0]
        relative_left_y = left_pos[1] - self._center[1]
        relative_right_x = right_pos[0] - self._center[0]
        relative_right_y = right_pos[1] - self._center[1]

        if abs(relative_left_x) > 1e-4 and abs(relative_right_x) > 1e-4:
            if relative_left_x < -1e-4:
                sinA1 = math.sqrt((relative_left_y ** 2 + self._focal ** 2) / (relative_left_x ** 2 + relative_left_y ** 2 + self._focal ** 2))
                sinA2 = math.sqrt((relative_right_y ** 2 + self._focal ** 2) / (relative_right_x ** 2 + relative_right_y ** 2 + self._focal ** 2))
                A1 = math.asin(sinA1)
                A2 = math.asin(sinA2)
                return self._baseline * sinA1 * sinA2 / math.sin(A1 - A2)
            elif relative_right_x > 1e-4:
                sinA1 = math.sqrt((relative_right_y ** 2 + self._focal ** 2) / (relative_right_x ** 2 + relative_right_y ** 2 + self._focal ** 2))
                sinA2 = math.sqrt((relative_left_y ** 2 + self._focal ** 2) / (relative_left_x ** 2 + relative_left_y ** 2 + self._focal ** 2))
                A1 = math.asin(sinA1)
                A2 = math.asin(sinA2)
                return self._baseline * sinA1 * sinA2 / math.sin(A1 - A2)
            else:
                tanA1 = 1 / math.sqrt((relative_left_y ** 2 + self._focal ** 2) / relative_left_x ** 2)
                tanA2 = 1 / math.sqrt((relative_right_y ** 2 + self._focal ** 2) / relative_right_x ** 2)
                return self._baseline / (tanA1 + tanA2)

        return 0


# Test Function
if __name__ == '__main__':
    distance_predictor = DistancePredictor(100, 640, 480, 60)
    print("Distance(mm): ", distance_predictor.predict_distance((320, 300), (200, 300)))
