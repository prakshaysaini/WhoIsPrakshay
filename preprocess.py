from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Step 1: Load PDF
loader = PyPDFLoader("p_info.pdf")  # Change filename
pages = loader.load()

# Step 2: Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
documents = text_splitter.split_documents(pages)

# Step 3: Generate Embeddings using local model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(documents, embedding_model)
vectorstore.save_local("faiss_index")
print("Vectorstore saved as 'faiss_index'")
