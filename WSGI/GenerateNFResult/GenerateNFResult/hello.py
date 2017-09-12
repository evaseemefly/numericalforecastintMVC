

def application(environ,start_response):
    method=environ('REQUEST_METHOD')
    start_response('200 ok',[('Content-Type','text/html')])
    return [b'<h1>Hi</h1>']

