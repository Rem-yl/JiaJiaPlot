'''
绘制误差柱状图
'''
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import math

plt.rcParams["font.sans-serif"] = "Times New Roman"
data = pd.read_excel("data2.xlsx", index_col=0)
print(data)

x = data.index.to_list()
x_label = np.arange(len(x))
print(x)

y = []
y_err = []

for name in x:
    col_data = data.loc[name].to_list()
    col_data = list(filter(lambda x: not math.isnan(x), col_data))
    print(col_data)
    y.append(np.average(col_data))
    y_err.append(np.std(col_data))

width = 0.5
err_attr = {"elinewidth": 2, "ecolor": "black", "capsize": 6}
fig, ax = plt.subplots(figsize=(9, 7), dpi=80)
bar = ax.bar(x_label, y, yerr=y_err, error_kw=err_attr, width=width, color="#c0c0c0", edgecolor='black')
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(1))
plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(0.5))

plt.xticks(x_label, labels=x, size=24, weight='bold')
plt.yticks(size=24, weight='bold')

plt.ylabel("NMN (g/L)", fontdict={"size": 24}, weight='bold')
# plt.legend(prop={"size": 24}, frameon=False)
plt.show()
