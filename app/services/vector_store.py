from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

texts = [
"High income low debt approved",
"Low credit score rejected",
"Borderline cases require manual review"
]

embeddings = OpenAIEmbeddings()

vector_store = Chroma.from_texts(
    texts,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

def retrieve_cases(query,k=2):

    docs = vector_store.similarity_search(query,k=k)

    return [d.page_content for d in docs]
