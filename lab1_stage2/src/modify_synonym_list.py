import json
# 分词


# 对同近义词表进行改变
def read_txt(inputPath):
    wordList = []
    with open(inputPath, 'r', encoding='utf8') as f:
        origData = f.read()
    origData = origData.splitlines()
    for words in origData:
        words = words.split()
        if len(words) <= 2:
            continue
        words = words[1:]
        wordList.append('*')  # 作为不同近义词的分割符
        for word in words:
            wordList.append(word)
    wordList.append('*')  # 设立哨兵
    return wordList


# input: 离谱的同近义词词表
# output: 以分词中第一次出现的词作为代表元的词表 / 出现最多的词
def modify_syno_list(inputPath, wordList):
    with open(inputPath, 'r', encoding='utf8') as f:
        data = json.load(f)
    freqList = [0]*len(wordList)
    # 对各个词出现的频率进行计数
    for num, item in enumerate(data):
        for word in item:
            if word in wordList:
                index = wordList.index(word)
                freqList[index] = freqList[index] + 1
        print(num)

    # 对每一个词组选择频率最高的作为代表词
    newSynoLists = []
    for i in range(len(wordList)-1):
        if wordList[i] == '*':
            synoList = []
            begin = i+1
            max = i+1
            while wordList[i+1] != '*':
                synoList.append(wordList[i+1])
                if freqList[i+1] > freqList[max]:
                    max = i+1
                i = i+1
            if max != begin:  # 将频率最高的元素放到第一个
                tmp = synoList[0]
                synoList[0] = synoList[max-begin]
                synoList[max-begin] = tmp
            if freqList[max] != 0:  # 这组被用到过才加入
                newSynoLists.append(synoList)

    with open('../doc/new_syno_list', 'w', encoding='utf-8') as f:
        json.dump(newSynoLists, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    txtPath = '../doc/chinese_dictionary/dict_synonym.txt'
    movieInput = '../doc/words_movies.json'
    # bookInput = '../doc/words_books.json'
    # movieOutput = '../doc/nosyn_words_movies.json'
    # bookOutput = '../doc/nosyn_words_books.json'

    wordList = read_txt(txtPath)
    modify_synoList(movieInput, wordList)
    # merge_syn(movieInput, movieOutput, wordList)
    # merge_syn(bookInput, bookOutput, wordList)
