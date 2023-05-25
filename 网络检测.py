import datetime
import requests
import requests.exceptions as exceptions


def open_site(__name__, __url__):
    try:
        req = requests.get(
            url=__url__,
            timeout=5
        )
    except exceptions.Timeout as e:
        print(f'{__name__} TIMEOUT')
        return
    except Exception as e:
        print(f'{__name__} ERROR    Err: {e}')
        return
    if req.status_code == 200:
        print(f'{__name__} OK')
    else:
        print(f'{__name__} FAILED')


if __name__ == '__main__':
    open_site('谷歌', 'https://www.google.com/ncr')
    open_site('GitHub', 'https://github.com/')
    open_site('百度', 'https://www.baidu.com')
    open_site('腾讯', 'https://www.qq.com')
    open_site('淘宝', 'https://www.baidu.com')
