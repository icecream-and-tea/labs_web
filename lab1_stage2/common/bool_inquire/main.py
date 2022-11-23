import json

from user_input_process import input_processor
from search import Searcher

req_type = None


def search():
    global req_type
    # 电影和书籍分别检索
    searcher = Searcher(req_type)
    require = input_processor(req_type)
    return searcher.run(require)


def movies_show(id_list):
    info_file = '../../../lab1_stage1/movie_spider/doc/json/info_movie.json'
    with open(info_file, 'r', encoding='utf-8') as f:
        info = json.load(f)
    info = [movie for movie in info if movie['Id'] in id_list]  # 将信息缩减为所需信息
    # print(info)
    print('相关电影共{}部'.format(len(info)))
    for num, movie in enumerate(info):
        print('-------------------------------------------------------------')
        title = movie['基本信息']['标题']
        direct = movie['基本信息']['导演']
        tags = movie['基本信息']['类型']
        summarys = movie['剧情简介']
        recommond = movie['相关电影']

        print("相关电影{}\n".format(num+1))
        if title:
            print("标题：" + title)
        if direct:
            print("导演：", end='')
            [print(person + ' / ', end='') for person in direct]
            print('')
        if tags:
            print("类型：", end='')
            [print(tag + ' / ', end='') for tag in tags]
            print('')
        if summarys:
            print("简介：")
            spilt = 0
            while spilt != -1:
                spilt = summarys.find('\par')
                if len(summarys[:spilt]) > 0:
                    print('  ' + summarys[:spilt])
                summarys = summarys[spilt+4:]
        if recommond:
            print('其他电影推荐：')
            for item in recommond:
                print("  " + item[0], end='')
        print('\n')

        if (num+1) % 5 == 0:
            opt = input('查看下一页请输入next，退出输入exit\n')
            if opt == 'next':
                continue
            else:
                break


def books_show(id_list):
    info_file = '../../../lab1_stage1/book_spider/doc/json/info_book.json'
    with open(info_file, 'r', encoding='utf-8') as f:
        info = json.load(f)
    info = [book for book in info if book['Id'] in id_list]  # 将信息缩减为所需信息
    print('相关书籍共{}部'.format(len(info)))
    for num, book in enumerate(info):
        print('-------------------------------------------------------------')
        title = book['基本信息']['标题']
        tags = book['基本信息']['类型']
        author = book['基本信息']['作者']
        summarys = book['内容简介']
        recommond = book['书籍推荐']

        print("相关书籍{}\n".format(num + 1))
        if title:
            print("标题：" + title)
        if author:
            print("作者：" + author)
        if tags:
            print("类型：", end='')
            [print(tag + ' / ', end='') for tag in tags]
            print('')
        if summarys:
            print("简介：")
            spilt = 0
            while spilt != -1:
                spilt = summarys.find('\par')
                if len(summarys[:spilt]) > 0:
                    print('  ' + summarys[:spilt])
                summarys = summarys[spilt + 4:]
        if recommond:
            print('其他书籍推荐：')
            for item in recommond:
                print("  " + item[0], end='')
        print('\n')

        if (num + 1) % 5 == 0:
            opt = input('查看下一页请输入next，退出输入exit\n')
            if opt == 'next':
                continue
            else:
                break


# 处理用户输入，查询符合规则电影，以一定形式展现
if __name__ == "__main__":
    print("please input 电影 or 书籍 to search")
    tmp = input(">>>")
    if tmp == "电影":
        req_type = 'movies'
    elif tmp == "书籍":
        req_type = 'books'
    else:
        print("input error")
        exit()

    res = search()

    if req_type == 'movies':
        movies_show(res)
    else:
        books_show(res)


