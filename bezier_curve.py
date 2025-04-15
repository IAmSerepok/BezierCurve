from typing import Sequence, Tuple


class BezierCurve:
    """Класс для работы с квадратичными кривыми Безье.

    Реализует рекурсивный алгоритм построения кривой Безье по опорным точкам.
    Поддерживает кривые любого порядка (количество точек >= 2).

    Attributes:
        points (Sequence[Tuple[float, float]]): Опорные точки кривой в формате [(x1, y1), (x2, y2), ...].
    """

    def __init__(self, points: Sequence[Tuple[float, float]]) -> None:
        """Инициализирует кривую Безье с заданными опорными точками.

        Args:
            points (Sequence[Tuple[float, float]]): Последовательность координат опорных точек. Минимум 2 точки.

        Raises:
            ValueError: Если передано меньше 2 точек.
        """
        if len(points) < 2:
            raise ValueError('Must be at least 2 points')
        self.points = points

    def curve(self, t: float) -> Tuple[float, float]:
        """Вычисляет точку на кривой Безье для параметра t.

        Args:
            t (float): Параметр кривой в диапазоне [0, 1]. 
               0 соответствует начальной точке, 1 - конечной.

        Returns:
            cords (Typle[float, float]): Координаты (x, y) точки на кривой при заданном t.
        """
        points = []
        for i in range(len(self.points) - 1):
            start, end = self.points[i], self.points[i + 1]
            point = (
                start[0] + (end[0] - start[0]) * t,
                start[1] + (end[1] - start[1]) * t,
            )
            points.append(point)

        if len(points) == 1:
            return points[0]

        return BezierCurve(points).curve(t)
