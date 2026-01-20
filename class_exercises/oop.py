triangle_dict = {
    "side_a": 3,
    "side_b": 4,
    "side_c": 5,
    "base": 3,
    "height": 4,
}

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
        
if __name__ == "__main__":
    right_triangle = Triangle(side_a=3, side_b=4, side_c=5, base=3, height=4)
    assert right_triangle.calc_area() == (1 / 2) * 3 * 4
    assert right_triangle.calc_perimeter() == 3 + 4 + 5

    isosceles_triangle = Triangle(side_a=6, side_b=5, side_c=5, base=6, height=4)
    assert isosceles_triangle.calc_area() == (1 / 2) * 6 * 4
    assert isosceles_triangle.calc_perimeter() == 6 + 5 + 5

    equilateral_triangle = Triangle(side_a=2, side_b=2, side_c=2, base=2, height=3 ** (1/2))
    assert equilateral_triangle.calc_area() == (1 / 2) * 2 * 3 ** (1/2)
    assert equilateral_triangle.calc_perimeter() == 2 + 2 + 2

