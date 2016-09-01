import weakref
from .helpers import is_string


class Selector(object):
    def __init__(self, root_node):
        self._id_dict = weakref.WeakValueDictionary()
        self._root_node = root_node  # TODO: Need weakref ?

    def __call__(self, s_str):
        # TODO: More select options !!!!!!!!!!!!!
        if s_str.startwith('#'):
            return self.by_id(s_str[1: ].strip())
        return None

    def by_id(self, id):
        if id in self._id_dict:
            return self._id_dict[id]
        else:
            raise KeyError('No id: %s in Dom of root %s' % (id, self._root_node.__repr__()))


class _GroupManList(list):
    def __init__(self, *args, **kw):
        super(_GroupManList, self).__init__(*args, **kw)

    def __getattr__(self, foo):
        ret = _GroupManList()
        for node in self:
            ret.append(getattr(node, foo))
        return ret

    def __call__(self, *args, **kw):  # TODO: is this also work for decorator ???
        ret = _GroupManList()
        for node in self:
            ret.append(node(*args, **kw))
        return ret

    def __repr__(self):
        return 'GroupManList(%s)' % super(_GroupManList, self).__repr__()


class _DomNode(object):
    _type = 'NodeBase'

    def __init__(self, dom, id=None, cls=None):
        self._children = []
        if id is None:
            id = '__%d__' % hash(self)  # TODO: better hash ?
        assert is_string(id)
        self._id = id
        self._parent = None  # weak ref !!!
        self._dom_root = weakref.ref(dom)

    @property
    def dom_root(self):
        if self._is_root:
            return self
        elif self._parent:
            return self._parent().dom_root
        return None

    def append_child(self, node):
        self._children.append(node)
        node._parent = weakref.ref(self)

    def __le__(self, other):
        if isinstance(other, _DomNode):
            self.append_child(other)
        elif isinstance(other, list):
            for _n in other:
                self.append_child(_n)
        else:
            raise ValueError('Child element must be DomNode or List of DomNode')
        return self

    def __getitem__(self, item):
        if isinstance(item, int) or isinstance(item, long):
            return self._children[item]

    def __repr__(self):
        attr = 'id="%s"' % self._id if self._id else ''
        return '%s(%s)' % (self._type, attr)

    def _print_cascade(self):
        if len(self._children) > 0:
            lines = [self.__repr__() + ' <= [']
            for ch in self._children:
                lines.extend(map(lambda _s: '    ' + _s, ch._print_cascade()))
            lines.append('], ')
            return lines
        else:
            return [self.__repr__() + ', ']

    def __str__(self):
        return '\n'.join(self._print_cascade())


class DomRoot(_DomNode):
    _type = 'Document'

    def __init__(self):
        _DomNode.__init__(self, self)
        self._all_ele_ref = weakref.WeakValueDictionary()





class Div(_DomNode):
    _type = 'Div'


lll = DomRoot(id='1')

lll <= Div() <= [
    Div() <= Div(),
    Div(),
]

lll <= Div(id='23333')
print lll