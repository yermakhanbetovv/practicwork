using FactoryMethodDocuments.Documents;
using FactoryMethodDocuments.Interfaces;

namespace FactoryMethodDocuments.Creators
{
    public class LetterCreator : DocumentCreator
    {
        public override IDocument CreateDocument()
        {
            return new Letter();
        }
    }
}
