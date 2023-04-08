from wsgiref.simple_server import make_server
from get_time_now import app


'''
wsgiref - wsgi сервер, поставляемый в стандартной библиотеке python
'''

def server(wsgi_support):
    s = make_server('', 8000, wsgi_support)
    print('Сервер запущен на порту 8000')
    s.serve_forever()


if __name__ == '__main__':
    server(app)