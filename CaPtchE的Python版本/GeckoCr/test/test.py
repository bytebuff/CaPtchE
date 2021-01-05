"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: test.py
    @time: 2019/12/8 16:31
    @desc:
"""
import base64
import requests


def readBase64Img():
    '''
    读取图片 并且转换成 base64 -> standard_b64encode
    :return: base64 图片
    '''
    with open('code.php.png', 'rb') as fp:
        img = fp.read()
        img = base64.standard_b64encode(img) # 需要转换成 base64
        return img


def testGecko(url, img):
    data = {
        'img': img
    }
    response = requests.post(url, data=data)
    return response.json()


if __name__ == '__main__':
    url = 'http://127.0.0.1:8001/gecko'

    img = readBase64Img()  # 读取图片
    for _ in range(100):
        result = testGecko(url, img)
        print(result)
