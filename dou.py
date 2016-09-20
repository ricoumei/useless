import requests

headers = {
    'Host': 'www.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Cookie': 'bid="3ZWUZe43kKo"; ll="118163"; push_noty_num=0; push_doumail_num=0; __utma=30149280.656735126.1456048922.1473937865.1474203377.164; __utmz=30149280.1473599289.160.108.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utmv=30149280.13579; gr_user_id=e6c9b475-320e-45e1-b3d0-9062ed20715e; viewed="4127574"; ap=1; ct=y; ps=y; dbcl2="135795855:1tAL+RofGoM"; ck=YMRg; __utmb=30149280.8.10.1474203377; __utmc=30149280; __utmt=1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.douban.com/'
}

data = {
    'ck': 'YMRg',
    'comment': 'hello world'
}

session = requests.Session()
session.headers = headers
session.post('https://www.douban.com/', data=data)
print('success')