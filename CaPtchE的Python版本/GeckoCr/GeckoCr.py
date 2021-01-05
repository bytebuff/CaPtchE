"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: GeckoCr.py
    @time: 2019/11/29 22:34
    @desc:
"""
import base64
from oCr.oCr import GeckoCr
from flask import Flask, request, render_template

app = Flask(__name__)
geckocr = GeckoCr()


@app.route('/')  # 首页
def index():
    return '欢迎使用 GeckoCr 验证码识别系统'


@app.route('/gecko', methods=['POST', 'GET'])
def gecko():
    '''
    实现验证码的识别与返回
    :return: 识别结果
    '''
    img = request.form['img']
    # imgBase64 = base64.standard_b64encode(bytes(img))
    imgBinary = base64.standard_b64decode(img)
    imgResult = geckocr.oCr(imgBinary)
    if imgResult:
        imgResult = {
            'result': imgResult,
            'ok': 1
        }
    return imgResult


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run(port=8001)
