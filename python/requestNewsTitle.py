# -*- coding:utf-8 -*-
from requests import get
from bs4 import BeautifulSoup
import xlwt

def getResponse(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    r = get(url, headers)
    print(r)
    if r.status_code != 200:
        raise RuntimeError('网络错误')
    return r.text

def getTitles(text):
    soup = BeautifulSoup(text, 'lxml')
    print(soup.prettify())
    titles = soup.select('.news_title')
    for a in titles:
        print(a.string)
        yield (a.string, a['href'])



if __name__ == '__main__':
    url = 'http://news.163.com'
    workBook = xlwt.Workbook()
    sheet = workBook.add_sheet('NewTitle')

    for i, e in enumerate(getTitles(getResponse(url))):
        sheet.write(i, 0, e[0])
        sheet.write(i, 1, e[1])

    workBook.save('newstitle.xls')
