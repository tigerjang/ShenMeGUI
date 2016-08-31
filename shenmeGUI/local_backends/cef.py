from cefpython3 import cefpython  # TODO: CEF 5
from ..backend import  Backend
from ..utils import ExceptHook, GetApplicationPath
import sys

class CEFBackend(Backend):
    def __init__(self):
        Backend.__init__(self)
        sys.excepthook = ExceptHook  # TODO: ??????????????

        # Application settings

        settings = {
            # "cache_path": "webcache/", # Disk cache
            "debug": True,  # cefpython debug messages in console and in log_file  # TODO
            "log_severity": cefpython.LOGSEVERITY_INFO,  # LOGSEVERITY_VERBOSE
            "log_file": GetApplicationPath("debug.log"),  # Set to "" to disable.
            "release_dcheck_enabled": True,  # Enable only when debugging.
            # This directories must be set on Linux
            "locales_dir_path": cefpython.GetModuleDirectory() + "/locales",
            "resources_dir_path": cefpython.GetModuleDirectory(),
            "browser_subprocess_path": "%s/%s" % (
                cefpython.GetModuleDirectory(), "subprocess")
        }

        # Command line switches set programmatically
        switches = {
            # "proxy-server": "socks5://127.0.0.1:8888",
            # "enable-media-stream": "",
            # "--invalid-switch": "" -> Invalid switch name
        }

        cefpython.Initialize(settings, switches)
