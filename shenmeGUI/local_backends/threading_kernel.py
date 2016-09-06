import threading
from Queue import Queue
# import time

from .sp_kernel import SPShell


class ThreadingKernel(SPShell):
    def __init__(self):
        SPShell.__init__(self)
        self._run_request_queue = Queue()
        self._thread = threading.Thread(target=self._main_loop)

    def _main_loop(self):
        rrq = self._run_request_queue
        while True:
            req_type, req_data = rrq.get(block=True)
            if req_type == 'c':
                self.run_script(req_data)  # TODO
            elif req_type == 'o':
                obj, args, kwargs = req_data
                obj(*args, **kwargs)

    def start(self):
        self._thread.start()

    def run(self, _code):
        self._run_request_queue.put(('c', _code))

    def run_obj(self, obj, args, kwargs):
        self._run_request_queue.put(('o', (obj, args, kwargs)))






