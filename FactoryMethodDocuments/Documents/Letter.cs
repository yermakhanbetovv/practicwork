using System;
using FactoryMethodDocuments.Interfaces;

namespace FactoryMethodDocuments.Documents
{
    public class Letter : IDocument
    {
        public void Open()
        {
            Console.WriteLine("Открыт документ: Письмо (Letter)");
        }
    }
}
