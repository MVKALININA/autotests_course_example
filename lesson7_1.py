# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы класса:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (-4, -5)).y_axis_intersection() --> False

# Здесь пишем код

class Segment:
    """
    Класс сегмент, который включает в себя экземпляры класса: координаты точек
    """
    def __init__(self, line1, line2):
        """
        Метод инициализирует передаваемые характеристики - 2 кортежа с координатами точек
        :param line1: кортеж из первого набора координат x1, y1
        :param line2: кортеж из первого набора координат x2, y2
        """
        self.x1 = line1[0]
        self.y1 = line1[1]
        self.x2 = line2[0]
        self.y2 = line2[1]
        self.xmin = min
        self.xmax = max
        self.ymin = min
        self.ymax = max

    def length(self):
        """
        Метод принимает в себя передаваемые характеристики координат
        :return: возвращает длину отрезка, с округлением до 2 знаков после запятой
        """
        segment_length = round(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5, 2)
        # возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
        return segment_length

    def x_axis_intersection(self):
        """
        Метод принимающий в себя координаты точек для расчета пересечения их с осью X
        :return: возвращает True, если отрезок пересекает ось абцисс, иначе False
        """
        self.xmin = min(self.x1, self.x2)  # найти левую и правую границу отрезка
        self.xmax = max(self.x1, self.x2)
        if self.xmin <= 0 <= self.xmax:
            return True
        else:
            return False

    def y_axis_intersection(self):
        """
        Метод принимающий в себя координаты точек для расчета пересечения их с осью Y
        :return: возвращает True, если отрезок пересекает ось ординат, иначе False
        """
        self.ymin = min(self.y1, self.y2)  # найти верхнюю и нижнюю границу отрезка
        self.ymax = max(self.y1, self.y2)
        if self.ymin <= 0 <= self.ymax:
            return True
        else:
            return False


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
