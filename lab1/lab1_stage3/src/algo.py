import lenskit
import os
import numpy as np
import pandas as pd
from lenskit import batch
from lenskit import crossfold as xf
from lenskit import topn, util
from lenskit.algorithms import Recommender, als
from lenskit.algorithms import item_knn, user_knn, svd
from sklearn.metrics import ndcg_score


def eval(aname, algo, train, test):
    fittable = util.clone(algo)  # 复制这个算法
    fittable = Recommender.adapt(fittable)
    fittable.fit(train)
    # now we run the recommender
    recs = batch.predict(fittable, test)
    recs['Algorithm'] = aname
    return recs


def get_ndcg(df):

    df = df.sort_values(
        by=['user', 'prediction'], ascending=False)
    user_id_list = []
    ndcg_dic = {}

    # 将所有的user_id全放到一个列表中, 用来查找df中的用户
    for i in range(len(df)):
        if user_id_list.count(df.iloc[i, 0]) == 0:
            user_id_list.append(df.iloc[i, 0])
    for user in range(len(user_id_list)):
        tmp_user_data = df.loc[df['user'] == user_id_list[user]]
        pred = list(tmp_user_data['prediction'])
        true = list(tmp_user_data['rating'])
        # 将每个用户的 ndcg 分数存入 ndcg_dic 中
        # 若只有单个评分, 则无需考虑使用 NDCG 对其进行评估
        if len(pred) > 1: 
            ndcg_dic[user_id_list[user]] = ndcg_score([pred], [true])

    ndcg_df = pd.DataFrame.from_dict(
        ndcg_dic, orient='index', columns=['ndcg'])
    ndcg_df = ndcg_df.reset_index().rename({'index': 'user'}, axis='columns')

    return ndcg_df


if __name__ == '__main__':
    ratings = pd.read_csv(
        r"lab1_stage3\doc\pro_movie_score.csv", encoding='utf-8')
    train = pd.read_csv(r"lab1_stage3\doc\train_data.csv", encoding='utf-8')
    test = pd.read_csv(r"lab1_stage3\doc\test_data.csv", encoding='utf-8')

    ratings = ratings.iloc[:, 0:3]
    train = train.iloc[:, 0:3]
    test = test.iloc[:, 0:3]

    ratings.sort_values(by=['user', 'item'], inplace=True)

    algo_list = ['als', 'svd', 'uu_20']

    # 针对 ItemItem, 尝试比较不同的近邻值对结果的影响
    # 以 k = 20 为基准来比较
    for i in range(5):
        k = 20*(1+i)
        algo = item_knn.ItemItem(k)
        n_path = 'lab1_stage3\doc\ii_{}'.format(str(k))
        if os.path.isdir(n_path) == False:
            os.mkdir(n_path)

        pred_data = []
        pred_data.append(eval('II_{}'.format(str(k)), algo, train, test))

        # 得到预测的数据
        pred_data = pd.concat(pred_data, ignore_index=True)
        pred_data = pred_data.sort_values(
            by=['user', 'prediction'], ascending=False)
        pred_data.to_csv(
            r'{}\pred_data.csv'.format(n_path), index=False)

        results = get_ndcg(pred_data)

        results.to_csv(
            r'{}\ndcg_results.csv'.format(n_path), index=False)

    for i in algo_list:

        n_path = 'lab1_stage3\doc\{}'.format(i)
        if os.path.isdir(n_path) == False:
            os.mkdir(n_path)

        if i == 'als':
            algo = als.BiasedMF(50)
        elif i == 'svd':
            algo = svd.BiasedSVD(50)  # feature = 50
        elif i == 'uu_20':
            algo = user_knn.UserUser(20)

        pred_data = []
        pred_data.append(eval(i.upper(), algo, train, test))

        # 得到预测的数据
        pred_data = pd.concat(pred_data, ignore_index=True)
        pred_data = pred_data.sort_values(
            by=['user', 'prediction'], ascending=False)
        pred_data.to_csv(
            r'{}\pred_data.csv'.format(n_path), index=False)

        results = get_ndcg(pred_data)

        results.to_csv(
            r'{}\ndcg_results.csv'.format(n_path), index=False)
