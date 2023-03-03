# _*_ coding:utf-8 _*_
import pkuseg
import json

seg = pkuseg.pkuseg('D:\python\Lib\site-packages\pkuseg\default_v2')  # 开启词性标注功能
filename_input = '../../../lab1_stage1/book_spider/doc/json/info_book.json'
filename_output = '../doc/words_books.json'
filename_stopwords = '../doc/stop_words_books.json'
words_set = []

with open(filename_input, encoding='UTF-8') as f_info:  # 加上encoding参数，否则会解码报错
    info = json.load(f_info)
with open(filename_stopwords, encoding='UTF-8') as f_stopwords:
    stop_words = json.load(f_stopwords)

for book in info:
    keywords = [book["基本信息"]["标题"]]  # 标题
    book_type = book["基本信息"]["类型"]  # 类型
    if book["基本信息"].get("类型"):
        keywords.extend(book_type)
    # keywords.extend(book_type)

    if book["基本信息"].get("作者"):
        writer = book["基本信息"]["作者"].split("/")
        writers = []
        for name in writer:
            writers.append(name.split("]")[-1])
        keywords.extend(writers)
#   else:
#       print(f"{book_title} has no writer!")
    if book["基本信息"].get("出版社"):
        keywords.append(book["基本信息"]["出版社"])

    if book.get("内容简介"):
        content = seg.cut(book["内容简介"].replace("\\par", ""))  # 内容简介
        keywords.extend(content)

    origin_name = book["基本信息"].get("原作名")  # 如果原作名存在，则加入
    if origin_name:
        keywords.append(origin_name)

    translator = book["基本信息"].get("译者")  # 如果有译者，则加入
    if translator:
        keywords.extend(translator.split("/"))

    subtitle = book["基本信息"].get("副标题")  # 如果有副标题，则加入
    if subtitle:
        keywords.append(subtitle)

    series = book["基本信息"].get("丛书")  # 如果有丛书，则加入
    if series:
        keywords.append(series)

    key_words_temp = keywords[:]
    for member in key_words_temp:   # 去除停用词
        if member in stop_words:
            keywords.remove(member)
    merged_keywords = []
    for word in keywords:   # 合并相同词
        if word not in merged_keywords:
            merged_keywords.append(word)

    print(merged_keywords)
    words_set.append(merged_keywords)

print(len(words_set))
with open(filename_output, 'w', encoding="UTF-8") as f_output:  # 以写入模式打开文件
    json.dump(words_set, f_output, ensure_ascii=False, indent=4)
