#-*- coding: utf-8 -*-
from selenium import webdriver
import xlwt
import time

def startDriver(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--host-resolver-rules=MAP nex.163.com 127.0.0.1')
    options.add_argument('--window-size=1920, 1080')
    options.add_argument('--start-maximized')
    options.add_argument('--disabled-gpu')
    options.add_argument('--no-sandbox')
    options.add_experimental_option('prefs', {
        'profile.managed_default_content_settings.images': 2,
    })
    chrome = webdriver.Chrome(options=options)
    chrome.get(url)
    chrome.implicitly_wait(10)

    return chrome

def getTitles(url):
    driver = startDriver(url)

    e = driver.find_element_by_class_name('load_more_btn')
    while e.is_displayed():
        if e.text.strip() == '+\n加载更多':
            e.click()
        else:
            time.sleep(1)

    for e in driver.find_elements_by_class_name('news_title'):
        yield e.text.strip()


def write(data, filename):
    workBook = xlwt.Workbook()
    sheet = workBook.add_sheet('NewTitle')

    for i, e in enumerate(data):
        sheet.write(i, 0, e)

    workBook.save('newstitle.xls')


if __name__ == '__main__':
    url = 'http://news.163.com'
    filename = 'newstitle.xls'
    data = getTitles(url)
    write(data, filename)
