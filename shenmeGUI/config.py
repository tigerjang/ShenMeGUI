

class Config(object):
    Bool = 1
    String = 2
    Int = 3
    Hex = 4

    class Enum(object):
        def __init__(self, enum_dict):
            self._enum_dict = enum_dict

    class FormatString(object):
        def __init__(self, holders=None):
            # TODO: implement
            pass

    def __init__(self, conf_dict):
        pass

    # TODO: implement

