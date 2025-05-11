import bz2
import pickle
import pandas as pd

import streamlit as st


def searched(anime):
    searched_anime_data = []
    searched_anime_poster = []
    anime_index = anime_name[anime_name['title'] == anime].index[0]
    searched_anime_poster.append(anime_name.iloc[anime_index].img_url)
    searched_anime_data.append(anime_name.iloc[anime_index].synopsis)
    searched_anime_data.append(anime_name.iloc[anime_index].genre)
    searched_anime_data.append(anime_name.iloc[anime_index].episodes)
    searched_anime_data.append(anime_name.iloc[anime_index].score)
    searched_anime_data.append(anime_name.iloc[anime_index].link)

    return searched_anime_data, searched_anime_poster


def recommend(anime):
    anime_index = anime_name[anime_name['title'] == anime].index[0]
    distances = similarity[anime_index]
    anime_recommended = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_anime = []
    recommended_anime_poster = []
    for i in anime_recommended:
        anime_id = i[0]
        # fetch poster
        recommended_anime_poster.append(anime_name.iloc[i[0]].img_url)
        recommended_anime.append(anime_name.iloc[i[0]].title)
    return recommended_anime, recommended_anime_poster


anime_name = pd.read_csv('animes.csv')
anime_name['genre'] = anime_name['genre'].apply(eval).apply(', '.join)


# similarity = pickle.load(open('similarity.pkl', 'rb'))


def decompress_pickle(file):
    similarity = bz2.BZ2File(file, 'rb')
    similarity = pickle.load(similarity)
    return similarity


similarity = decompress_pickle('x_similarity.pbz2')

st.title("Anime Recommendation System")
selected_name = st.selectbox('Type the name of Anime',
                             anime_name['title'].values)

if st.button('Search'):
    searched_anime_info, searched_poster = searched(selected_name)
    searched, description = st.columns(2)
    with searched:
        searched.image(searched_poster)
    with description:
        description.subheader(selected_name)
        description.write("Genre: " + searched_anime_info[1])
        description.write("Episodes: ")
        description.write(searched_anime_info[2])
        description.write("Rating: ")
        description.write(searched_anime_info[3])
        description.write("Link: " + searched_anime_info[4])
    st.caption(searched_anime_info[0])

    st.header("Recommended")
    recommendations, posters = recommend(selected_name)

    col2, col3, col4 = st.columns(3)
    with col2:
        col2.write(recommendations[1])
        col2.image(posters[1])
    with col3:
        col3.write(recommendations[2])
        col3.image(posters[2])
    with col4:
        col4.write(recommendations[3])
        col4.image(posters[3])

    col5, col6, col7 = st.columns(3)
    with col5:
        col5.write(recommendations[4])
        col5.image(posters[4])
    with col6:
        col6.write(recommendations[5])
        col6.image(posters[5])
    with col7:
        col7.write(recommendations[6])
        col7.image(posters[6])

    col8, col9, col10 = st.columns(3)
    with col8:
        col8.write(recommendations[7])
        col8.image(posters[7])
    with col9:
        col9.write(recommendations[8])
        col9.image(posters[8])
    with col10:
        col10.write(recommendations[9])
        col10.image(posters[9])
