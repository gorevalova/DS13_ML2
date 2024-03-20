import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def eda_page():

    # Загрузка файла train_data.csv из папки data
    file_path = 'data/train_data.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)

        st.write("### Пример тренировочных данных:")
        st.write(df.head())

        st.title("Графики на основе данных")

        # График для acousticness
        st.write("### Количество уникальных значений")
        fig = plt.figure(figsize=(16, 5))
        cols = df.columns
        uniques = [len(df[col].unique()) for col in cols]
        ax = sns.barplot(x=cols, y=uniques, palette="muted", log=True)
        ax.set(xlabel='Признак', ylabel='log(количество уникальных значений)',
               title='Количество уникальных значений по признакам')
        for p, uniq in zip(ax.patches, uniques):
            ax.text(p.get_x() + p.get_width() / 2., uniq + 10, uniq, ha='center')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        st.pyplot(fig)

        st.write("### Уровень аккустичности для классической музыки и рока")
        bins = 17
        fig = plt.figure(figsize=(10, 6))
        plt.hist(df.loc[df['music_genre'] == 'Classical', 'acousticness'], bins, alpha=0.5, label='Classical')
        plt.hist(df.loc[df['music_genre'] == 'Rock', 'acousticness'], bins, alpha=0.5, label='Rock')
        plt.legend(loc='upper right')
        plt.xlabel('acousticness', fontsize=16)
        plt.ylabel('Количество наблюдений', fontsize=16)
        plt.title('Уровень аккустичности для классической музыки и рока', fontsize=16)
        st.pyplot(fig)

        def grafik(x):
            x1 = list(df[df['music_genre'] == 'Country'][x])
            x2 = list(df[df['music_genre'] == 'Rock'][x])
            x3 = list(df[df['music_genre'] == 'Alternative'][x])
            x4 = list(df[df['music_genre'] == 'Hip-Hop'][x])
            x5 = list(df[df['music_genre'] == 'Blues'][x])
            x6 = list(df[df['music_genre'] == 'Jazz'][x])
            x7 = list(df[df['music_genre'] == 'Electronic'][x])
            x8 = list(df[df['music_genre'] == 'Anime'][x])
            x9 = list(df[df['music_genre'] == 'Rap'][x])
            x10 = list(df[df['music_genre'] == 'Classical'][x])

            colors = ['#E69F00', '#56B4E9', '#F0E442', '#009E73', '#D55E00', '#00FFFF', '#DC143C', '#7FFF00', '#5F9EA0',
                      '#DEB887']
            names = ['Country', 'Rock', 'Alternative',
                     'Hip-Hop', 'Blues', 'Jazz', 'Electronic', 'Anime', 'Rap', 'Classical']

            plt.hist([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10], bins=int(180 / 15),
                     color=colors, label=names)

        st.write("### Зависимость жанра от энергичности")
        fig = plt.figure(figsize=(16, 5))
        grafik('energy')
        plt.legend()
        plt.xlabel('Энергичность')
        plt.ylabel('Количество треков')
        st.pyplot(fig)

        st.write("### Зависимость жанра от аккустичности")
        fig = plt.figure(figsize=(16, 5))
        grafik('acousticness')
        plt.legend()
        plt.xlabel('Аккустичность')
        plt.ylabel('Количество треков')
        st.pyplot(fig)

        st.write("### Зависимость жанра от громкости")
        fig = plt.figure(figsize=(16, 5))
        grafik('loudness')
        plt.legend()
        plt.xlabel('Громкость')
        plt.ylabel('Количество треков')
        st.pyplot(fig)


        st.write("### Зависимость жанра от продолжительности")
        fig = plt.figure(figsize=(16, 5))
        grafik('duration_ms')
        plt.legend()
        plt.xlabel('Продолжительность')
        plt.ylabel('Количество треков')
        st.pyplot(fig)

        st.write('### Количество значений в поле "key" для каждого значения в поле "music_genre"')
        mode_counts = df.groupby('music_genre')['key'].value_counts()
        mode_counts = mode_counts.unstack()
        # Построение графика
        fig, ax = plt.subplots(figsize=(12, 6))
        mode_counts.plot(kind='bar', stacked=True, ax=ax)
        # Настройка графика
        plt.xlabel('Music Genre')
        plt.ylabel('Count')
        plt.legend(title='Mode', loc='upper right')
        st.pyplot(fig)

    else:
        st.write("Файл train_data.csv не найден в папке data.")
