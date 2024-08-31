import numpy as np

from PIL import Image, ImageDraw
from time import time


class BezierCurve:
    def __init__(self, points: list):
        if len(points) < 2:
            raise ValueError('Must be at least 2 points')
        self.points = points

    def curve(self, t):
        points = []
        for _1 in range(len(self.points) - 1):
            start, end = self.points[_1], self.points[_1 + 1]
            point = (
                start[0] + (end[0] - start[0]) * t,
                start[1] + (end[1] - start[1]) * t,
            )
            points.append(point)

        if len(points) == 1:
            return points[0]

        return BezierCurve(points).curve(t)


class App:
    def __init__(self, points: list):
        self.width = 600
        self.height = 600
        self.image = Image.new("RGB", (self.width, self.height), 'black')
        self.draw = ImageDraw.Draw(self.image)
        self.bezier = BezierCurve(points)

    def draw_points(self):
        for x, y in self.bezier.points:
            self.draw.arc((x - 3, y - 3, x + 3, y + 3), start=0, end=360, fill='lightgreen', width=6)

    def draw_sub_lines(self):
        for _1 in range(len(self.bezier.points) - 1):
            start, end = self.bezier.points[_1], self.bezier.points[_1 + 1]
            self.draw.line([*start, *end], fill='skyblue')

    def draw_line(self, precision: int = 500):
        t_list = np.linspace(0, 1, precision)
        points = []
        for t in t_list:
            x, y = self.bezier.curve(t)
            points.append((x, y))

        for _1 in range(len(points) - 1):
            start, end = points[_1], points[_1 + 1]
            self.draw.line([*start, *end], fill='white')

    def draw_all(self):
        self.draw_points()
        self.draw_line()
        self.draw_sub_lines()

    def save(self):
        self.image.save('output.png')
        self.image.show()


if __name__ == '__main__':
    start_time = time()

    app = App(
        points=[
            (100, 300), (300, 500), (500, 500), (400, 50), (300, 100), (200, 250)
        ]
    )
    app.draw_all()
    app.save()

    print(f'Time: {time() - start_time} seconds')
