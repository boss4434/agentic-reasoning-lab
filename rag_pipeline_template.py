documents = [
    "Retail demand fluctuates with promotions and holidays.",
    "Machine learning models can predict inventory shortfalls.",
    "AWS Bedrock enables scalable LLM orchestration.",
]

def retrieve(query):
    matches = [d for d in documents if any(word in d.lower() for word in query.lower().split())]
    return matches or ["No relevant context found."]

def summarize(contexts):
    print("\nRetrieved Context:")
    for c in contexts:
        print("-", c)
    return f"Summary: based on {len(contexts)} retrieved facts, suggest adjusting forecast dynamically."

def rag_pipeline(query):
    contexts = retrieve(query)
    summary = summarize(contexts)
    print("\nRAG Output:\n", summary)

if __name__ == "__main__":
    rag_pipeline("inventory forecast")
