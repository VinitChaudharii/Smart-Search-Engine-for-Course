import streamlit as st
import pandas as pd
from Search_engine import CourseSearchSystem

# Initialize the search system
df = pd.read_csv('course_data.csv')
search_system = CourseSearchSystem()
search_system.load_and_prepare_data(df)

# Streamlit page setup
st.set_page_config(
    page_title="Analytics Vidhya Course Search",
    layout="centered",
    initial_sidebar_state="auto"
)

# Title and description
st.title("Analytics Vidhya Free Course Search")
st.markdown("""
Find the perfect free course from Analytics Vidhya's collection using natural language search.  
Simply describe what you're looking for!
""")

# Input fields
query = st.text_input(
    "What would you like to learn?",
    placeholder="E.g., 'machine learning for beginners' or 'computer vision projects'"
)
num_results = st.slider(
    "Number of results to show:",
    min_value=1,
    max_value=10,
    value=3,
    step=1
)

# Search button
if st.button("🔍 Search Courses"):
    if not query.strip():
        st.warning("Please enter a search query to find relevant courses!")
    else:
        results = search_system.search_courses(query, top_k=num_results)
        st.markdown("### Search Results:")
        if isinstance(results, list) and results:
            for i, result in enumerate(results, 1):
                st.markdown(f"**{i}. {result}**")
        else:
            st.info("No courses found. Try refining your query!")

# Footer
st.markdown("""
---
Made with Sentence Transformers and Streamlit
""")
