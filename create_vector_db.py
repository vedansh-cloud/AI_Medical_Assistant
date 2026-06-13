import os

from src.data_loader import load_pdf
from src.text_splitter import split_documents
from src.embedding_model import get_embeddings
from src.vector_store import create_vector_store

all_docs = []

pdf_folder = "data"

for pdf in os.listdir(pdf_folder):

    if pdf.endswith(".pdf"):

        docs = load_pdf(
            os.path.join(pdf_folder, pdf)
        )

        all_docs.extend(docs)

chunks = split_documents(all_docs)

embeddings = get_embeddings()

create_vector_store(
    chunks,
    embeddings
)

print("FAISS Database Created")