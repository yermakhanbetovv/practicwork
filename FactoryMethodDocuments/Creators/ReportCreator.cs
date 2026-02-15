using FactoryMethodDocuments.Documents;
using FactoryMethodDocuments.Interfaces;

namespace FactoryMethodDocuments.Creators
{
    public class ReportCreator : DocumentCreator
    {
        public override IDocument CreateDocument()
        {
            return new Report();
        }
    }
}
