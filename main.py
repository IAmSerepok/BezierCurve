import numpy as np
from PIL import Image, ImageDraw
from time import time
from bezier_curve import BezierCurve
from typing import List, Tuple

class App:
    """Класс для визуализации кривой Безье и её контрольных точек.
    
    Attributes:
        width (int): Ширина выходного изображения (600px).
        height (int): Высота выходного изображения (600px).
        image (Image): Объект изображения PIL.
        draw (ImageDraw): Объект для рисования на изображении.
        bezier (BezierCurve): Объект кривой Безье.
    """

    def __init__(self, points: List[Tuple[float, float]], size: Tuple[int, int] = (600, 600)) -> None:
        """Инициализирует приложение для работы с кривой Безье.
        
        Args:
            points (List[Tuple[float, float]]): Список контрольных точек в формате [(x1, y1), (x2, y2), ...].
            size (Typle): Размер изображения в пикселях.

        """
        self.width, self.height = size
        self.image = Image.new("RGB", (self.width, self.height), 'black')
        self.draw = ImageDraw.Draw(self.image)
        self.bezier = BezierCurve(points)

    def draw_points(self) -> None:
        """Рисует контрольные точки кривой Безье."""
        for x, y in self.bezier.points:
            self.draw.arc((x - 3, y - 3, x + 3, y + 3), start=0, end=360, fill='lightgreen', width=6)

    def draw_sub_lines(self) -> None:
        """Рисует вспомогательные линии между контрольными точками."""
        for i in range(len(self.bezier.points) - 1):
            start, end = self.bezier.points[i], self.bezier.points[i + 1]
            self.draw.line([*start, *end], fill='skyblue')

    def draw_line(self, precision: int = 500) -> None:
        """Рисует кривую Безье.
        
        Args:
            precision (int): Количество отрезков для аппроксимации кривой.
                      Чем больше значение, тем более гладкой будет кривая.
        """
        t_list = np.linspace(0, 1, precision)
        points = []
        for t in t_list:
            x, y = self.bezier.curve(t)
            points.append((x, y))

        for i in range(len(points) - 1):
            start, end = points[i], points[i + 1]
            self.draw.line([*start, *end], fill='white')

    def draw_all(self) -> None:
        """Выполняет полную отрисовку"""
        self.draw_points()
        self.draw_line()
        self.draw_sub_lines()

    def save(self) -> None:
        """Сохраняет изображение в файл 'output.png' и открывает его для просмотра."""
        self.image.save('output.png')
        self.image.show()


if __name__ == '__main__':  # Пример использования
    start_time = time()

    app = App(
        points=[
            (100, 300), (300, 500), (500, 500), 
            (400, 50), (300, 100), (200, 250)
        ]
    )
    
    app.draw_all()
    app.save()

    print(f'Время выполнения: {time() - start_time:.2f} секунд')
