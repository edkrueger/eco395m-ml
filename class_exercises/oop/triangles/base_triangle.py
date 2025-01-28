class BaseTriangle():

    def calc_perimeter(self):
        return sum(self._get_sides())
    
    def calc_area(self):
        base, height = self._get_base_height()
        return (1 / 2) * base * height

class EquilateralTriangle(BaseTriangle):

    def __init__(self, side):
        self.side = side

    def _get_sides(self):
        return [self.side, self.side, self.side]
    
    def _get_base_height(self):
        return self.side, self.side * 3 ** (1 / 2) / 2

if __name__ == "__main__":
    equilateral_triangle = EquilateralTriangle(side=2)
    assert equilateral_triangle.calc_area() == 3 ** (1/2)
    assert equilateral_triangle.calc_perimeter() == 6