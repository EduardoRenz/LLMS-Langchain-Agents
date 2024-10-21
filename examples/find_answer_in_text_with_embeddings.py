# This example show how to find texts in a document using indexes

from llm_models.openai import create_model
# from llm_models.ollama import create_model
from langchain.globals import set_debug


from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

set_debug(False)
llm = create_model()


loader = TextLoader("data/lumorules.txt")
documents = loader.load()

splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = splitter.split_documents(documents)


embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(texts, embeddings)

qa_chain = RetrievalQA.from_chain_type(
    llm, retriever=db.as_retriever(), chain_type="stuff")

question = "Quantos jogadores tem cada time?"
print(qa_chain.invoke(question))

question = "O que acontece se tiver empate?"

print(qa_chain.invoke(question))
