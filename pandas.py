import pandas as pd

# Генерация данных
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# Преобразование в one hot
one_hot = pd.get_dummies(data['whoAmI'])

# Объединение и вывод результата
result = pd.concat([data, one_hot], axis=1)
result.head()
