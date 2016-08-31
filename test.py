import sys

sys.path.extend([r'E:\Work\Yoda-master', r'E:\Work\Xtalpi\libs'])
import os

if 'YODA_CONFIG' not in os.environ:
    os.environ['YODA_CONFIG'] = r'E:\Work\Yoda-master\test_config.ini'

from shenmeGUI import App


app = App()
app.run()


