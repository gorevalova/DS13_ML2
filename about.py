import streamlit as st

def about_page():
    st.title('Предсказание музыкального жанра')

    st.write('### Участники проекта:')
    st.write('- Анна Булкина')
    st.write('- Анастасия Горевалова')
    st.write('- Наталья Джога')

    # Добавление изображения
    image = 'data/image_about.png'  # Поменяйте 'your_image.png' на путь к вашему изображению
    st.image(image)
