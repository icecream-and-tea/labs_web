import json


# 基本数据结构
# dic = {
#     key1: [n1, ...],
#     key2: [n2, ...],
#     ...
# }

# 基本思路-参见./posting_list_movies.py

file_input_info = 'E:/Study/4.5_web/labs_web/lab1_spiders/book_spider/doc/json/info_book.json'
file_input_words = 'E:/Study/4.5_web/labs_web/lab2_search_engine/doc/words_books.json'
file_input_book_list = 'E:/Study/4.5_web/labs_web/lab1_spiders/book_spider/doc/Book_id.txt'
file_output_book_list = 'E:/Study/4.5_web/labs_web/lab2_search_engine/doc/posting_list_books.json'
file_output_new_book_id = 'E:/Study/4.5_web/labs_web/lab2_search_engine/doc/new_book_id.txt'

with open(file_input_info, encoding='utf-8') as f_input_info:
    input_info = json.load(f_input_info)
with open(file_input_words, encoding='utf-8') as f_input_words:
    input_words = json.load(f_input_words)

# 不需要了
with open(file_input_book_list, encoding='utf-8') as f_input_list:
    input_list = f_input_list.readlines()
# for n in range(0, len(input_list)):
#     input_list[n].replace('\n', '')

# 除去坏点，重新建立id表（987个元素）
id_num_list = []
N = 1000
for book_id in range(0, len(input_info)):
    id = input_info[book_id]['Id']
    id_num_list.append(id)
with open(file_output_new_book_id, 'w', encoding='utf-8') as f_output_list:
    for lien in id_num_list:
        f_output_list.write(lien + '\n')

# print(len(input_words))
# print(len(input_info))

word_dic = {}
for book_id in range(0, len(input_words)):
    title = input_words[book_id][0]
    id = input_info[book_id]['Id'] 
    num = id_num_list.index(id)     # 在id_num_list中找到对应的数字（0~987)
    for key in range(0, len(input_words[book_id])):   # 如果需要将电影名加入key，则从0开始而非1
        if input_words[book_id][key] not in word_dic.keys():  # 第一次加入关键词，初始化value链表并加入id
            tmp_list = []
            tmp_list.append(num)
            word_dic[input_words[book_id][key]] = tmp_list         
        else:       # 否则直接加入后面的链表 
            if num not in word_dic[input_words[book_id][key]]:   # 不知道为什么book的关键词对应num有重复冗余，加上这句话
                word_dic[input_words[book_id][key]].append(num)    

for key_n in word_dic.keys(): # 排列n值，从小到大
    word_dic[key_n].sort()

# print(word_dic)

with open(file_output_book_list, 'w', encoding='utf-8') as f_output:
    json.dump(word_dic, f_output, ensure_ascii=False, indent=4)