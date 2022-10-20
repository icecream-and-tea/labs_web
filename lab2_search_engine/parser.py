# _*_ coding:utf-8 _*_
import pkuseg
import json

seg = pkuseg.pkuseg('D:\python\Lib\site-packages\pkuseg\default_v2')  # 开启词性标注功能
filename_input = 'info_movie_1.json'
filename_output = 'words_test.json'
words_set = []
with open(filename_input, encoding='UTF-8') as f:  # 加上encoding参数，否则会解码报错
    info = json.load(f)

for film_id in range(0, 10):
    plot = seg.cut(info[film_id]["剧情简介"].replace("\\par", ""))  # 进行分词
    titles = info[film_id]["基本信息"]["标题"].split()
    casts = []
    for actor in info[film_id]["演职员"]:
        casts.append(actor[0])
        casts.extend(actor[1].split())
    key_words = titles + info[film_id]["基本信息"]["类型"] + casts + plot
    for member in key_words:
        if member == "（" or member == "）" or member == "，" or member == "。" or member == "饰" or member == "配" or \
                member == "“" or member == "/" or member == "；" or member == "《" or member == "》" \
                or member == "”" or member == "、" or member == '——' or member == '—':
            key_words.remove(member)

    while True:
        if "）" in key_words:
            key_words.remove("）")
        else:
            break

    print(key_words)
    words_set.insert(0, key_words)

with open(filename_output, 'w', encoding="UTF-8") as f:  # 以写入模式打开文件
    json.dump(words_set, f, ensure_ascii=False, indent=4)  # 中文的写入 json.dump需要加上ensure_ascii=False参数。否则默认写入unicode;
    # 若觉得每一行太长可以在最后加上indent=4参数
