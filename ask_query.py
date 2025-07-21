from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import os
import random
import time

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

print("Loading FAISS index...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
print("FAISS index loaded successfully.")

#some lines for fun comeback
fallbacks = [
    "Hmm… I asked Prakshay. He blinked twice and went back to beatboxing.",
    "This ain't on Prakshay's resume, and he refuses to answer without pineapple.",
    "Sorry, my guy only speaks in code and football stats.",
    "That's a general question. But Prakshay prefers chaos. Be specific or be roasted.",
    "I tried asking, but Prakshay just said ‘Skill issue 💀’ and walked off.",
    "He doesn’t know, but he says he’d rather learn than Google it.",
    "This question isn’t covered in the sacred texts of Prakshay.",
    "I don’t know either. Let’s just pretend it never happened.",
    "Error 404: Prakshay didnt see that coming",
]

#we have three models to choose from
model_names = ["llama3.1:8b", "deepseek-r1:1.5b", "deepseek-r1:8b"]
print("*** Note -> The Deepseek models show <think> in their responses, which shows their reasoning. ***\n")

while True:
    try:
        input_model = int(input("Choose a model (1 for llama3.1:8b, 2 for deepseek-r1:1.5b, 3 for deepseek-r1:8b): "))
        if input_model in [1, 2, 3]:
            break
        else:
            print("Enter a valid option (1, 2, or 3).")
    except ValueError:
        print("Enter a valid number.")

model_name = model_names[input_model - 1]

#choosing mode for normal or fun comebacks
mode = int(input("Choose mode   1-> [Normal Mode],       2-> [King Prakshay Mode (got something crazy)]: "))
mode = "King Prakshay Mode" if mode == 2 else "Normal"

#calling my boy
llm = OllamaLLM(model=model_name, callbacks=[StreamingStdOutCallbackHandler()])
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever(),
    return_source_documents=False
)

#shoot ur question phew phew...
print(f"\nAsk your question to {model_name} with ({mode}) — type 'bye' to exit:\n")
while True:
    query = input(f"\n\n Ask: ").strip()

    if query.lower() == "bye":
        print("Bye bye!")
        break

    if not query or len(query.split()) <= 1:
        print("Prakshay raises an eyebrow. Try asking something better .")
        continue

    
    query= query + "if you dont know just say 'I don't know'"
    try:
        result = qa_chain.invoke(query)
        answer = result.get("result", "")

        #when i need to step in huh!
        if "I don't know" in answer or "I do not know" in answer or answer.strip() == "":
            if mode == "King Prakshay Mode":
                time.sleep(0.6)
                print(f"\n"+random.choice(fallbacks))
            

    except Exception as e:
        print(f"Error: {e}")
        if mode == "King Prakshay Mode":
            print(random.choice(fallbacks))
        else:
            print("Something went wrong while processing your query.")
