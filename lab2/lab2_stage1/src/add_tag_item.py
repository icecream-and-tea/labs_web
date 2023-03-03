# 将所有的不同tag统计出来，用拼音或者哈希映射对其编码，人为构建三元组，添加到图中
import json
from pypinyin import lazy_pinyin


def create_triplet(id_dict, pinyin_dict):
    # 将这些拼音变为三元组，加入到子图中
    # 关系统一为film.film.type
    # 建立两个hash表用来快速构建三元组
    input_file_path = "info_movie.json"
    with open(input_file_path, 'r', encoding='utf-8') as f:
        movie_info_list = json.load(f)
    f.close()

    rela_list = []
    for movie_info in movie_info_list:
        movie_id = movie_info["Id"]
        if movie_id not in id_dict:
            continue
        db_id = id_dict[movie_id]
        tags = movie_info['基本信息']['类型']
        for tag in tags:
            pinyin = pinyin_dict[tag]
            rela_list.append([db_id, pinyin])

    # 构建三元组，以文件形式输出
    output_file = open('../doc/new_triplet.txt', 'w', encoding='utf-8')
    for rela in rela_list:
        triplet = rela[0] + ' ' + 'film.film.type' + ' type.' + rela[1] + '\n'
        output_file.write(triplet)
    output_file.close()


def tag2pinyin():
    input_file_path = "info_movie.json"
    with open(input_file_path, 'r', encoding='utf-8') as f:
        movie_info_list = json.load(f)
    f.close()

    tag_list = []
    for movie_info in movie_info_list:
        tags = movie_info['基本信息']['类型']
        for tag in tags:
            if tag not in tag_list:
                tag_list.append(tag)

    # 转换为拼音存储
    pinyin_dict = {}
    pinyin_list = []
    for tag in tag_list:
        word_pinyin_list = lazy_pinyin(tag)
        res = ''
        for pinyin in word_pinyin_list:
            res += pinyin
        pinyin_list.append(res)
        pinyin_dict[tag] = res

    output_file_path = "../doc/tag2pinyin.txt"
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for i in range(len(tag_list)):
            f.write(tag_list[i] + ' ' + pinyin_list[i] + '\n')
    f.close()

    return pinyin_dict


if __name__ == "__main__":
    # 得到映射表1
    with open('../doc/douban2fb.txt', 'r') as id_file:
        datas = id_file.read().splitlines()
    id_dict = {}
    for data in datas:
        tmp = data.split()
        id_dict[tmp[0]] = tmp[1]

    # 得到映射表2
    pinyin_dict = tag2pinyin()

    # 创建三元组
    create_triplet(id_dict, pinyin_dict)




