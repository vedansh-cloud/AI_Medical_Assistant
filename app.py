import streamlit as st

from src.rag_pipeline import generate_answer
from src.utils import display_disclaimer

st.set_page_config(
    page_title="AI Medical Assistant",
    layout="wide"
)

st.title("🩺 AI Medical Assistant")

st.markdown(display_disclaimer())

if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input(
    "Ask a medical question"
)

if st.button("Submit"):

    answer, sources = generate_answer(
        question
    )

    st.session_state.history.append(
        {
            "question": question,
            "answer": answer
        }
    )

    st.subheader("Answer")

    st.write(answer)

    st.subheader("Sources")

    for source in sources:

        st.write(source)

st.sidebar.title("Chat History")

for item in st.session_state.history:

    st.sidebar.write(
        "Q: " + item["question"]
    )