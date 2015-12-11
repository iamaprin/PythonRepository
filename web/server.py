from wsgiref.simple_server import make_server

from web.hello import application

httpd = make_server('', 8000, application)
print('Sercing HTTP on port 8000...')

httpd.serve_forever()
