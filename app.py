import streamlit as st
import pandas as pd
from course_search import CourseSearchSystem

# Initialize the search system
df = pd.read_csv('course_data.csv')
search_system = CourseSearchSystem()
search_system.load_and_prepare_data(df)

def search_courses(query: str, num_results: int) -> str:
    """Search function for Streamlit interface"""
    if not query.strip():
        return "Please enter a search query to find relevant courses!"
    
    return search_system.search_courses(query, top_k=num_results)

# Streamlit page configuration
st.set_page_config(
    page_title="Analytics Vidhya Course Search",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded",
)

# App title
st.markdown(
    """
    # Analytics Vidhya Free Course Search
    Find the perfect free course.
    Simply describe what you're looking for!
    ---
    """,
    unsafe_allow_html=True,
)

# Input fields
query = st.text_input(
    label="What would you like to learn?",
    placeholder="E.g., 'machine learning' or 'computer vision'",
    help="Enter a search query to find relevant courses."
)

num_results = st.slider(
    label="Number of results to show",
    min_value=1,
    max_value=10,
    value=3,
    step=1,
    help="Select the number of results you want to see."
)

# Search button
if st.button("🔍 Search Courses"):
    if not query:
        st.warning("Please enter a search query to proceed.")
    else:
        with st.spinner("Searching for courses..."):
            results = search_courses(query, num_results)
            st.markdown("### Search Results")
            if isinstance(results, str):
                st.info(results)
            else:
                for idx, result in enumerate(results, start=1):
                    st.markdown(f"**{idx}. {result}**")
                    st.markdown("---")

# Footer
st.markdown(
    """
    ---
    *Made with Sentence Transformers and Streamlit*
    """,
    unsafe_allow_html=True
)
