import sys

sys.path.extend([r'E:\Work\Yoda-master', r'E:\Work\Xtalpi\libs'])
import os
import time

if 'YODA_CONFIG' not in os.environ:
    os.environ['YODA_CONFIG'] = r'E:\Work\Yoda-master\test_config.ini'

from shenmeGUI import App

from shenmeGUI.local_backends.threading_kernel import ThreadingKernel


def py_test(*args, **kw):
    print "ZZZZZZ....."
    time.sleep(10)
    print "Awake !!!"
    print args


class TestApp(App):
    init_page = 'https://www.baidu.com'

    def __init__(self):
        App.__init__(self)
        self.kkk = ThreadingKernel()
        self.kkk.start()
        self.backend.bind_js(py_test)
        self.kkk.user_global.on_XXX = self.onXXX
        self.kkk.run('''
import time

@on_XXX
def py_on_xxx(*args, **kwargs):
    print args
    if len(args) > 0:
        op = args[0]
        if isinstance(op, dict):
            if 'callback' in op:
                op['callback'].Call()

@on_XXX
def py_sleep(*args, **kw):
    print "hahaha....."
    time.sleep(10)
    print "Awake !!!"
''')

    def onXXX(self, func):
        print func
        def run_XXX(*args, **kwargs):
            self.kkk.run_obj(func, args, kwargs)
        self.backend.bind_js(run_XXX, js_name=func.func_name)
        return func

# py_on_xxx({callback: function () {console.log('ccccccccc');}})

@TestApp.bind2client
def py_print(self, *args, **kw):
    print self
    print args
    print kw


app = TestApp()
app.run()



# kkk = ThreadingKernel()
# kkk.start()
#
# kkk.run('''
# import time
# def py_test(aaa, ccc):
#     time.sleep(10)
#     print aaa
#     # ccc.Call()
# ''')
#
# kkk.user_global_ns['py_test'](2333, 2333)
