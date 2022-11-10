import json
import pickle

# 基本数据结构
# dic = {
#     key1: [n1, ...],
#     key2: [n2, ...],
#     ...
# }

# 基本思路
# 0. 根据爬出来的实际电影数目建立新的movie_id.txt；方便倒排表的索引
# 1. 根据分词结果，通过words_movies.json的每个部分的第一条电影名来找到对应info_movie.json中的ID
# 2. 通过new_movie_id.txt找到ID对应的序号num，存入叔叔
# 3. 结束后，使用sort()将ID对应的num从小到大排序（以便建立跳表？）

file_input_info = 'E:/Study/4.5_web/labs_web/lab1_spiders/movie_spider/doc/json/info_movie.json'
file_input_words = 'E:/Study/4.5_web/labs_web/lab2_search_engine/doc/words_movies.json'
file_input_movie_list = 'E:/Study/4.5_web/labs_web/lab1_spiders/movie_spider/doc/Movie_id.txt'
file_output_movie_list = 'E:/Study/4.5_web/labs_web/lab2_search_engine/doc/posting_list_movies.json'
file_output_new_movie_id = 'E:/Study/4.5_web/labs_web/lab2_search_engine/doc/new_movie_id.txt'

with open(file_input_info, encoding='utf-8') as f_input_info:
    input_info = json.load(f_input_info)
with open(file_input_words, encoding='utf-8') as f_input_words:
    input_words = json.load(f_input_words)
with open(file_input_movie_list, encoding='utf-8') as f_input_list:
    input_list = f_input_list.readlines()
# for n in range(0, len(input_list)):
#     input_list[n].replace('\n', '')

# 除去坏点，重新建立id表（987个元素）
id_num_list = []
N = 1000
for film_id in range(0, len(input_info)):
    id = input_info[film_id]['Id']
    id_num_list.append(id)
with open(file_output_new_movie_id, 'w', encoding='utf-8') as f_output_list:
    for lien in id_num_list:
        f_output_list.write(lien + '\n')

# print(len(input_words))
# print(len(input_info))

word_dic = {}
for film_id in range(0, len(input_words)):
    title = input_words[film_id][0]
    id = input_info[film_id]['Id'] 
    num = id_num_list.index(id)     # 在id_num_list中找到对应的数字（0~986)
    for key in range(0, len(input_words[film_id])):
        if input_words[film_id][key] not in word_dic.keys():  # 第一次加入关键词，初始化value链表并加入id
            tmp_list = []
            tmp_list.append(num)
            word_dic[input_words[film_id][key]] = tmp_list         
        else:
            word_dic[input_words[film_id][key]].append(num)    # 否则直接加入后面的链表

for key_n in word_dic.keys(): # 排列n值，从小到大
    word_dic[key_n].sort()

# print(word_dic)

with open(file_output_movie_list, 'w', encoding='utf-8') as f_output:
    json.dump(word_dic, f_output, ensure_ascii=False, indent=4)