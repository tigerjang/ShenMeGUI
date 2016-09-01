
class BindingTypes:
    JSFunction = 1
    JSObject = 2


class Binding(object):
    def __init__(self, type, src, dest):
        self.type = type
        self.src = src
        self.dest = dest

