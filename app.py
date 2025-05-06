import streamlit as st
import pickle
import pandas as pd
from PIL import Image

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:22]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Page configuration
st.set_page_config(page_title="SEEALL", layout="wide")

# Custom CSS for better styling
st.markdown("""
<style>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px;
}
.logo-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
}
.logo-img {
    width: 50px;
}
.title {
    color: #FF0000;
    font-size: 32px;
    font-weight: bold;
    margin-top: 10px;
    text-align: center;
    letter-spacing: 2px;
}
.movie-title {
    font-size: 18px;
    padding: 10px;
    background-color: #FF0000;
    border-radius: 5px;
    margin: 5px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Container for centering content
st.markdown('<div class="container">', unsafe_allow_html=True)

# Logo container with title
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
# Display the logo
logo = Image.open('seeall.png')
st.image(logo, width=50)
st.markdown('<div class="title">SEEALL</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Movie selection
selected_movie = st.selectbox(
    'Which type of movie do you want to watch?',    
    movies['title'].values
)

st.markdown('</div>', unsafe_allow_html=True)

# Recommendation button and display
if st.button('Show Recommendations'):
    with st.spinner('Finding similar movies...'):
        recommendations = recommend(selected_movie)
        
        # Create 3 columns for better layout
        cols = st.columns(3)
        
        # Display recommendations in columns
        for idx, movie in enumerate(recommendations):
            col_idx = idx % 3
            with cols[col_idx]:
                st.markdown(f'<div class="movie-title">{movie}</div>', unsafe_allow_html=True)
        

