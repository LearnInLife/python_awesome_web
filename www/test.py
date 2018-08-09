# _*_ coding:utf-8 _*_

import orm
from models import *
import asyncio
import os

dir1 = os.path.dirname(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))

mod = __import__('orm', globals(), locals())

for d in dir(mod):
    print(d)


@asyncio.coroutine
def test():
    yield from orm.create_pool(loop, user='root', password='123456', db='awesome')

    u = User(name='test', email='test@163.com', passwd='123456', image='about:blank')

    yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test())

from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, '')
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()