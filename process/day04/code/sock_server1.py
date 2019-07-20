from socketserver import *

#多进程UDP并发
class Server(ForkingMixIn, UDPServer):
    pass


#请求处理类， 与服务器类型匹配
class Handler(DatagramRequestHandler):
    def handle(self):
        while True:
            data = self.rfile.readline().decode()
            if not data:
                break
            print(data)
            self.wfile.write(b"OK")

#启动服务器
server = Server(('0.0.0.0', 8888))
server.serve_forever()

