import json
from time import sleep
from spider import Spider
from html_parser import Parser
from bs4 import BeautifulSoup


def main_handler(event, context):
    event = event['queryString']
    print(event)

    # 打开id集合文件，将id存放于列表中
    infile = open('../doc/Book_id.txt', 'r', encoding='utf8')
    bookList = infile.read().split()

    # 生成爬虫与解析器
    spider = Spider()

    # 要做保存断点工作
    res = list()
    errorList = list()
    for num, bookId in enumerate(bookList):
        print('第%d本书籍' % (num+1))
        try:
            # 爬取并返回html
            html = spider.run(bookId)
            if html == -1:
                print('第%d本书籍爬取出现错误，且为爬取错误' % num)
                errorList.append(bookId)
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
            print('第%d本书籍爬取出现错误' % (num + 1))
            errorList.append(bookId)

        if num == 15:
            break
        if num % 200 == 0 and num != 0:
            print('开始必要休眠')
            sleep(300)

    print('本次爬取发生错误的书籍编号为')
    print(errorList)

    # 指定存放位置
    outfile = open('../doc/result.json', 'w', encoding='utf-8')
    json.dump(res, outfile, ensure_ascii=False, indent=1)


main_handler({'queryString': ''}, None)

