from base_triangle import BaseTriangle

class RightTriangle(BaseTriangle):
    
    def __init__(self, leg_a, leg_b):
        self.leg_a = leg_a
        self.leg_b = leg_b

    def _get_sides(self):

        leg_a = self.leg_a
        leg_b = self.leg_b

        hypotenuse = (leg_a ** 2 + leg_b ** 2) ** (1 / 2)

        return (leg_a, leg_b, hypotenuse)
    
    def _get_base_height(self):
        return (self.leg_a, self.leg_b)


if __name__ == "__main__":
    right_triangle = RightTriangle(leg_a=3, leg_b=4)
    assert right_triangle.calc_area() == (1 / 2) * 3 * 4
    assert right_triangle.calc_perimeter() == 3 + 4 + 5
