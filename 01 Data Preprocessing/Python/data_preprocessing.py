# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Подготовка данных. Основные мероприятия

# 1. Отсутствующие данные

# 2. Кодирование категориальных признаков. One Hot Encoding

# 3. Разделение набора на обучаемую и тестовую выборку

# 4. Нормализация данных
