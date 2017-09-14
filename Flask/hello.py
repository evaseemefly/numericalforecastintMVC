from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/hello')
def hello_world():
    return 'Hello world'

def request2obj(request):
    '''
    将传入的request转换为Request_Data 对象
    :param request:request
    :return:Request_Data对象
    '''
    # 若使用get的方式就不能通过request.form.get的方式获取数据
    request_date = request.form.get('date', None)
    request_lon_start = request.form.get('lon_start', None)
    request_lon_finish = request.form.get('lon_finish', None)
    request_lat_start = request.form.get('lat_start', None)
    request_lat_finish = request.form.get('lat_finish', None)
    request_element = request.form.get('element', None)
    request_level = request.form.get('level', None)
    request_interval = request.form.get('interval', None)
    obj = Request_Data(request_date, request_lon_start, request_lon_finish, request_lat_start, request_lat_finish,
                        request_element, request_level, request_interval)
    return obj;

@app.route('/produceImg',methods=['POST','GET'])
def produceImg():
    error=None
    if request.method=='POST':
        # 获取到前台传过来的数据
        obj= request2obj(request)
        '''
        根据obj去执行指定的shell脚本，并输入指定的参数；
        生成jpg图片
        '''

    return "ok"

class Request_Data:
    '''
    前台发过来的请求数据
    '''
    def __init__(self,date,lon_start,lon_finish,lat_start,lat_finish,element,level,interval):
        '''

        :param date:
        :param lon_start:
        :param lon_finish:
        :param lat_start:
        :param lat_finish:
        :param element:
        :param level:
        :param interval:
        '''
        self.date=date
        self.lon_start=lon_start
        self.lon_finish=lon_finish
        self.lat_start=lat_start
        self.lat_finish=lat_finish
        self.element=element
        self.level=level
        self.interval=interval


if __name__=='__main__':
    app.run(debug=True)