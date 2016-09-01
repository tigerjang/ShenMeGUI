import sys

sys.path.extend([r'E:\Work\Yoda-master', r'E:\Work\Xtalpi\libs'])
import os

if 'YODA_CONFIG' not in os.environ:
    os.environ['YODA_CONFIG'] = r'E:\Work\Yoda-master\test_config.ini'

from shenmeGUI import App
#
#
# class disc(object):
#     def __init__(self):
#         pass
#
#     def __get__(self, instance, owner):
#         print instance, owner
#         def foo(fff):
#             print fff.func_name
#             return fff
#         return foo
#
#
#
# class App:
#     Bind2Client = disc()
#     _bindings = {}
#     def __init__(self):
#         pass
#
#     @classmethod
#     def hhh(cls, func):
#         print cls
#         print func.func_name
#         if cls not in cls._bindings:
#             cls._bindings[cls] = []
#         cls._bindings[cls].append(func.func_name)
#         setattr(cls, func.func_name, func)
#         return func
#
class TestApp(App):
    init_page = 'https://www.baidu.com'
    def __init__(self):
        App.__init__(self)
        pass

@TestApp.bind2client
def py_print(self, *args, **kw):
    print self
    print args
    print kw


app = TestApp()
app.run()


