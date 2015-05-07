using System;


namespace Interface_Example_01
{
    class Program
    {
        static void Main()
        {
            Bird objBird = new Bird();
            objBird.fly();
            Console.WriteLine();

            Plane objPlane = new Plane();
            Console.WriteLine(objPlane.brandname());
            Console.WriteLine(objPlane.logo());
            objPlane.GetData();
            objPlane.ShowData();
            Console.WriteLine();

            Train objTrain = new Train();
            Console.WriteLine(objTrain.brandname());
            Console.WriteLine(objTrain.logo());
            objTrain.GetData();
            objTrain.ShowData();
        }
    }

    abstract class PassengerDetails
    {
        protected int pnrno;
        protected string name;
        protected double mobno;
        public abstract void GetData();
        public abstract void ShowData();

    }

    interface IFlying
    {
        void fly();
    }

    interface IAdvertisement
    {
        string brandname();
        string logo();
    }

    class Bird:IFlying
    {
        public void fly()
        {
            Console.WriteLine("Flap Flap... Go to Canada without VISA");
        }
    }

    class Plane:PassengerDetails, IFlying, IAdvertisement
    {
        public void fly()
        {
            Console.WriteLine("Arise up above and pollute the Skies");
        }

        public string brandname()
        {
            return "Smoke Asia";
        }

        public string logo()
        {
            return "No flight for this route";
        }

        public override void GetData()
        {
            pnrno = 12345;
            name = "sanjeevi";
            mobno = 9886564123;
        }

        public override void ShowData()
        {
            Console.WriteLine(pnrno + "," +  name + "," + mobno);
        }
    }

    class Spiderman : IFlying
    {
        public void fly()
        {
            Console.WriteLine("Flying... but still render is in progress");
        }
    }

    class Train : PassengerDetails, IAdvertisement
    {

        public string brandname()
        {
            return "ISCTC";
        }

        public string logo()
        {
            return "Always stinks";
        }

        public override void GetData()
        {
            pnrno = 12345;
            name = "sanjeevi";
            mobno = 9886564123;
        }

        public override void ShowData()
        {
            Console.WriteLine(pnrno + "," + name + "," + mobno);
        }
    }
}
