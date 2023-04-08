from datetime import datetime


def app(environ, start_response):
    time = datetime.now()
    data = bytes(f'Time now is: {time:%H:%M:%S}\n', 'utf-8')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return [data]