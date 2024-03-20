import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import pandas as pd

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from catboost import CatBoostClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from catboost import CatBoostRegressor

from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from category_encoders.ordinal import OrdinalEncoder
from category_encoders.one_hot import OneHotEncoder
from category_encoders.target_encoder import TargetEncoder
from category_encoders.leave_one_out import LeaveOneOutEncoder

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from pickle import dump, load
def model_page():

    # Загрузка файла test_data.csv из папки data
    file_path = 'data/test_data.csv'
    if os.path.exists(file_path):
        df_test = pd.read_csv(file_path)
        test_df = pd.read_csv(file_path)

        st.write("### Пример тестовых данных:")
        st.write(df_test)

        df_test = df_test.drop(['instance_id', 'obtained_date'], axis=1)
        df_test['track_name'] = df_test['track_name'].apply(lambda x: len(str(x)))
        df_test.loc[(df_test['mode'] == 'Major'), 'mode'] = 1
        df_test.loc[(df_test['mode'] == 'Minor'), 'mode'] = -1
        df_test['mode'] = df_test['mode'].fillna(0)
        df_test['tempo'] = df_test['tempo'].fillna(120.011)
        df_test['key'] = df_test['key'].fillna('Pusto')

        with open('data/final_model_test.pkl', 'rb') as file:
            model = pickle.load(file)

        predictions = model.predict(df_test)

        predicted_genres = [genre[0] for genre in predictions]

        # Присвоение предсказанных жанров столбцу 'predicted_genre'
        test_df['predicted_genre'] = predicted_genres
        st.write("### Пример тестовых данных с предсказанием:")
        st.write(test_df)


    else:
        st.write("Файл train_data.csv не найден в папке data.")


