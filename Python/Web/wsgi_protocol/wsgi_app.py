def app(environ, start_response):
    '''Эта функция удовлетворяет wsgi протоколу.'''
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
