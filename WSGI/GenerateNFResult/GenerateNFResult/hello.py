from cgi import parse_qs,escape

def application(environ,start_response):
    # method=environ('REQUEST_METHOD')
    try:
        size=int(environ.get('CONTENT_LENGTH',0))
    except (ValueError):
        size=0

    request_body=environ['wsgi.input'].read(size)
    d=parse_qs(request_body)
    start_response('200 ok',[('Content-Type','text/html')])
    return [b'<h1>Hi</h1>']

