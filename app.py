import streamlit as st
from document_process import(
    read_pdf,read_docx,read_txt,chunking
)
from vector_store import VectorStore
from qa_sys import answers_questions

if "vector_store" not in st.session_state:
    st.session_state.vector_store = VectorStore()

st.title("Document Query-Answer Retreival")
uploaded_files=st.file_uploader("Upload Documents",type=["pdf","docx","txt"],
                                accept_multiple_files=True)

if uploaded_files:
    all_chunks=[]
    for file in uploaded_files:
        if file.name.endswith(".pdf"):
            text=read_pdf(file)

        elif file.name.endswith(".docx"):
            text=read_docx(file)

        else:
            text=read_txt(file)

        chunks= chunking(text)
        all_chunks.extend(chunks)

    st.session_state.vector_store.add_documents(all_chunks)
    st.success("Documents uploaded successfully")

    if uploaded_files:
        st.subheader("" \
        "Uploaded Documents")
        for file in uploaded_files:
            st.write(file.name)

    question=st.text_input("Ask a relevant question")

    if st.button("Ask"):
        retrieved_chunks=(st.session_state.vector_store.search(question))
        answer=answers_questions(question, retrieved_chunks)
    
        st.subheader("Answer")
        st.write(answer)
        