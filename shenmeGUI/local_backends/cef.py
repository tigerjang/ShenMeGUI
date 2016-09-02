from cefpython3 import cefpython  # TODO: CEF 5
from ..backend import  Backend
from ..utils import ExceptHook, GetApplicationPath
import sys
from ..config import Config

path_string = Config.FormatString(holders={
    '%(CEF_DIR)s': cefpython.GetModuleDirectory(),
    '%(App_DIR)s': GetApplicationPath(),
})

application_settings = Config({
    'accept_language_list': Config.String,
    'auto_zooming': Config.String,
    'background_color': (Config.Int, Config.Hex),
    'browser_subprocess_path': path_string,
    'cache_path': path_string,
    'command_line_args_disabled': Config.Bool,
    'context_menu': {
        'enabled': Config.Bool,
        'navigation': Config.Bool,
        'print': Config.Bool,
        'view_source': Config.Bool,
        'external_browser': Config.Bool,
        'devtools': Config.Bool,
    },
    'downloads_enabled': Config.Bool,
    'ignore_certificate_errors': Config.Bool,
    'javascript_flags': Config.String,
    'locale': Config.String,
    'locales_dir_path': path_string,
    'debug': Config.Bool,
    'log_file': path_string,
    'log_severity': Config.Enum({
        'LOGSEVERITY_VERBOSE': cefpython.LOGSEVERITY_VERBOSE,
        'LOGSEVERITY_INFO ': cefpython.LOGSEVERITY_INFO,
        'LOGSEVERITY_WARNING': cefpython.LOGSEVERITY_WARNING,
        'LOGSEVERITY_ERROR': cefpython.LOGSEVERITY_ERROR,
        'LOGSEVERITY_ERROR_REPORT': cefpython.LOGSEVERITY_ERROR_REPORT,
        'LOGSEVERITY_DISABLE': cefpython.LOGSEVERITY_DISABLE,
    }),
    'multi_threaded_message_loop': Config.Bool,
    'pack_loading_disabled': Config.Bool,
    'persist_session_cookies': Config.Bool,
    'persist_user_preferences': Config.Bool,
    'product_version': Config.String,
    'remote_debugging_port': Config.Int,
    'resources_dir_path': path_string,
    'single_process': Config.Bool,
    'string_encoding': Config.String,
    'uncaught_exception_stack_size': Config.Int,
    'unique_request_context_per_browser': Config.Bool,
    'user_agent': Config.String,
    'user_data_path': path_string,
    'windowless_rendering_enabled': Config.Bool,
})


class CEFBackend(Backend):
    def __init__(self):
        Backend.__init__(self)
        sys.excepthook = ExceptHook  # TODO: ??????????????

        # Application settings

        settings = {
            # "cache_path": "webcache/", # Disk cache
            # "debug": True,  # cefpython debug messages in console and in log_file  # TODO
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
