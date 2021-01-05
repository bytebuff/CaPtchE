# CaPtchE简介
CaPtchE是本地打码服务，识别英文数字类型的验证码，可以快速用于验证码识别场景！有易语言版本和Python版本！
# CaPtchE易语言版本使用方式
- 下载该项目
- 双击exe执行文件
- 点击启动服务
- 调用执行打码服务，示例代码如下：
```python
import requests


class HttpRequest:

    def __init__(self):
        self.url = 'http://127.0.0.1:5658/{}'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        self.data = {

        }

    def http_request_get(self):
        response = requests.get(self.url.format("Base64后的图片"), headers=self.headers)
        print(response.text)


if __name__ == '__main__':
    session = HttpRequest()
    session.http_request_get()
```
# CaPtchE的Python版本使用方式
