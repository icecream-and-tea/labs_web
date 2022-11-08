import re
from bs4 import BeautifulSoup


class Parser(object):

    def __init__(self, soup, movieId):
        self.id = movieId
        self.title = soup.find('span', property="v:itemreviewed")
        self.imgLink = soup.find('a', class_='nbgnbg')
        self.summary = soup.find('span', class_="all hidden")
        self.celebrites = soup.find('div', id="celebrities")
        self.score = soup.find('div', class_='rating_self clearfix')
        self.award = soup.find('div', class_='mod')
        self.recommendations = soup.find('div', class_='recommendations-bd')
        self.comments = soup.find('div', id='hot-comments')
        self.moreInfo = soup.find('div', id="info")

        if self.summary is None:
            self.summary = soup.find('span', property='v:summary')

    # 总的解析函数
    def parse_all(self):
        # 创建字典用来存放解析到的信息
        movieDict = dict()

        # 将信息整合到moveiDict中
        movieDict['id'] = self.id
        movieDict['基本信息'] = self.parse_info()
        movieDict['剧情简介'] = self.parse_summary()
        movieDict['演职员'] = self.parse_celebrites()
        movieDict['热评'] = self.parse_comment()
        movieDict['相关电影'] = self.parse_recommendations()

        # print(movieDict)
        return movieDict

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

        # 4.获奖信息
        awards = []
        if self.award:
            for item in self.award.find_all('ul', class_='award'):
                tmp = item.text.split()  # 继续去除多余的'/'
                award = [item for i, item in enumerate(tmp) if item != '/']
                awards.append(award)
                # print(award)
            infoDict['获奖情况'] = awards

        # 5.解析更多信息
        infoDict.update(self.parse_moreinfo())

        return infoDict

    # 解析更多信息
    def parse_moreinfo(self):
        infoDict = dict()
        for item in str(self.moreInfo).splitlines():  # 不同信息，如导演，编剧
            item = BeautifulSoup(item, "html.parser")
            item = item.text.split(':')
            if item[0] != '':
                key = item[0]
                value = item[1]
                if key == '官方网站':
                    value = [value.lstrip()]
                elif key == '官方小站':
                    value = [self.moreInfo.find_all("a")[-1]['href']]
                    infoDict[key] = value
                    break
                else:
                    value = item[1].split('/')
                    for i in range(len(value)):
                        value[i] = value[i].lstrip().rstrip()
                infoDict[key] = value
        return infoDict

    # 获取剧情简介
    def parse_summary(self):
        summary = ''
        tmp = self.summary.text.replace('\u3000', '')
        for par in tmp.split('\n'):
            par = par.lstrip()
            if par != '':
                summary = summary + par + '\par'
        return summary

    # 获取演职员
    def parse_celebrites(self):
        castList = list()
        if not self.celebrites:
            return None
        for item in self.celebrites.find_all('li', class_='celebrity'):
            if not item.text:
                continue
            imgLink = item.div
            imgLink = imgLink['style']
            imgLink = re.findall(re.compile(r'url\((.*?)\)'), imgLink)[0]
            subItem = item.find('div', class_='info')
            person = subItem.find('a', class_='name').string
            work = subItem.find('span', class_='role').string
            personLink = subItem.a
            personLink = personLink['href']
            castList.append([person, work, personLink, imgLink])
        return castList

    # 评论
    def parse_comment(self):
        comments = []
        if not self.comments:
            return None
        for item in self.comments.find_all('span', class_='short'):
            comments.append(item.text)
        return comments

    # 相关电影推荐
    def parse_recommendations(self):
        recommendations = []
        if not self.recommendations:
            return None
        for item in self.recommendations.find_all('dl'):
            imgLink = item.img
            imgLink = imgLink['src']
            recommendations.append([item.text.split()[0], imgLink])
        return recommendations

    # 接口函数
    def run(self):
        # print('开始解析')
        res = self.parse_all()
        return res
        # 将dict 转换为 json格式
        # return json.dumps(res, ensure_ascii=False, indent=1)


# if __name__ == '__main__':
#     # 打开文件进行解析
#     inputPath = r'C:\Users\31363\Desktop\Workspace\lab_web\doc\demo.html'
#     soup = BeautifulSoup(open(inputPath, encoding='utf8'), 'html.parser')
#     parser = Parser(soup)
#     parser.parse_all()



