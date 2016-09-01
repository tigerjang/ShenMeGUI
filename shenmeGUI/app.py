
# from cefpython3 import cefpython
from PyQt4 import QtGui
from PyQt4 import QtCore

from .utils import GetApplicationPath, ExceptHook
from .bindings import Binding, BindingTypes

class App(object):
    _all_pre_bindings = {}
    init_page = 'about:blank'

    def __init__(self):
        from local_backends.cef_qt import CEFQtBackend as Backend  # TODO
        pre_bindings = self._all_pre_bindings[self.__class__]
        bindings = []
        for _type, _p_src, _p_dest in pre_bindings:
            if _type == BindingTypes.JSFunction:
                src = _p_src.__get__(self, self.__class__)
                setattr(self, _p_src.func_name, src)
                bindings.append(Binding(_type, src, _p_dest))
        self.backend = Backend(init_page=self.init_page)  # TODO
        self.backend.bind_all(bindings)

    def run(self):
        self.backend.serve()

    @classmethod
    def bind2client(cls, func):
        if cls not in cls._all_pre_bindings:
            cls._all_pre_bindings[cls] = []
        cls._all_pre_bindings[cls].append((BindingTypes.JSFunction, func, func.func_name))
        return func

