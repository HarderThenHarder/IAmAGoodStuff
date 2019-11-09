
class Face:
    def __init__(self, rect: tuple):
        """
        :param rect: rect is a tuple with four params -> (x, y, w, h)
        """
        self.__rect = rect

    def calculate_size(self) -> float:
        return self.__rect[2] * self.__rect[3]

    def get_rect(self):
        return self.__rect
