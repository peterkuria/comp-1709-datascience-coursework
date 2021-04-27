# Bar chart group sorted - Proportion
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('https://tinyurl.com/ChrisCoNorth/001178008/DailyCustomers.csv', index_col=0)

# sort the data according to the sum of each column
data = data.reindex(data.sum().sort_values(ascending=False).index, axis=1)

selected = []
columns = data.columns
data['Small_Stores'] = [0] * len(data.index)
for name in columns:
    total_visits = data[name].sum()
    if total_visits > 119000:
        selected.append(name)
    else:
        data['Small_Stores'] += data[name]
selected.append('Small_Stores')
print(data[selected].head())

plt.figure(figsize=(8, 8))
x_pos = np.arange(len(selected))
plt.bar(x_pos, data[selected].sum(), align='center')
plt.xticks(x_pos, selected)
plt.xlabel('Stores', fontsize=18)
plt.ylabel('Customers visits', fontsize=18)
plt.title('Bar chart Total Store Visits', fontsize=20)
plt.show()
