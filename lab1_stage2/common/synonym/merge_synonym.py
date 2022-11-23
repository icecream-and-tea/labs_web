import json


class Merger(object):
    def __init__(self, synList):
        self.synList = synList

    # 合并单个列表的同近义词
    def merge_syn(self, words):
        res = []
        for word in words:
            flag = False
            for item in self.synList:   # 若有同近义词，则转化成“标准词语”，加入res
                if word in item:
                    if item[0] not in res:  # 防止重复添加
                        res.append(item[0])
                    flag = True
                    break
            if not flag and word not in res:    # 若没有同近义词且不在res里，则加入res
                res.append(word)
        return res  # 返回

    # 对文件进行合并
    def run(self, inputPath, outputPath):
        res = []
        with open(inputPath, 'r', encoding='utf8') as f:
            data = json.load(f)

        for words in data:
            res.append(self.merge_syn(words))
            print(len(res))

        with open(outputPath, 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    movieInput = '../movies/doc/words_movies.json'
    bookInput = '../books/doc/words_books.json'
    movieOutput = '../movies/doc/no_syn_words_movies.json'
    bookOutput = '../books/doc/no_syn_words_books.json'

    synListPath_movies = '../movies/doc/syno_dict_movies.json'
    with open(synListPath_movies, 'r', encoding='utf8') as f:
        synList = json.load(f)
    merger = Merger(synList)
    merger.run(movieInput, movieOutput)

    synListPath_books = '../books/doc/syno_dict_books.json'
    with open(synListPath_books, 'r', encoding='utf8') as f:
        synList = json.load(f)
    merger = Merger(synList)
    merger.run(bookInput, bookOutput)

