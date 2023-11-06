import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


if __name__ == '__main__':
    with open('percent_helpful_model.pickle', 'rb') as f:
        model = pickle.load(f)

    df = pd.read_csv('/home/sumedhakoranga/Downloads/archive (1)/wikihow.csv')

    print('Spliting data')
    df_full_train, df_test = train_test_split(
        df, test_size=0.2, random_state=42)

    numerical = df.columns[:-1]

    regression_target = ['percent_helpful']

    X = df_test[numerical]
    y = df_test[regression_target]['percent_helpful']

    score = mean_squared_error(model.predict(X), y, squared=False)

    print('Test set RMSE =', score)