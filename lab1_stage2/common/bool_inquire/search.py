import json
from compress import Decompressor
from user_input_process import input_processor
# 输入：bool查询最小项格式，索引表
# 输出：符合查询条件的电影序号


# 处理与操作 与 或 非
class Searcher(object):

    def __init__(self, req_type):
        self.req_type = req_type
        post_list = "../../{}/doc/posting_list_{}.json".format(req_type, req_type)
        decompressor = Decompressor(post_list)
        self.post_list = decompressor.interval2num()
        # with open(post_list, 'r', encoding='utf-8') as f:
        #     self.post_list = json.load(f)

    def inquire_and(self, word1_list, word2_list):
        res = []  # 两个列表的并集
        for movie in word1_list:
            if movie in word2_list:
                res.append(movie)
        return res

    def inquire_or(self, word1_list, word2_list):
        res = []  # 两个列表的或集
        for movie in word1_list:
            res.append(movie)
        for movie in word2_list:
            if movie not in res:
                res.append(movie)
        return res

    def inquire_not(self, word1_list, word2_list):
        res = []  # 两个列表的减集，第二个列表是not集合
        for movie in word1_list:
            if movie not in word2_list:
                res.append(movie)
        return res

    def run(self, req_list):
        # req_list: [[A,B,C],[D,E],...]
        res = []
        for req in req_list:  # 遍历每一个和项
            # 注意NOT操作不能简单理解为某一词项的补集，因为补集可能会很大，必须是两个倒排表的减集。
            and_list = []
            for word in req:
                if word[:3] == 'NOT':
                    if word[4:0] in self.post_list:
                        and_list.append([self.post_list[word[4:]], 1])
                else:
                    if word in self.post_list:
                        and_list.append([self.post_list[word], 0])
                    else:
                        continue  # 应为有了空集，AND结果为空

            while len(and_list) >= 2:
                and_list.sort(key=lambda i: len(i[0]), reverse=False)
                # 进行NOT判定与操作
                sum = and_list[0][1] + and_list[1][1]
                if sum == 0:  # 两个均不为NOT
                    tmp = [self.inquire_and(and_list[0][0], and_list[1][0]), 0]  # 每次选择最小的两个进行查询
                elif sum == 1:
                    if and_list[0][1] == 1:  # 第一个为NOT
                        tmp = [self.inquire_not(and_list[1][0], and_list[0][0]), 0]
                    else:  # 第二个为NOT
                        tmp = [self.inquire_not(and_list[0][0], and_list[1][0]), 0]
                else:  # 两个均为NOT
                    tmp = [self.inquire_or(and_list[0][0], and_list[1][0]), 1]
                del and_list[0:2]
                and_list.append(tmp)
            if and_list:
                res.append(and_list[0][0])  # AND和NOT操作的结果

        while len(res) >= 2:  # 均为NOT的情况没有考虑
            res.sort(key=lambda i: len(i), reverse=False)
            tmp = self.inquire_or(res[0], res[1])
            del res[0:2]
            res.append(tmp)
        if res:
            res = res[0]
            res.sort()
        else:
            print("无结果\n")

        # 将序号转换为id
        id_file = "../../{}/doc/new_{}_id.txt".format(self.req_type, self.req_type)
        with open(id_file, 'r', encoding='utf-8') as f:
            id_list = f.read()
        id_list = id_list.split()
        for i in range(len(res)):
            res[i] = id_list[res[i]]

        return res


# if __name__ == "__main__":
#     searcher = Searcher("books")
#     print(searcher.run([['文学']]))
