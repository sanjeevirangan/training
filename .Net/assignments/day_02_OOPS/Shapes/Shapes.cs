using System;


namespace ShapesExample
{
    class Shapes
    {
        // Rectangle
        public static double Area(double width, double height)
        {
            return width * height;
        }
        // Square
        public static double Area(int width, int height)
        {
            return width * height;
        }
        // Circle
        public static double Area(double radius)
        {
            return Math.PI * radius * radius;
        }
        // Triangle
        public static decimal Area(decimal base_val, decimal height)
        {
            return 0.5M * base_val * height;
        }
    }
}
