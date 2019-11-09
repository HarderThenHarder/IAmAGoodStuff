import cv2


class Drawer:

    @staticmethod
    def draw_lines(frame):
        width = frame.shape[1]
        height = frame.shape[0]
        cv2.line(frame, (0, height // 2), (width, height // 2), (0, 255, 0), 1)
        cv2.line(frame, (width // 2, 0), (width // 2, height), (0, 255, 0), 1)
        cv2.circle(frame, (width // 2, height // 2), 50, (0, 255, 0), 1)

    @staticmethod
    def text(frame, text, pos, size, color):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, text, pos, font, size, color, 1)

    @staticmethod
    def dotted_rectangle(frame, start, end, color, line_width):
        vertexs = []
        for i in range(start[0], end[0], 5):
            vertexs.append((i, start[1]))
        for i in range(start[1], end[1], 5):
            vertexs.append((end[0], i))
        for i in range(end[0], start[0], -5):
            vertexs.append((i, end[1]))
        for i in range(end[1], start[1], -5):
            vertexs.append((start[0], i))
        for i in range(0, len(vertexs), 2):
            cv2.line(frame, vertexs[i], vertexs[i + 1], color, line_width)
