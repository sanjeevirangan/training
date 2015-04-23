using System;

namespace Salary
{
    class NetAnnualSalary
    {
        /*
         * Write a program to accept name, empId, basic, special allowances, percentage of bonus(10 % of basic)
         * and monthly tax saving investments. The gross monthly salary is basic + special allowances + bonus. 
         * Compute the annual salary. The gross annual salary also includes the bonus. Compute the annual net salary, 
         * by deducting taxes as suggested.
         * Income upto 1 lac – exempted
         * Income from 1 to 1.5 lac – 20%
         * Income from 1.5 lac onwards – 30%
         * However if there is any tax saving investment, then there is further exemption of upto 1 lac annually.
         * This would mean that by having tax saving investments of about 1 lac, an income of 2 lacs is non-taxable. 
         * Display the annual gross, annual net and tax payable.
         */
        static void Main()
        {
            // I/P params:
            string emp_name;
            int emp_id;
            decimal basic, allowance, bonus_rate, investment, tax, monthly_gross_salary, annual_gross_salary, annual_net_salary;

            // Get values from user.
            Console.WriteLine("Enter employee name");
            emp_name = Console.ReadLine();
            if (emp_name == string.Empty || string.IsNullOrWhiteSpace(emp_name))
            {
                Console.WriteLine("Please enter a valid employee name");
                return;
            }

            Console.WriteLine("Enter employee ID");
            if (!int.TryParse(Console.ReadLine(), out emp_id))
            {
                Console.WriteLine("Please enter a valid employee ID");
                return;
            }

            Console.WriteLine("Enter Basic pay");
            if (!decimal.TryParse(Console.ReadLine(), out basic))
            {
                Console.WriteLine("Please enter a valid basic pay");
                return;
            }
            
            Console.WriteLine("Enter special allowances pay");
            if (!decimal.TryParse(Console.ReadLine(), out allowance))
            {
                Console.WriteLine("Please enter a valid special allowance pay");
                return;
            }

            Console.WriteLine("Enter bonus rate");
            if (!decimal.TryParse(Console.ReadLine(), out bonus_rate))
            {
                Console.WriteLine("Please enter a valid bonus rate");
                return;
            }

            Console.WriteLine("Enter total annual investements");
            if (!decimal.TryParse(Console.ReadLine(), out investment))
            {
                Console.WriteLine("Please enter a valid annual investment");
                return;
            }

            monthly_gross_salary = basic + allowance + (basic * bonus_rate / 100);
            annual_gross_salary = monthly_gross_salary * 12;
            tax = ComputeTax(annual_gross_salary, investment);
            annual_net_salary = annual_gross_salary - tax;

            Console.WriteLine();
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
            Console.WriteLine("Employee ID: "  + emp_id + "\n");
            Console.WriteLine("Employee name: " +  emp_name + "\n");
            Console.WriteLine("Monthly gross salary: " + monthly_gross_salary + "\n");
            Console.WriteLine("Annual gross salary: " + annual_gross_salary + "\n");
            Console.WriteLine("Total Investment: " + investment + "\n");
            Console.WriteLine("Tax payable: " + tax + "\n");
            Console.WriteLine("Annual net salary: " + annual_net_salary + "\n");
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
            Console.WriteLine();

        }


        static decimal ComputeTax(decimal gross_income, decimal investment)
        {
            const int max_exemption = 100000;
            const int no_tax_slab = 100000;
            const int twenty_percent_slab = 150000;

            if (gross_income <= no_tax_slab)
            {
                return 0.0M;
            }
            else
            {
                gross_income -= no_tax_slab;  // Exempt the no tax slab.
            }

            // Limit the tax investment exemption to max value.
            if (investment > max_exemption)
            {
                investment = max_exemption;
            }

            decimal taxable_income = gross_income - investment;

            if (taxable_income < twenty_percent_slab)
            {
                return taxable_income * 0.2M;
            }
            else
            {
                return taxable_income * 0.3M;
            }
        }
    }
}
