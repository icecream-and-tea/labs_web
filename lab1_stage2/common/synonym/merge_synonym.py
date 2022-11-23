import json


class Merger(object):
    def __init__(self, synList):
        self.synList = synList

    # 合并单个列表的同近义词
    def merge_syn(self, words):
        res = []
        for word in words:
            flag = False
            for item in self.synList:
                if word in item:
                    res.append(item[0])
                    flag = True
                    break
            if not flag and word not in res:
                res.append(word)
        return res

    # 对文件进行合并
    def run(self, inputPath, outputPath):
        res = []
        with open(inputPath, 'r', encoding='utf8') as f:
            data = json.load(f)

        for words in data:
            res.append(self.merge_syn(words))

        with open(outputPath, 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=1)


# if __name__ == "__main__":
#     # 框架已重构，需改路径
#     movieInput = '../doc/words_movies.json'
#     bookInput = '../doc/words_books.json'
#     movieOutput = '../doc/nosyn_words_movies.json'
#     bookOutput = '../doc/nosyn_words_books.json'
#
#     synListPath = '../doc/new_syno_list.json'
#     with open(synListPath, 'r', encoding='utf8') as f:
#         synList = json.load(f)
#     merger = Merger(synList)
#     merger.run(movieInput, movieOutput)

