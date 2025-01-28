from base_triangle import BaseTriangle
    
class IsoscelesTriangle(BaseTriangle):
    
    def __init__(self, leg, base):

        self.leg = leg
        self.base = base

    def _get_sides(self):

        return (self.leg, self.leg, self.base)
    
    # leave as an exercise
    def _get_base_height(self):
        pass
    
class RightTriangle(BaseTriangle):
    pass
    
if __name__ == "__main__":
    
    right_triangle = RightTriangle(leg_a=3, leg_b=4)
    assert right_triangle.calc_area() == (1 / 2) * 3 * 4
    assert right_triangle.calc_perimeter() == 3 + 4 + 5

    isosceles_triangle  = IsoscelesTriangle(leg=5, base=6)
    assert isosceles_triangle.calc_area() == (1 / 2) * 6 * 4
    assert isosceles_triangle.calc_perimeter() == 6 + 5 + 5
