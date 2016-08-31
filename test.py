import sys

sys.path.extend([r'E:\Work\Yoda-master', r'E:\Work\Xtalpi\libs'])
import os

if 'YODA_CONFIG' not in os.environ:
    os.environ['YODA_CONFIG'] = r'E:\Work\Yoda-master\test_config.ini'

from shenmeGUI import App

class App:
    N = '233'
    def __init__(self):
        pass


class HHH(object):
    def onload(self, callback):
        return callback


class TestApp(App):
    aaa = App.N
    ui = HHH()
    ui <= '123'

    def __init__(self):
        App.__init__(self)
        pass

    @ui.onload
    def on_load(self):
        pass

    # @App.on_load
    # def on_load(self):
    #     pass

app = TestApp()
app.run()


