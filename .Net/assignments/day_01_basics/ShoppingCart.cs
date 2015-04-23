using System;


namespace Shopping
{
    class ShoppingCart
    {
        /*
         * Write a program to do the following:
         * Accept the item code, description, qty and price of an item. Compute the total for the item.
         * Accept the user’s choice. If the choice is ‘y’ then accept the next set of inputs for a new item and compute the total.
         * In this manner, compute the grand total for all the items purchased by the customer.
         * If the grand total is more than Rs. 10,000/- then, the customer is allowed a discount of 10%.
         * If the grand total is less than Rs. 1,000/- and the customer chooses to pay by card, then a surcharge of 2.5% is levied
         * on the grand total. Display the grand total for the customer.
         */
        static void Main()
        {
            bool continue_shopping;
            decimal item_price, total_price = 0.0M;
            int item_code, quantity, payment_mode;
            string item_desc;
            char continue_str;
            const int discount_price = 10000;
            const int surcharge_limit = 1000;
            const decimal surcharge_rate = 0.025M;
            const decimal discount_rate = 10.0M;

            do
            {
                continue_shopping = false;
                Console.WriteLine("Enter item code.");
                if (!int.TryParse(Console.ReadLine(), out item_code))
                {
                    Console.WriteLine("Please enter a valid item code");
                    return;
                }

                Console.WriteLine("Enter item description.");
                item_desc = Console.ReadLine();
                if (item_desc == string.Empty || string.IsNullOrWhiteSpace(item_desc))
                {
                    Console.WriteLine("Please enter a valid item description.");
                    return;
                }

                Console.WriteLine("Enter item quantity.");
                if (!int.TryParse(Console.ReadLine(), out quantity))
                {
                    Console.WriteLine("Please enter valid quantity.");
                    return;
                }

                Console.WriteLine("Enter item price.");
                if (!decimal.TryParse(Console.ReadLine(), out item_price))
                {
                    Console.WriteLine("Please enter valid item price.");
                    return;
                }

                total_price += (quantity * item_price);

                Console.WriteLine("Continue shopping? Press 'Y' to continue adding to cart or 'N' to checkout");
                if (!char.TryParse(Console.ReadLine(), out continue_str))
                {
                    Console.WriteLine("Please enter a valid choice");
                    return;
                }
                else if (char.ToLower(continue_str) == 'y')
                {
                    continue_shopping = true;
                }

            } while (continue_shopping);

            Console.WriteLine();
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");

            if (total_price >= discount_price)
            {
                Console.WriteLine("Congrats!!! \nYou are eligible for discount of rate: " + discount_rate + "%");
                total_price -= total_price * discount_rate / 100;
            }
            else if (total_price < surcharge_limit)
            {
                Console.WriteLine("Hey, looks like your cart is with less number of items. \nChoose your payment mode.\n" + 
                                  "For cash payment, enter '1'\n"+
                                  "For card payment enter '2'\n");
                if (!int.TryParse(Console.ReadLine(), out payment_mode))
                {
                    Console.WriteLine("Please enter valid mode.");
                    return;
                }
                else if (payment_mode == 2)
                {
                    total_price += total_price * surcharge_rate;                    
                } 
            }
            Console.WriteLine("Total amount payable = " + total_price);
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
            Console.WriteLine();
        }
    }
}
