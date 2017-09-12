
from wsgiref.simple_server import make_server
from hello import application

http=make_server('',8120,application)
print('服务已启动 8000')
http.serve_forever()

