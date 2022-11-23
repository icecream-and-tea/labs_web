import pandas as pd
from sklearn.model_selection import train_test_split

# 切分数据集: 训练集与测试集合 8:2

movie_score = '../doc/Movie_score.csv'

train_data = pd.DataFrame()
test_data = pd.DataFrame()
raw_data = pd.read_csv(r'lab1_stage3/doc/pro_movie_score.csv')

raw_data_len = len(raw_data)
user_id_list = []

# 将所有的user_id全放到一个列表中
for i in range(raw_data_len):
    if user_id_list.count(raw_data.iloc[i, 0]) == 0:
        user_id_list.append(raw_data.iloc[i, 0])

# 根据user_id, 分别将每个user_id分为5:5的训练集与测试集,
# 最后加入到总的train_data与test_data中
for i in range(len(user_id_list)):
    tmp_user_data = raw_data.loc[raw_data['user'] == user_id_list[i]]
    train_set, test_set = train_test_split(
        tmp_user_data, test_size=0.2, random_state=42)
    train_data = pd.concat([train_data, train_set])
    test_data = pd.concat([test_data, test_set])

train_data.to_csv(r'lab1_stage3/doc/train_data.csv', index=False)
test_data.to_csv(r'lab1_stage3/doc/test_data.csv', index=False)
