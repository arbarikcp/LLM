from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import BasePromptTemplate
from langchain_core.prompts import BaseChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

from langchain_community.document_loaders import WebBaseLoader

from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.chains.combine_documents import create_stuff_documents_chain

from langchain.tools.retriever import create_retriever_tool


loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()
print(len(docs))
# print(docs)

embeddings = OpenAIEmbeddings()


text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
print("number of docuemnts=",len(documents))
vector = FAISS.from_documents(documents, embeddings)
FAISS.from_documents
