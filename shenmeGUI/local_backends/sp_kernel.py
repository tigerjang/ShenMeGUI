'''
A Simple interactive python kernel
'''
import types
import sys
import traceback


class SPShell(object):
    def __init__(self):
        self._user_module = None
        self._user_ns = None
        self._init_module()


    def _init_module(self):
        user_module = types.ModuleType("__main__",
                                       doc="Automatically created module for Simple Python interactive Shell")
        user_ns = user_module.__dict__
        # user_ns.setdefault('__builtin__', builtin_mod)
        # user_ns.setdefault('__builtins__', builtin_mod)

        # sys.modules[user_module.__name__] = user_module
        self._user_module, self._user_ns = user_module, user_ns
        self.run_script('')

        # self._swap_region = types.ModuleType("__kernel_swap__",
        #                                      doc="Swap module for kernel and outside")
        # self.user_global_ns.update({'__kernel_swap__': self._swap_region})

    @property
    def user_global_ns(self):
        return self._user_module.__dict__

    @property
    def user_global(self):
        return self._user_module

    def run_script(self, code_obj, result=None):
        # Set our own excepthook in case the user code tries to call it
        # directly, so that the IPython crash handler doesn't get triggered
        # old_excepthook, sys.excepthook = sys.excepthook, self.excepthook

        # we save the original sys.excepthook in the instance, in case config
        # code (such as magics) needs access to it.
        # self.sys_excepthook = old_excepthook
        outflag = 1  # happens in more places, so it's easier as default
        try:
            try:
                # self.hooks.pre_run_code_hook()
                # rprint('Running code', repr(code_obj)) # dbg
                exec(code_obj, self.user_global_ns, self._user_ns)
            finally:
                # Reset our crash handler in place
                # sys.excepthook = old_excepthook
                pass
        except SystemExit as e:
            if result is not None:
                result.error_in_exec = e
            self.showtraceback(exception_only=True)
            # warn("To exit: use 'exit', 'quit', or Ctrl-D.", level=1)
        # except self.custom_exceptions:
        #     etype, value, tb = sys.exc_info()
        #     if result is not None:
        #         result.error_in_exec = value
        #     self.CustomTB(etype, value, tb)
        except:
            if result is not None:
                result.error_in_exec = sys.exc_info()[1]
            self.showtraceback()
        else:
            outflag = 0
        return outflag

    def showtraceback(self, exc_tuple=None, filename=None, tb_offset=None,
                      exception_only=False):
        traceback.print_exc()

#
# sss = SPShell()
# sss.run_code('print aaa')
# import time
# sss.run_code('''
# import sys
# # import time
# # def aaa(bbb):
# #     time.sleep(10)
# # aaa(2333)
# ''')

