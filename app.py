import streamlit as st 
import pickle 
import pandas as pd 
import numpy as np 
import requests 

def fetch_poster(movie_id):
    # requests.get('https://api.themoviedb.org/3/movie/1363?api_key')
    response = requests.get('https://api.themoviedb.org/3/movie/1363?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US').format(movie_id)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = new_df[new_df['title']==movie].index[0]
    distances = similarity_matrix[movie_index]
    movies_list = sorted(enumerate(distances),reverse=True,key=lambda x:x[1])
    recommended_movies = []
    for i in movies_list[1:6]:
        movie_id = i[0]
        recommended_movies.append(new_df.iloc[movie_id].title)
    return recommended_movies
        
        

new_dict = pickle.load(open('new_dict.pkl','rb'))
new_df = pd.DataFrame(new_dict)

similarity_matrix = pickle.load(open('similarity_matrix.pkl','rb'))

st.write("Movie Recommender System")

selected_movie_name = st.selectbox(
    'How would you like to be continued?',
    new_df['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)