using System;
using FactoryMethodDocuments.Interfaces;

namespace FactoryMethodDocuments.Documents
{
    public class Invoice : IDocument
    {
        public void Open()
        {
            Console.WriteLine("Открыт документ: Счет (Invoice)");
        }
    }
}
