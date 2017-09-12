import web
import json
urls = (
    '/', 'index'
)

class index:
    def GET(self):
        # 通过该方法获取传过来的数据
        data=web.data()
        return "Hello, world!"

    def POST(self):
        data_byte=web.data()
        data_str=data_byte.decode('utf8')
        # input适用于url中拼接的参数
        # data_input=web.input()
        data_obj=json.loads(data_str)
        return "ok"
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()