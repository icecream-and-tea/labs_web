import json
# 分词


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
        wordList.append('.')  # 作为不同近义词的分割符
        for word in words:
            wordList.append(word)
    return wordList


def merge_syn(inputPath, outputPath, wordList):
    # 合并每部电影的同近义词
    newData = []
    with open(inputPath, 'r', encoding='utf8') as f:
        origData = json.load(f)

    for num, item in enumerate(origData):
        synWord = 0
        newItem = []
        for word in item:
            if word in wordList:
                index = wordList.index(word)
                while wordList[index-1] != '.':
                    index = index - 1
                newItem.append(wordList[index])
                synWord += 1
            else:
                newItem.append(word)
        newData.append(newItem)
        print(num)

    with open(outputPath, 'w', encoding='utf-8') as f:
        json.dump(newData, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    txtPath = '../doc/chinese_dictionary/dict_synonym.txt'
    movieInput = '../doc/words_movies.json'
    bookInput = '../doc/words_books.json'
    movieOutput = '../doc/nosyn_words_movies.json'
    bookOutput = '../doc/nosyn_words_books.json'

    wordList = read_txt(txtPath)
    # merge_syn(movieInput, movieOutput, wordList)
    merge_syn(bookInput, bookOutput, wordList)
