import re
from bs4 import BeautifulSoup

'''
要爬取信息：
    1. 基本信息
    2. 作者简介
    3. 内容简介
    4. 原文摘录
    5. 推荐电子书
    6. 推荐书籍
    7. 评论
'''


class Parser(object):

    def __init__(self, soup):
        self.title = soup.find('span', property="v:itemreviewed")
        self.imgLink = soup.find('a', class_='nbg')
        self.score = soup.find('div', class_='rating_self clearfix')
        self.blockquote = soup.find('ul', class_='blockquote-list')
        self.comments = soup.find('div', class_='comment-list new_score show')
        self.moreInfo = soup.find('div', id="info")

        # 内容简介
        tmp = soup.find('div', class_="indent", id='link-report')
        if tmp:
            self.summary = tmp.find('span', class_='all hidden')
            if self.summary is None:
                self.summary = tmp.find('div', class_='intro')
        else:
            self.summary = None

        # 作者简介
        tmp = soup.find('div', class_='related_info').find('div', class_="indent", id=False)
        if tmp:
            self.author = tmp.find('span', class_='all hidden')
            if self.author is None:
                self.author = tmp.find('div', class_='intro')
        else:
            self.author = None

        # 推荐电子书
        tmp = soup.find('div', id='rec-ebook-section')
        if tmp:
            self.recom_ebook = tmp.find('div', class_='content clearfix')
        else:
            self.recom_ebook = None

        # 推荐书籍
        tmp = soup.find('div', id='db-rec-section')
        if tmp:
            self.recom_book = tmp.find('div', class_='content clearfix')
        else:
            self.recom_book = None

    # 总的解析函数
    def parse_all(self):
        # 创建字典用来存放解析到的信息
        bookDict = dict()

        # 将信息整合到moveiDict中
        bookDict['基本信息'] = self.parse_info()
        bookDict['内容简介'] = self.parse_summary()
        bookDict['作者简介'] = self.parse_author()
        bookDict['原文摘录'] = self.parse_blockquote()
        bookDict['电子书推荐'] = self.parse_recom_ebook()
        bookDict['书籍推荐'] = self.parse_recom_book()
        bookDict['热评'] = self.parse_comment()

        return bookDict

    # 解析基本信息
    def parse_info(self):
        infoDict = dict()

        # 1.标题
        infoDict['标题'] = self.title.text  # 总不至于连标题也没有吧

        # 2.图片链接
        if self.imgLink:
            infoDict['图片链接'] = self.imgLink.img['src']

        # 3.评分 {'评分':['xxx 评分', 'xxx 人数']}
        if self.score:
            score = self.score.text.split()
            score[1] = score[1][:-3]
            infoDict['评分'] = score

        # 5.解析更多信息
        infoDict.update(self.parse_moreinfo())

        return infoDict

    # 解析更多信息
    def parse_moreinfo(self):
        infoDict = dict()
        for item in re.split('<br>|<br/>', str(self.moreInfo)):  # 不同信息
            item = BeautifulSoup(item, "html.parser")
            item = re.sub('[ \n]', '', item.text)
            if not item:
                continue
            item = item.split(':')
            key = item[0]
            value = item[1].strip()
            infoDict[key] = value
        return infoDict

    # 获取内容简介
    def parse_summary(self):
        if not self.summary:
            return None
        summary = ''
        for par in self.summary.find_all('p'):
            par = par.text.replace('\u3000', '')
            summary = summary + par + '\par'
        return summary

    # 获取作者简介
    def parse_author(self):
        if not self.author:
            return None
        author = ''
        for par in self.author.find_all('p'):
            par = par.text.replace('\u3000', '')
            author = author + par + '\par'
        return author

    # 获取原文摘录
    def parse_blockquote(self):
        if not self.blockquote:
            return None

        blockquote = list()
        [s.extract() for s in self.blockquote('div')]
        for item in self.blockquote.find_all('figure'):
            blockquote.append(item.text.strip().split(' (查看原文)')[0])
        return blockquote

    # 相关电子书推荐
    def parse_recom_ebook(self):
        if not self.recom_ebook:
            return None
        recom_ebook = list()
        for item in self.recom_ebook.find_all('dl'):
            imgLink = item.img
            imgLink = imgLink['src']
            recom_ebook.append([item.text.split()[0], imgLink])
        return recom_ebook

    # 相关书籍推荐
    def parse_recom_book(self):
        if not self.recom_book:
            return None

        recom_book = list()
        for item in self.recom_book.find_all('dl'):
            if not item.text:
                continue
            imgLink = item.img
            imgLink = imgLink['src']
            recom_book.append([item.text.split()[0], imgLink])
        return recom_book

    # 评论
    def parse_comment(self):
        if not self.comments:
            return None

        comments = []
        for item in self.comments.find_all('span', class_='short'):
            comments.append(item.text)
        return comments

    # 接口函数
    def run(self):
        # print('开始解析')
        res = self.parse_all()
        return res
        # 将dict 转换为 json格式
        # return json.dumps(res, ensure_ascii=False, indent=1)


# if __name__ == '__main__':
#     # 打开文件进行解析
#     inputPath = r'C:\Users\31363\Desktop\Workspace\lab_web\book_spider\doc\demo.html'
#     soup = BeautifulSoup(open(inputPath, encoding='utf8'), 'html.parser')
#     parser = Parser(soup)
#     parser.parse_all()



