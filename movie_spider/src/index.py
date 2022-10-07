import json
from time import sleep
from spider import Spider
from html_parser import Parser
from bs4 import BeautifulSoup


# 第二次爬取电影列表：官方小站， 动画片
# movieList = ['3541415', '3742360', '1291543', '4271894', '3412830', '4226741', '3546019', '1437342', '2326676',
#              '3560787', '4151110', '4896263', '1300395', '1792928', '1310174', '4822848', '1295250', '4190211',
#              '4057312', '1305724', '1408100', '1449381', '1401524', '3792816', '1470591', '3041294', '4059245',
#              '1434184', '1483507', '1431685', '1761854', '1295428', '4888039', '1431946']


def main_handler(event, context):
    event = event['queryString']
    print(event)

    # 打开id集合文件，将id存放于列表中
    infile = open('../doc/Movie_id.txt', 'r', encoding='utf8')
    movieList = infile.read().split()

    # 生成爬虫与解析器
    spider = Spider()

    # 要做保存断点工作
    res = list()
    errorList = list()
    for num, movieId in enumerate(movieList):
        print('第%d部影片' % (num+1))
        try:
            # 爬取并返回html
            html = spider.run(movieId)
            if html == -1:
                print('第%d影片爬取出现错误，且为爬取错误' % num)
                errorList.append(movieId)
                break
            elif html == 0:
                continue  # 空页面
            # 使用bs4库对html进行解析
            soup = BeautifulSoup(html, 'html.parser')
            parser = Parser(soup)

            # 先将解析字典存入列表，最后进行json格式转换
            res.append(parser.run())

        except Exception as e:
            print(e)
            print('第%d影片爬取出现错误' % (num + 1))
            errorList.append(movieId)

        if num % 200 == 0 and num != 0:
            print('开始必要休眠')
            sleep(300)

    print('本次爬取发生错误的影片编号为')
    print(errorList)

    # 指定存放位置
    outfile = open('../doc/result.json', 'w', encoding='utf-8')
    json.dump(res, outfile, ensure_ascii=False, indent=1)


main_handler({'queryString': ''}, None)

