import requests
from fake_useragent import get_ua


class Spider(object):
    def __init__(self):
        # https://movie.douban.com/subject/1291546/
        self.url = 'https://movie.douban.com/subject/{}/'

    def get_url(self, movieId):
        return self.url.format(movieId)

    def get_html(self, url):
        # 构造请求头
        headers = {
            'User-Agent': get_ua()
        }
        res = requests.get(url, headers=headers)
        # print(str(res.request.headers))

        if res.status_code != 200:
            if res.status_code == 404:
                print('unvaild link')
                return 0
            else:
                print('error ! the status code is' + str(res.status_code))
                return -1

        return res.text

    def run(self, movieId):
        # print('开始爬取')
        url = self.get_url(movieId)
        return self.get_html(url)


