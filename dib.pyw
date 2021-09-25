from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout
import PyQt5.QtGui as QtGui
import sys
import os

filters = ["#000000", "#120800", "#1a0d00", "#362000"]
position = 0
opacity = 0.5

try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PyQt5.QtWinExtras import QtWin
    myappid = 'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

# https://stackoverflow.com/a/31966932
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Window(QWidget):
    def __init__(self):
        global opacity, position, filters

        super().__init__()
        self.title = "PyQt5 Frame"
        self.left = -3840
        self.top = -2160
        self.width = 9600
        self.height = 5400
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet('background-color:' + filters[position])
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setAttribute(Qt.WA_NoChildEventsForParent, True)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window|Qt.X11BypassWindowManagerHint|Qt.WindowStaysOnTopHint|Qt.FramelessWindowHint)
        self.setFixedSize(9600, 5400)
        self.setWindowOpacity(opacity)
        self.setWindowIcon(QtGui.QIcon(resource_path('brightness.png')))

        hbox = QHBoxLayout()
        frame = QFrame(self)
        hbox.addWidget(frame)
        self.setLayout(hbox)
        self.show()

    def keyPressEvent(self, event):
        global opacity, position, filters

        if event.key() == 16777235 and (opacity-0.1>=0):
            opacity = opacity - 0.1
            self.setWindowOpacity(opacity)
        elif event.key() == 16777237 and (opacity+0.1<=1):
            opacity = opacity + 0.1
            self.setWindowOpacity(opacity)
        elif event.key() == 16777236 and (position+1<=len(filters)-1):
            position = position + 1
            self.setStyleSheet('background-color:' + filters[position])
        elif event.key() == 16777234 and (position-1>=0):
            position = position - 1
            self.setStyleSheet('background-color:' + filters[position])

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())