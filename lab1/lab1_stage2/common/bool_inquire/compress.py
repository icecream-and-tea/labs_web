import json
import os
import filecmp
import pickle

# 输入：倒排索引表
# 输出：经过可变字节压缩的倒排表
# 流程：先对倒排表中的序号改为间距，在此基础上进行可变字节编码


class Compressor(object):

    def __init__(self, post_list):
        with open(post_list, 'r', encoding='utf-8') as f:
            self.post_list = json.load(f)

    def num2interval(self):
        post_list = self.post_list
        for key, value in post_list.items():
            for i in range(len(value)-1, 0, -1):
                value[i] -= value[i-1]
        # with open('tmp.json', 'w', encoding='GBK') as f:
        #     json.dump(self.post_list, f, ensure_ascii=False, indent=1)


class Decompressor(object):

    def __init__(self, post_list):
        with open(post_list, 'r', encoding='utf-8') as f:
            self.post_list = json.load(f)

    def interval2num(self):
        post_list = self.post_list
        for key, value in post_list.items():
            for i in range(len(value)-1):
                value[i+1] += value[i]
        return post_list


# if __name__ == "__main__":
#     compressor = Compressor("../movies/doc/posting_list_movies.json")
#     compressor.num2interval()
    # decompressor = Decompressor("tmp.json")
    # decompressor.interval2num()

