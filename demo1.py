'''
绘制24h和48h误差柱状图
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
# from matplotlib import font_manager
# for font in font_manager.fontManager.ttflist:
#     # 查看字体名以及对应的字体文件名
#     print(font.name, '-', font.fname)

plt.rcParams["font.sans-serif"] = "Times New Roman"
data = pd.read_excel("data.xlsx", index_col=0)
print(data)
x = data.index.to_list()
x_label = np.arange(len(x))
print(x)
col_names = data.columns.to_list()
col1_names = []
col2_names = []
for name in col_names:
    if "24h" in name:
        col1_names.append(name)
    elif "48h" in name:
        col2_names.append(name)
    else:
        raise ValueError

y1 = []
y1_err = []
y2 = []
y2_err = []

for name in x:
    col1_data = data.loc[name][col1_names].to_list()
    col1_data = list(filter(lambda x: not math.isnan(x), col1_data))
    col2_data = data.loc[name][col2_names].to_list()
    col2_data = list(filter(lambda x: not math.isnan(x), col2_data))
    y1.append(np.average(col1_data))
    y1_err.append(np.std(col1_data))
    y2.append(np.average(col2_data))
    y2_err.append(np.std(col2_data))

print(y1)
print(y2)


width = 0.3
err_attr = {"elinewidth": 2, "ecolor": "black", "capsize": 6}
fig, ax = plt.subplots(figsize=(12, 9), dpi=80)
bar1 = ax.bar(x_label-width/2, y1, yerr=y1_err, error_kw=err_attr,
              width=width, color="#c0c0c0", edgecolor='black', label='24h')
bar2 = ax.bar(x_label+width/2, y2, yerr=y2_err, error_kw=err_attr,
              width=width, color="#cddbc6", edgecolor='black', label='48h')
plt.xticks(x_label, labels=x, size=24, weight='bold')
plt.yticks(size=24, weight='bold')

plt.ylabel("NMN (g/L)", fontdict={"size": 24}, weight='bold')
plt.legend(prop={"size": 24}, frameon=False)
plt.show()
