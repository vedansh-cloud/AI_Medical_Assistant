from src.embedding_model import get_embeddings
from src.retriever import load_vector_store
from src.llm import get_model

from templates.medical_prompt import PROMPT

def generate_answer(question):

    embeddings = get_embeddings()

    db = load_vector_store(
        embeddings
    )

    docs = db.similarity_search(
        question,
        k=3
    )

    context = ""

    sources = []

    for doc in docs:

        context += doc.page_content + "\n"

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        page = doc.metadata.get(
            "page",
            "N/A"
        )

        sources.append(
            f"{source} Page {page}"
        )

    prompt = PROMPT.format(
        context=context,
        question=question
    )

    model = get_model()

    response = model.generate_content(
        prompt
    )

    return response.text, sources