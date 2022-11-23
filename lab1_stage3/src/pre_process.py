import pandas as pd

# 预处理 Movie_score.csv 部分
# 意义: 删除很坏的数据, 例如某用户的评价绝大多数分数相同
# 暂定占比为95%, 后续可能根据基于用户的近邻数 k(暂取20)以及预测结果作相应修改

raw_data = pd.read_csv(r"lab1_stage3\doc\Movie_score.csv", encoding='utf-8')
raw_data.sort_values(by=['user', 'item'], inplace=True)
raw_data = raw_data.drop(raw_data[raw_data.rating == 0].index)
pro_data = pd.DataFrame()

user_id_list = []
for i in range(len(raw_data)):
    if user_id_list.count(raw_data.iloc[i, 0]) == 0:
        user_id_list.append(raw_data.iloc[i, 0])

for user in range(len(user_id_list)):
    now_user_score = raw_data.loc[raw_data.user == user_id_list[user]]
    total_len = len(now_user_score)
    flag = 0  # 判断该用户是否为坏点
    for i in range(1, 6):
        # 该用户评分为 i 的电影个数
        tmp_df = now_user_score.loc[now_user_score.rating == i]
        i_len = len(tmp_df)
        if i_len/total_len > 0.95:
            flag = 1

    if flag == 0:  # 是一个好的数据
        pro_data = pd.concat([pro_data, now_user_score])

pro_data.to_csv(r'lab1_stage3\doc\pro_movie_score.csv', index=False)
