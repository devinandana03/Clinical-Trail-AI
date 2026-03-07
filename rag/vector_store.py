from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document

def create_vector_store():

    with open("data/regulatory_guidelines.txt") as f:
        guidelines = f.read()

    with open("data/protocol_template.txt") as f:
        template = f.read()

    docs = [
        Document(page_content=guidelines),
        Document(page_content=template)
    ]

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings()

    vectorstore = FAISS.from_documents(docs, embeddings)

    return vectorstore