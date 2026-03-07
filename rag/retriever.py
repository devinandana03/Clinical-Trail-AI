from rag.vector_store import create_vector_store

vectorstore = create_vector_store()

def retrieve_context(query):

    docs = vectorstore.similarity_search(query,k=3)

    context = "\n".join([d.page_content for d in docs])

    return context