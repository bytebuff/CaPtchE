"""
    @author: 挖掘机小王子
    @contact: scrapy@qq.com
    @software: PyCharm
    @file: 7.py
    @time: 2019/11/25 23:10
    @desc: 验证码识别
"""
import ctypes


class GeckoCr(object):

    def __init__(self):
        '''
        初始化 dll init ctypes等
        '''
        # 初始化 dll 文件 加载 dll 文件
        self.dll = ctypes.windll.LoadLibrary('oCr.dll')
        # 初始化 dll 文件中的 init
        self.dll.init()  # 初始化

    def oCr(self, img):
        '''
        识别验证码
        :param img: 传入的读取后的图片 eg: with open as f --> f.read()
        :return: 返回验证码
        '''
        result = self.dll.ocr(img, len(img))
        result = ctypes.string_at(result)
        return str(result, encoding='utf-8')


    def __del__(self):
        '''
        在文件结束的时候卸载dll文件
        :return: None
        '''
        self.dll.un() # 卸载

if __name__ == '__main__':
    GeckoCr()