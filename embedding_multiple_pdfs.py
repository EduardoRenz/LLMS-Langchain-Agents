# This example show how to find texts in a document using indexes
# %%
from llm_factory import create_model
# from llm_models.ollama import create_model
from langchain.globals import set_debug

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts.chat import ChatPromptTemplate
from langchain import hub

set_debug(False)
llm = create_model()
llm.temperature = 0.0
# %%
loaders = [PyPDFLoader("data/ManualdaBrasa.pdf")]
documents = []
for loader in loaders:
    documents.extend(loader.load())

splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = splitter.split_documents(documents)

# %%
embeddings = OpenAIEmbeddings()
# db = FAISS.from_documents(texts, embeddings)
# db.save_local("faiss_index")
db = FAISS.load_local("faiss_index", embeddings,
                      allow_dangerous_deserialization=True)
# %%
retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
combine_docs_chain = create_stuff_documents_chain(
    llm, retrieval_qa_chat_prompt)


qa_chain = create_retrieval_chain(
    retriever=db.as_retriever(), combine_docs_chain=combine_docs_chain)

# %%
question = "Qual a vantagem da grelha?"
answer = qa_chain.invoke({"input": question})


# %%
