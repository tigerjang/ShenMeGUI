from PyQt4 import QtGui
from PyQt4 import QtCore
from ..utils import GetApplicationPath, ExceptHook
from cefpython3 import cefpython
from .cef import CEFBackend
import sys


class MainWindow(QtGui.QMainWindow):
    mainFrame = None

    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.createMenu()
        self.mainFrame = MainFrame(self)
        self.setCentralWidget(self.mainFrame)
        self.resize(1024, 768)
        self.setWindowTitle('PyQT CEF 3 example')
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def createMenu(self):
        menubar = self.menuBar()
        filemenu = menubar.addMenu("&File")
        filemenu.addAction(QtGui.QAction("Open", self))
        filemenu.addAction(QtGui.QAction("Exit", self))
        aboutmenu = menubar.addMenu("&About")

    def focusInEvent(self, event):
        cefpython.WindowUtils.OnSetFocus(int(self.centralWidget().winId()), 0, 0, 0)

    def closeEvent(self, event):
        self.mainFrame.browser.CloseBrowser()


class MainFrame(QtGui.QWidget):
    browser = None

    def __init__(self, parent=None):
        super(MainFrame, self).__init__(parent)
        windowInfo = cefpython.WindowInfo()
        windowInfo.SetAsChild(int(self.winId()))
        self.browser = cefpython.CreateBrowserSync(windowInfo,
                                                   browserSettings={},
                                                   # navigateUrl=GetApplicationPath("file:///E:/Work/MyProjects/3D_Project/temp-plot.html"))
                                                   navigateUrl=GetApplicationPath("http://127.0.0.1:5000/multi_views"))

        self.show()

    def moveEvent(self, event):
        cefpython.WindowUtils.OnSize(int(self.winId()), 0, 0, 0)

    def resizeEvent(self, event):
        cefpython.WindowUtils.OnSize(int(self.winId()), 0, 0, 0)


class _QtApp(QtGui.QApplication):
    timer = None

    def __init__(self, args):
        super(_QtApp, self).__init__(args)
        self.createTimer()

    def createTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.onTimer)
        self.timer.start(10)

    def onTimer(self):
        # The proper way of doing message loop should be:
        # 1. In createTimer() call self.timer.start(0)
        # 2. In onTimer() call MessageLoopWork() only when
        #    QtGui.QApplication.instance()->hasPendingEvents() returns False.
        # But... there is a bug in Qt, hasPendingEvents() returns always true.
        cefpython.MessageLoopWork()

    def stopTimer(self):
        # Stop the timer after Qt message loop ended, calls to MessageLoopWork()
        # should not happen anymore.
        self.timer.stop()


class CEFQtBackend(CEFBackend):
    def __init__(self):
        print("[CEFQtBackend] PyQt version: %s" % QtCore.PYQT_VERSION_STR)
        print("[CEFQtBackend] QtCore version: %s" % QtCore.qVersion())
        CEFBackend.__init__(self)

        self.qt_app = _QtApp(sys.argv)
        self.mainWindow = MainWindow()

    def serve(self, *args, **kw):
        self.mainWindow.show()
        self.qt_app.exec_()
        self.qt_app.stopTimer()
        self.on_stop()

    def on_stop(self):
        try:
            del self.mainWindow
            del self.qt_app
        except Exception, e:
            pass
        try:
            cefpython.Shutdown()
        except Exception, e:
            pass

    def __del__(self):
        self.on_stop()  # TODO: Need???

