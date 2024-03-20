import streamlit as st
import pickle
import pandas as pd
def select_page():
        st.write("# Прогноз музыкального жанра")

        # Форма для ввода параметров
        track_name = st.text_input('Название трека')
        acousticness = st.slider('Акустичность', min_value=0.0, max_value=1.0, value=0.2, step=0.01)
        danceability = st.slider('Танцевальность', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        duration_ms = st.slider('Продолжительность', min_value=0.0, max_value=40000.0, value=500.0, step=0.01)
        energy = st.slider('Энергичность', min_value=0.0, max_value=1.0, value=0.6, step=0.01)
        instrumentalness = st.slider('Инструментальность', min_value=0.0, max_value=1.0, value=0.2, step=0.001)
        key = st.selectbox('Тональность', ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'))
        liveness = st.slider('Живость', min_value=0.0, max_value=1.0, value=0.2, step=0.01)
        loudness = st.slider('Громкость', min_value=-40.0, max_value=0.0, value=-7.0, step=0.1)
        mode = st.selectbox('Лад', ('Мажор', 'Минор'))
        speechiness = st.slider('Выразительность', min_value=0.0, max_value=1.0, value=0.2, step=0.01)
        tempo = st.slider('Тем', min_value=0.0, max_value=200.0, value=100.0, step=0.01)
        valence = st.slider('Привлекательность', min_value=0.0, max_value=1.0, value=0.5, step=0.01)

        if st.button('Предсказать'):
            # Обработка введенных параметров
            mode = 1 if mode == 'Мажор' else -1
            track_name = int(len(track_name))

            data = {
                'track_name': [track_name],
                'acousticness': [acousticness],
                'danceability': [danceability],
                'duration_ms': [duration_ms],
                'energy': [energy],
                'instrumentalness': [instrumentalness],
                'key': [key],
                'liveness': [liveness],
                'loudness': [loudness],
                'mode': [mode],
                'speechiness': [speechiness],
                'tempo': [tempo],
                'valence': [valence]
            }

            user_input = pd.DataFrame(data)

            with open('data/final_model_test.pkl', 'rb') as file:
                model = pickle.load(file)

            # Предсказание музыкального жанра
            prediction = model.predict(user_input)

            prediction_genre_clean = prediction[0].item().replace('[', '').replace(']', '').replace("'", "")

            # Вывод предсказанного музыкального жанра
            st.write(f"Предсказанный музыкальный жанр: {prediction_genre_clean}")

            # Визуализация воздушных шариков
            st.balloons()
