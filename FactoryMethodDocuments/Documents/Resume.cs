using System;
using FactoryMethodDocuments.Interfaces;

namespace FactoryMethodDocuments.Documents
{
    public class Resume : IDocument
    {
        public void Open()
        {
            Console.WriteLine("Открыт документ: Резюме (Resume)");
        }
    }
}
