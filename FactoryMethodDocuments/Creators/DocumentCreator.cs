using FactoryMethodDocuments.Interfaces;

namespace FactoryMethodDocuments.Creators
{
    public abstract class DocumentCreator
    {
        public abstract IDocument CreateDocument();
    }
}
