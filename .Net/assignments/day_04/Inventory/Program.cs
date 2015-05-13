using System;


namespace Inventory
{
    public delegate void PublishWarningDelegate(string msg);    
    class Program
    {       
        static void Main()
        {
            PublishWarningDelegate publish_warning = null;  
            try
            {                   
                Console.WriteLine("Enter product id, name, quantity");
                Products products = new Products(int.Parse(Console.ReadLine()), Console.ReadLine(), int.Parse(Console.ReadLine()));
                publish_warning = new PublishWarningDelegate(products.OnOversellEvent);          

                bool proceed = true;
                while (proceed)
                {
                    Console.WriteLine("Choose operation: 1. Add quantity 2. Remove quantity 3. Show qauantity 4. Quit." );
                    int choice;
                    int.TryParse(Console.ReadLine(), out choice);
                    switch (choice)
                    {
                        case 1:
                            Console.WriteLine("Enter quantity to add.");
                            int add = int.Parse(Console.ReadLine());
                            products.AddQuantity(add);
                            break;
                        case 2:
                            Console.WriteLine("Enter quantity to remove.");
                            int remove = int.Parse(Console.ReadLine());
                            if (remove > products.Qoh)
                            {
                                publish_warning.Invoke("Cannot oversell products.");
                            }
                            else
                            { 
                                products.RemoveQuantity(remove);
                            }
                            break;
                        case 3:
                            products.ShowStock();
                            break;
                        case 4:
                            proceed = false;
                            break;
                        default:
                            Console.WriteLine("Enter a valid option");
                            break;
                    }
                }
            }
            catch (FormatException ex)
            {
                Console.WriteLine("Invalid entry!!!\n" + ex.Message);
            }  
        }
    }    

    class Products
    {
        public Products(int product_id, string product_name, int qoh)
        {
            this.product_id = product_id;
            this.product_name = product_name;
            this.qoh = qoh;
        }

        public void OnOversellEvent(string msg)
        {
            Console.WriteLine(msg);
        }

        string product_name;

        public string Product_name
        {
            get { return product_name; }
        }
        int product_id;

        public int Product_id
        {
            get { return product_id; }
        }
        int qoh;

        public int Qoh
        {
            get { return qoh; }
        }

        public void AddQuantity(int quantity)
        {
            qoh += quantity;
        }
        public void RemoveQuantity(int quantity)
        {
            qoh -= quantity;
        }
        public void ShowStock()
        {
            Console.WriteLine("Product Name: " + product_name);
            Console.WriteLine("Product ID: " + product_id);
            Console.WriteLine("Product Quantity: " + qoh);
        }
    }
}
