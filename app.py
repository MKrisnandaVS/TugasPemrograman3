import streamlit as st
from search_engine import SearchEngine

# Inisialisasi Search Engine
engine = SearchEngine('dataset/data.txt')

# Judul Aplikasi
st.title("Search Engine with Machine Learning")

# Input Query
query = st.text_input("Enter your search query:")

if query:
    # Hasil Pencarian
    st.write("### Search Results:")
    results = engine.search(query)
    for i, (doc, score) in enumerate(results):
        st.write(f"**{i+1}.** {doc} (Score: {score:.4f})")