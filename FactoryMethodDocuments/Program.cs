using System;
using FactoryMethodDocuments.Creators;
using FactoryMethodDocuments.Interfaces;

namespace FactoryMethodDocuments
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Выберите тип документа:");
            Console.WriteLine("1 - Отчет (Report)");
            Console.WriteLine("2 - Резюме (Resume)");
            Console.WriteLine("3 - Письмо (Letter)");
            Console.WriteLine("4 - Счет (Invoice)");

            string choice = Console.ReadLine() ?? "";
            DocumentCreator? creator = null;

            if (choice == "1") creator = new ReportCreator();
            else if (choice == "2") creator = new ResumeCreator();
            else if (choice == "3") creator = new LetterCreator();
            else if (choice == "4") creator = new InvoiceCreator();

            if (creator != null)
            {
                IDocument doc = creator.CreateDocument();
                doc.Open();
            }
            else
            {
                Console.WriteLine("Неверный выбор");
            }
        }
    }
}
