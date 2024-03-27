"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, 
которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# Для кодировки категориальных данных можно использовать метод pandas get_dummies
# pd.get_dummies(df['Type 1'])
pd.get_dummies(data)
"""

import random

data = []
one_hot = []

for i in range(0, 20):
    data.append(random.choice(['robot', 'human']))

for i in data:
    if i == 'human':
        one_hot.append(1)
    elif i == 'robot':
        one_hot.append(0)

print("Сгенерированный Data Frame:\n", data)
print("\nOne Hot вид:\n", one_hot)