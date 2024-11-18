import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

if __name__ == '__main__':
    print("loading...")
    loader = TextLoader('C:/Users/mical/Desktop/LangChain/vector_dbs/mediumblog.txt', encoding='utf-8')
    document = loader.load()

    print("splitting...")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(f"created {len(texts)} chunks")

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

    print("ingesting...")

    PineconeVectorStore.from_documents(texts, embeddings, index_name=os.environ.get("INDEX_NAME"), )

    print("finish")