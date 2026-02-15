using FactoryMethodDocuments.Documents;
using FactoryMethodDocuments.Interfaces;

namespace FactoryMethodDocuments.Creators
{
    public class ResumeCreator : DocumentCreator
    {
        public override IDocument CreateDocument()
        {
            return new Resume();
        }
    }
}
