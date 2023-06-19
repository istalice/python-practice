import requests
from lxml import etree


def douban_hot_topics():
    req = requests.get(
        url='https://www.douban.com/gallery/',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/113.0.0.0 Safari/537.36'
        }
    )
    html = etree.HTML(req.text)
    results = html.xpath('//div[@class="aside"]/div[@class="mod"]/ul[@class="trend"]/li/a')
    for item in results:
        print(item.attrib['href'], item.text)


if __name__ == '__main__':
    douban_hot_topics()
