using System;


namespace MobileDelegate
{
    class Program
    {
        public delegate void Ad(string msg);
        static void Main(string[] args)
        {
            Airtel airtel = new Airtel();
            Vodafone vodafone = new Vodafone();
            Docomo docomo = new Docomo();
            Idea idea = new Idea();
            Ad sms = airtel.Message;
            sms += vodafone.Message;
            sms += idea.Message;
            sms += docomo.Message;
            sms("Congrats 50% off");
            sms -= idea.Message;
            sms("Sell your mobile and go to forest");
        }
    }
}
