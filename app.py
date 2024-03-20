import streamlit as st
from about import about_page
from EDA import eda_page
from model import model_page
from model_selection import select_page

# Главная страница
def main():

    st.set_page_config(page_title='Музыкальный проект', page_icon="random")

    st.title('Групповой проект по ML')

    page = st.sidebar.radio('Выберите страницу', ['О проекте', 'Графики', 'Модель', 'Предсказание по песне'])

    if page == 'О проекте':
        about_page()
    elif page == 'Графики':
        eda_page()
    elif page == 'Модель':
        model_page()
    elif page == 'Предсказание по песне':
        select_page()

if __name__ == '__main__':
    main()
