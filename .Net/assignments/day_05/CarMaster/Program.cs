using System;


namespace CarMaster
{
    class Program
    {
        static void Main()
        {
            
            try
            {
                Console.WriteLine("Enter car-1 details.\nmodel name, company, engine capacity\n");
                Car car1 = new Car(Console.ReadLine(), Console.ReadLine(), double.Parse(Console.ReadLine()));
                car1.DisplayCarDetails();

                Console.WriteLine("Enter car-2 details.\nmodel name, company, engine capacity\n");
                Car car2 = new Car(Console.ReadLine(), Console.ReadLine(), double.Parse(Console.ReadLine()));
                car2.DisplayCarDetails();

                if (car1 > car2)
                {
                    Console.WriteLine("Capacity of car1 is greater than that of car2.\n");
                }
                else
                {
                    Console.WriteLine("Capacity of car2 is greater than that of car1.\n");
                }

                if (car1 < car2)
                {
                    Console.WriteLine("Capacity of car1 is lesser than that of car2.\n");
                }
                else
                {
                    Console.WriteLine("Capacity of car2 is lesser than that of car1.\n");
                }

            }
            catch (FormatException ex)
            {
                Console.WriteLine("Invalid data.\n" + ex.Message);
            }
        }                
    }

    enum Transmission
    {
        Automatic,
        Manual,
        Hybrid
    }

    class Car
    {
        protected string model_name, company, car_type;
        protected Transmission transmission_type;
        protected int engine_type;
        protected double engine_capacity;


        public Transmission Transmission_type
        {
            get { return transmission_type; }
        }
        public int Engine_type
        {
            get { return engine_type; }
        }
        public double Engine_capacity
        {
            get { return engine_capacity; }
        }
        public string CarType
        {
            get { return car_type; }
        }
        public string Company
        {
            get { return company; }
        }
        public string Model_name
        {
            get { return model_name; }
        }


        // constructor
        public Car(string model_name, string company, double engine_capacity, string car_type = "sedan", int engine_type = 4, Transmission transmission_type = Transmission.Automatic)
        {
            this.model_name = model_name;
            this.company = company;
            this.engine_capacity = engine_capacity;
            this.car_type = car_type;
            this.engine_type = engine_type;
            this.transmission_type = transmission_type;
        }

        // Public Methods
        public void TransformCar(ref Car objCar, double capacity, int type, Transmission transmission)
        {
            objCar.engine_capacity = capacity;
            objCar.engine_type = type;
            objCar.transmission_type = transmission;
        }
        public void DisplayCarDetails()
        {
            Console.WriteLine("Company: " + this.Company);
            Console.WriteLine("Model name: " + this.Model_name);
            Console.WriteLine("Model type: " + this.CarType);
            Console.WriteLine("Engine capacity: " + this.Engine_capacity);
            Console.WriteLine("Engine type: " + this.Engine_type);
            Console.WriteLine("Transmission: " + this.Transmission_type);
        }
        public static bool operator >(Car car1, Car car2)
        {
            if (IsSameCategory(car1, car2) && car1.Engine_capacity > car2.Engine_capacity)
            {
                return true;
            }
            return false;
        }
        public static bool operator <(Car car1, Car car2)
        {
            if (IsSameCategory(car1, car2) && car1.Engine_capacity < car2.Engine_capacity)
            {
                return true;
            }
            return false;
        }

        // Private Methods
        static bool IsSameCategory(Car c1, Car c2)
        {
            return (c1.CarType == c2.CarType && c1.Engine_type == c2.Engine_type && c1.Transmission_type == c2.Transmission_type) ? true : false;
        }
    }
}
