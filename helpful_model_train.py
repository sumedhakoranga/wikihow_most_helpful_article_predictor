import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

import pickle

import warnings
warnings.filterwarnings("ignore")


def create_new_pipeline(params):
    numerical_transformer = SimpleImputer(strategy='mean')

    preprocessor = ColumnTransformer(
        transformers=[
            ('numerical', numerical_transformer, numerical),
        ])

    scaler = StandardScaler()

    forest = RandomForestRegressor(
        n_jobs=-1,
        random_state=42,
        **params
    )

    pipeline = Pipeline(
        steps=[
            ('preprocessing', preprocessor),
            ('scaling', scaler),
            ('model', forest)
        ]
    )

    return pipeline


if __name__ == '__main__':
    print('Importing data')
    # df = pd.read_csv('wikihow.csv')
    df = pd.read_csv('/home/sumedhakoranga/Downloads/archive (1)/wikihow.csv')

    print('Spliting data')
    df_full_train, df_test = train_test_split(
        df, test_size=0.2, random_state=42)

    numerical = df.columns[:-1]

    regression_target = ['percent_helpful']

    X = df_full_train[numerical]
    y = df_full_train[regression_target]['percent_helpful']

    params = {'n_estimators': 6,
              'min_samples_split': 6, 'max_features': 'log2'}

    print('Creating pipeline')
    pipeline = create_new_pipeline(params)

    print('Training model')
    pipeline.fit(X, y)

    print('Saving model')
    with open('percent_helpful_model.pickle', 'wb') as f:
        pickle.dump((pipeline), f)
