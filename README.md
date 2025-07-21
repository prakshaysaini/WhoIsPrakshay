# WhoIsPrakshay.AI

This is a context-aware chatbot powered by LLM QA chains that understands and answers queries specifically about Prakshay using a local context file. It showcases how you can build a personal assistant that answers questions only from a fixed source, without relying on external internet-based searches.
- Built with LangChain  
- Powered by Ollama

## *Why is it worth your time

- You can provide your own pdf, maybe a lecture pdf, a literature, song lyrics and much more.
- Just run the preprocessor.py on your pdf and start ask_query.py
- Now You can talk to model in context with your own file, boom!! now you can prepare for exams more efficiently

---

## 🔹 Project Overview

This project implements a Question Answering system using:

- LangChain QA Chain (RetrievalQA)

- Local LLM (via Ollama)

- Vector embeddings (via FAISS)

- Contextual document (Prakshay's bio/info in .pdf form)

- The chatbot is highly focused — it doesn't hallucinate, and it answers only based on Prakshay's personal info provided in the context.

---

## 🔹 File Structure
```
├── faiss_index/             # Preprocessed FAISS files to avoid recomputation
├── preprocess.py            # Parses and indexes the knowledge base using FAISS
├── p_info.pdf               # Knowledge base for the chatbot
├── ask_query.py             # Main script to handle user queries
├── requirements.txt         # List of dependencies
└── README.md                # You're here!
```

  ---
  
## 🔹 How It Works  (***the only interesting part for most readers)
  1. Context Embedding
- The file context/p_info.pdf contains all the info about me/Prakshay given by myself.

- It is split into chunks using LangChain's CharacterTextSplitter.

- These chunks are converted into vector embeddings using OllamaEmbeddings.

- All chunk embeddings are stored in a local FAISS index for fast retrieval.

2. QA Chain Construction
- The vector store is queried based on user questions.

- Top k=4(Default) relevant chunks are retrieved from FAISS.

- The local LLM (llama3, via Ollama) is used to answer the question using only the retrieved chunks.

- RetrievalQA ensures the LLM sticks to the context and avoids hallucination.


All logic is loaded on app start — context is embedded once per run.

## 🔹 Sample Queries outputs
  <img width="1453" height="185" alt="image" src="https://github.com/user-attachments/assets/7d8d28c4-68ca-4eb9-9ec9-25447e11722e" />

## Starting Questions
<img width="1455" height="369" alt="image" src="https://github.com/user-attachments/assets/234d6953-d144-49e3-882e-dee4f283c404" />

- Preffered model name and Mode is asked
  
- King Prakshay Mode just have some comeback strings, when the model is unsure
  
- Ignore warning as you always do.(this one is due to libraries update)

# 🔹 How To Run
---
## Getting Started with Ollama (Offline LLaMA)

To run this chatbot offline using a local LLM (no OpenAI keys needed), follow these steps:

### Step 1: Install Ollama

Download and install Ollama from the official site:  
https://ollama.com/download

Choose your OS (Windows, macOS, Linux) and follow the installation instructions.

---

### Step 2: Download the Model

```

ollama pull llama3.1:8b          <(deepseek-r1:1.5b and deepseek-r1:8b also used in this bot)>
```
You can also pull other models like `mistral`, `gemma`, or `llama2`.But then change the code according to the downloaded LLM

---

### Step 3: Start the ChatBot

Once the model is downloaded and Ollama is running in the background:

** In Terminal **

```
python ask_query.py
```
## Installation & Setup

### Step 1: Clone the Repo

```

git clone https://github.com/prakshaysaini/WhoIsPrakshay
```
cd WhoIsPrakshay

### Step 2: Install Python Requirements

```

pip install -r requirements.txt
```
---

### Step 3: Preprocess and RUN
```
python preprocess.py
python ask_query.py
```
## Author

**Prakshay Saini**  
---
