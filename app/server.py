""" This will create the falcon app for va_thon endpoints.
    Import all the endpoint handlers and add routes here.
"""
from wsgiref import simple_server
import falcon
from falcon_multipart.middleware import MultipartMiddleware

from app.apis import servicecheck


def create_server():
    app = falcon.API(middleware=list(filter(None, [MultipartMiddleware(), None, None])))
    servicecheckapi = servicecheck.ServiceCheck()
    app.add_route("/servicecheck", servicecheckapi)
    return app


def getapp():
    return create_server()


if __name__ == "__main__":
    httpd = simple_server.make_server('localhost', 8999, getapp())
    httpd.serve_forever()
