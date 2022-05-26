import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression

heart = pd.read_csv(r'C:\temp\projects_data\heart_2020_cleaned.csv')


def change_to_binary(x):
    if x == 'Yes':
        return 1
    elif x == 'No':
        return 0
    else:
        return np.NaN


def is_yes_no(x):
    if x == 'Yes' or x == 'No':
        return True
    else:
        return False


columns_to_change = [column for column in heart.columns if all(map(lambda x: is_yes_no(x), heart[column]))]

for column in columns_to_change:
    heart[column] = heart[column].apply(lambda x: change_to_binary(x))


heart = pd.get_dummies(heart, prefix_sep='_')
heart.head()

X = heart.drop(['HeartDisease'], axis=1)
y = heart['HeartDisease']


sc = StandardScaler()
X = sc.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

random_forest = RandomForestRegressor(n_jobs=4)
random_forest.fit(X, y)

logistic_regression = LogisticRegression(n_jobs=4)
logistic_regression.fit(X, y)


def predict_input_heart(input_dict):

    input_df = pd.DataFrame(data=input_dict, index=[400000])

    temp_df = pd.read_csv(r'C:\temp\projects_data\heart_2020_cleaned.csv')
    temp_df = temp_df.append(input_df, ignore_index=False)

    for column in columns_to_change:
        temp_df[column] = temp_df[column].apply(lambda x: change_to_binary(x))

    temp_df = pd.get_dummies(temp_df, prefix_sep='_')
    input_df = temp_df.tail(1)

    X_input = input_df.drop(['HeartDisease'], axis=1)
    X_input = sc.transform(X_input)

    prediction_rf = random_forest.predict(X_input)[0]
    prediction_lr = logistic_regression.predict(X_input)[0]

    prediction = [prediction_rf, prediction_lr]

    return prediction




