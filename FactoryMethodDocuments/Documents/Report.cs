using System;
using FactoryMethodDocuments.Interfaces;

namespace FactoryMethodDocuments.Documents
{
    public class Report : IDocument
    {
        public void Open()
        {
            Console.WriteLine("Открыт документ: Отчет (Report)");
        }
    }
}
