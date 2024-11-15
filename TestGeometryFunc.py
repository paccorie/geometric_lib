import unittest
import math
import square
import rectangle
import circle
import triangle

class TestGeometryFunctions(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(square.area(4), 16)
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.area(-3), 0)  

    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(4), 16)
        self.assertEqual(square.perimeter(0), 0)
        self.assertEqual(square.perimeter(-3), 0)  

    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(4, 5), 20)
        self.assertEqual(rectangle.area(0, 5), 0)
        self.assertEqual(rectangle.area(-4, 5), 0)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(4, 5), 18)
        self.assertEqual(rectangle.perimeter(0, 5), 0)
        self.assertEqual(rectangle.perimeter(-4, 5), 0)

    def test_circle_area(self):
        self.assertAlmostEqual(circle.area(3), math.pi * 9)
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.area(-3), 0 )

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(3), 2 * math.pi * 3)
        self.assertEqual(circle.perimeter(0), 0)
        self.assertEqual(circle.perimeter(-3), 2 * math.pi * 3)

    def test_triangle_area(self):
        self.assertEqual(triangle.area(3, 5), 15)  
        self.assertEqual(triangle.area(5, 0), 0)  
        self.assertEqual(triangle.area(-2, 3), 0)  


    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12) 
        self.assertEqual(triangle.perimeter(5, 7, 0), 0) 
        self.assertEqual(triangle.perimeter(5, -5, 6), 0) 

        with self.assertRaises(ValueError):
            triangle.perimeter(1, 1, 3) 

if __name__ == '__main__':
    unittest.main()
