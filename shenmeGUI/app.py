
from cefpython3 import cefpython
from PyQt4 import QtGui
from PyQt4 import QtCore

from .utils import GetApplicationPath, ExceptHook

class App(object):
    def __init__(self):
        from local_backends.cef_qt import CEFQtBackend  # TODO
        self.backend = CEFQtBackend()  # TODO

    def run(self):
        self.backend.serve()

