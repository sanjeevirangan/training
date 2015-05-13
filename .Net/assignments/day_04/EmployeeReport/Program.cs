using System;
using System.Collections.Generic;


namespace EmployeeReport
{
    class Program
    {


        static void Main()
        {
            List<Employee> Employee_List = new List<Employee>();
            int Incentive_Counter = 0;
            double Total_Incentive = 0;
            double Total_Gross_Salary = 0;
            bool proceed = true;
            Employee objEmployee;

            while (proceed)
            {
                try
                {
                    Console.WriteLine("Enter employee name");
                    string emp_name = Console.ReadLine();
                    Console.WriteLine("Enter employee ID");
                    int emp_id = int.Parse(Console.ReadLine());
                    objEmployee = new Employee(emp_id, emp_name);
                    Console.WriteLine("Enter the number of hours worked");
                    objEmployee.Hours_worked = double.Parse(Console.ReadLine());
                    if (objEmployee.Incentive > 0)
                    {
                        Incentive_Counter += 1;
                        Total_Incentive += objEmployee.Incentive;
                    }
                    Total_Gross_Salary += objEmployee.Gross_salary;
                    Employee_List.Add(objEmployee);
                    Console.WriteLine("Enter 1 to add employee.");
                    int choice = 0;
                    int.TryParse(Console.ReadLine(), out choice);
                    if (choice != 1)
                    {
                        proceed = false;
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
            }
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
            Console.WriteLine();
            foreach (Employee emp in Employee_List)
            {
                Console.WriteLine("Employee Name: " + emp.Emp_name);
                Console.WriteLine("Employee ID: " + emp.Emp_id);
                Console.WriteLine("Hours Worked: " + emp.Hours_worked);
                Console.WriteLine("Gross Salary: " + emp.Gross_salary);
                Console.WriteLine("Incentive Paid: " + emp.Incentive);
                Console.WriteLine("======================================================================");

            }
            Console.WriteLine();
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
            Console.WriteLine("Total number of employees eligible for incentive: " + Incentive_Counter);
            Console.WriteLine("Total incentive paid: " + Total_Incentive);
            Console.WriteLine("Total gross salary paid: " + Total_Gross_Salary);
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
        }
    }

    class Employee
    {
        const double Hourly_Wage = 4.50;
        const int Incentive_Limit = 720;
        const double Incentive_Rate = 0.05;
        int emp_id;
        public int Emp_id
        {
            get { return emp_id; }
        }
        string emp_name;
        public string Emp_name
        {
            get { return emp_name; }
        }
        double hours_worked;
        public double Incentive
        {
            get
            {
                double incentive = 0;
                if (HasIncentive())
                {
                    incentive = (Incentive_Rate * Gross_salary);
                }
                return incentive;
            }
        }

        public double Gross_salary
        {
            get { return (hours_worked * Hourly_Wage); }
        }

        public double Hours_worked
        {
            get { return hours_worked; }
            set { hours_worked = value; }
        }

        public Employee(int emp_id, string emp_name)
        {
            this.emp_id = emp_id;
            this.emp_name = emp_name; 
        }

        public bool HasIncentive()
        {
            if (Gross_salary > Incentive_Limit)
            {
                return true;
            }
            return false; 
        }
    }
}
