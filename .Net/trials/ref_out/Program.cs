using System;


namespace FeaturesExample
{
    class Program
    {
        static void Main()
        {
            /*Person objPerson = new Person();
            Console.WriteLine("Enter name and Age");
            objPerson.Name = Console.ReadLine();
            objPerson.Age = Convert.ToInt32(Console.ReadLine());
            objPerson.ShowPerson();

            Person objPerson2 = new Person("Ram", 100000);
            objPerson2.ShowPerson();
             * */
            /*int n, m;
            OutExample(3, 4, out n);
            Console.WriteLine( "x + y = " + n);
            m = 0;
            RefExample(5, 10, ref m);
            Console.WriteLine("x + y = " + m);
             * */
            ParamExample(123, "sanjeevi", 50, 60, 70, 80);
            Console.WriteLine();
            ParamExample(125, "somebody", 1, 2, 3, 4, 5);
        }

        public static void ParamExample(int rollno, string name, params int[] marks)
        {
            Console.WriteLine("Roll NO: " + rollno);
            Console.WriteLine("Name: " + name);
            Console.WriteLine("Marks:");
            foreach (int m in marks)
            {
                Console.WriteLine(m);
            }
        }

        public static void RefExample(int x, int y, ref int m)
        {
            m = x + y;
        }

        public static void OutExample(int x, int y, out int n)
        {
            n = x + y;                      
        }
    }

    class Person
    {
        int age;
        string name;

        public Person()
        { 
        }
        public Person(string name, int age)
        {
            this.Age = age;
            this.Name = name;
        }

        public int Age
        {
            get { return age; }
            set { age = value; }
        }      

        public string Name
        {
            get { return name; }
            set { name = value; }
        }

        public void ShowPerson()
        {
            Console.WriteLine("Name: " + this.Name);
            Console.WriteLine("Age: " + this.Age);
        }

    }
}
