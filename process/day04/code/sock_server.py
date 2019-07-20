from socketserver import *

#多进程tcp并发
class Server(ForkingMixIn, TCPServer):
    pass


#请求处理类， 与服务器类型匹配
class Handler(StreamRequestHandler):
    def handle(self):
        while True:
            # self.request就是accept返回的客户端连接套接字
            data = self.request.recv(1024).decode()
            if not data:
                break
            print(data)
            self.request.send(b"OK")

#启动服务器
server = Server(('0.0.0.0', 8888), Handler)
server.serve_forever()

