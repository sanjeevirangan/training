using System;


namespace GeometricShapes
{
    class Program
    {
        static void Main()
        {
            Circle objcircle = new Circle(10, "red", 50.0);
            Console.WriteLine(objcircle.ToString());
            Console.WriteLine("Area: " + Convert.ToString(objcircle.findArea()));
            Console.WriteLine("Perimeter: " + Convert.ToString(objcircle.findPerimeter()));
        }
    }

    class Circle : GeometricObject
    {
        int radius;
        //new string color;
        public Circle(int radius)
        {
            this.radius = radius;
        }
        public Circle(int radius, string color, double weight)
        {
            this.radius = radius;
            this.weight = weight;
            this.color = color;
        }

        public override double findArea()
        {
            return Math.PI * Math.Pow(radius, 2);
        }

        public override double findPerimeter()
        {
            return 2 * Math.PI * radius;
        }

        // Overriding ToString() method of Object
        public override string ToString()
        {
            return base.ToString() + "\nColor:" + this.color +
                ", Radius: " + this.radius + ", Weight: " + this.weight;
        }
    }

    public abstract class GeometricObject
    {
        protected string color;
        protected double weight;
        // Default construct
        protected GeometricObject()
        {
            color = "white";
            weight = 1.0;
        }
        // Construct a geometric object
        protected GeometricObject(string color, double weight)
        {
            this.color = color;
            this.weight = weight;
        }
        public string Color
        {
            get
            {
                return color;
            }
            set
            {
                color = value;
            }
        }
        public double Weight
        {
            get
            {
                return weight;
            }
            set
            {
                weight = value;
            }
        }
        // Abstract method
        public abstract double findArea();
        // Abstract method
        public abstract double findPerimeter();
    }
}
