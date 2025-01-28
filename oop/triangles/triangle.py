# this is just to motivate the idea of the constructor
def silly_triangle(side_a, side_b, side_c, base, height):

    self = {}

    self["side_a"] = side_a
    self["side_b"] = side_b
    self["side_c"] = side_c
    self["base"] = base
    self["height"] = height

    return self

class Triangle():

    def __init__(self, side_a, side_b, side_c, base, height):

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        self.base = base
        self.height = height

    def calc_area(self):
        return (1 / 2) * self.base * self.height
    
    def calc_perimeter(self):
        return self.side_a + self.side_b + self.side_c
    
class EquilateralTriangleOne(Triangle):

    def __init__(self, side):

        self.side_a = side
        self.side_b = side
        self.side_c = side

        self.base = side
        self.height = side * 3 ** (1/2) / 2

if __name__ == "__main__":

    right_triangle = Triangle(side_a=3, side_b=4, side_c=5, base=3, height=4)
    assert right_triangle.calc_area() == 6
    assert right_triangle.calc_perimeter() == 12

    isosceles_triangle = Triangle(side_a=6, side_b=5, side_c=5, base=6, height=4)
    assert isosceles_triangle.calc_area() == 12
    assert isosceles_triangle.calc_perimeter() == 16

    equilateral_triangle = Triangle(side_a=2, side_b=2, side_c=2, base=2, height=3 ** (1/2))
    assert equilateral_triangle.calc_area() == 3 ** (1/2)
    assert equilateral_triangle.calc_perimeter() == 6

    equilateral_triangle_one = EquilateralTriangleOne(side=2)
    assert equilateral_triangle_one.calc_area() == 3 ** (1/2)
    assert equilateral_triangle_one.calc_perimeter() == 6


    
