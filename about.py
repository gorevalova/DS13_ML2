import streamlit as st
def about_page():
    st.title('Предсказание музыкального жанра')

    st.write('### Участники проекта:')
    st.write('- Анна Булкина')
    st.write('- Анастасия Горевалова')
    st.write('- Наталья Джога')

    # Добавление изображения
    image = 'data/image_about.png'
    st.image(image)
