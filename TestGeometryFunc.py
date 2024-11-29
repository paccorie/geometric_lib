import unittest
import math
import square
import rectangle
import circle
import triangle
            
class squareTest(unittest.TestCase):
    def test_square_area(self):
        self.assertEqual(square.area(4), 16) 

    def test_square_area_null(self):
        self.assertEqual(square.area(0), 0) 

    def test_square_area_negative(self):
        self.assertEqual(square.area(-3), 0) 

    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(4), 16)
    
    def test_square_perimeter_null(self):
        self.assertEqual(square.perimeter(0), 0)

    
    def test_square_perimeter_negative(self):
        self.assertEqual(square.perimeter(-3), 0)

    
class rectangleTest(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(4, 5), 20)

    def test_rectangle_area_null(self):
        self.assertEqual(rectangle.area(0, 5), 0)
    
    def test_rectangle_area_negative(self):
        self.assertEqual(rectangle.area(-4, 5), 0)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(4, 5), 18)

    def test_rectangle_perimeter_null(self):
        self.assertEqual(rectangle.perimeter(0, 5), 0)

    def test_rectangle_perimeter_negative(self):
        self.assertEqual(rectangle.perimeter(-4, 5), 0)


    
class circleTest(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(circle.area(3), math.pi * 9)

    def test_circle_area_null(self):
        self.assertEqual(circle.area(0), 0)

    def test_circle_area_negative(self):
        self.assertEqual(circle.area(-3), 0 )

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(3), 2 * math.pi * 3)
    
    def test_circle_perimeter_null(self):
        self.assertEqual(circle.perimeter(0), 0)
    
    def test_circle_perimeter_negative(self):
        self.assertEqual(circle.perimeter(-3), 2 * math.pi * 3)

    
class triangleTest(unittest.TestCase):
    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12) 


    def test_triangle_perimeter_null(self):
        self.assertEqual(triangle.perimeter(5, 7, 0), 0) 


    def test_triangle_perimeter_negative(self):
        self.assertEqual(triangle.perimeter(5, -5, 6), 0) 

    def test_triangle_perimeter_notexist(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 1, 3) 

if __name__ == '__main__':
    unittest.main()
