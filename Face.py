
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

    def get_x(self):
        return self.get_rect()[0]

    def get_y(self):
        return self.get_rect()[1]

    def get_width(self):
        return self.get_rect()[2]

    def get_height(self):
        return self.get_rect()[3]


# Test Function
if __name__ == '__main__':
    face = Face((10, 10, 34, 78))
    print("The face's size: " + str(face.calculate_size()))
