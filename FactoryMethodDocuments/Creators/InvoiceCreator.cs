using FactoryMethodDocuments.Documents;
using FactoryMethodDocuments.Interfaces;

namespace FactoryMethodDocuments.Creators
{
    public class InvoiceCreator : DocumentCreator
    {
        public override IDocument CreateDocument()
        {
            return new Invoice();
        }
    }
}
