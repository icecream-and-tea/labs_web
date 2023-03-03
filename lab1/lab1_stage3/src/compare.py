import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# 对比不同算法的ndcg值
# 以 ItemItem(20) 为基准

base = pd.read_csv(
    r"lab1_stage3\doc\ii_20\ndcg_results.csv", encoding='utf-8')

# 获取所有文件夹(算法)名字:
path_doc = "lab1_stage3\doc"
tmp_algo_list = os.listdir(path_doc)
algo_list = []
for dbtype in tmp_algo_list:
    if os.path.isdir(os.path.join(path_doc, dbtype)):
        algo_list.append(dbtype)

# 计算各个ndcg的大小; 计算平均值

rst_list = []
mean_list = []
for i in algo_list:
    rst_path = "lab1_stage3/doc/{}/ndcg_results.csv".format(i)
    algo_rst_df = pd.read_csv(os.path.abspath(rst_path))
    num = 0
    flag = 0
    for k in range(len(algo_rst_df)):
        if algo_rst_df.iloc[k].iat[1] > base.iloc[k].iat[1]:
            num = num + 1
        elif algo_rst_df.iloc[k].iat[1] < base.iloc[k].iat[1]:
            num = num - 1
    rst_list.append(num)

    mean_list.append(np.mean(algo_rst_df['ndcg'].tolist()))
print(mean_list)

rst_list, algo_list = zip(*sorted(zip(rst_list, algo_list)))

print(algo_list, rst_list)

fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(x=algo_list, height=rst_list)
ax.set_title("Compared with ItemItem(20)", fontsize=15)


mean_list, algo_list = zip(*sorted(zip(mean_list, algo_list)))
fig, ax2 = plt.subplots(figsize=(10, 7))
ax2.bar(x=algo_list, height=mean_list)
ax2.set_title("Average NDCG", fontsize=15)
ax2.set_ylim(bottom=0.97, top=1.0)

plt.show()
