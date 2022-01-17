import sys

from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QLabel
from PySide2.QtCore import QFile, QObject, QEvent, QTime

    #this class removes the hover effect 
class ButtonEventFilter(QObject):       
    def eventFilter(self, obj, event):
        if event.type() == QEvent.HoverEnter:
            return True
        return False

class Form(QObject):
    
    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        btn_diagnostics = self.window.findChild(QPushButton, 'btn_diagnostics')
        btn_warnings = self.window.findChild(QPushButton, 'btn_warnings')
        btn_errors = self.window.findChild(QPushButton, 'btn_errors')
        btn_settings = self.window.findChild(QPushButton, 'btn_settings')

            #removing hover effect
        filter = ButtonEventFilter(self)
        btn_diagnostics.installEventFilter(filter)
        btn_warnings.installEventFilter(filter)
        btn_errors.installEventFilter(filter)
        btn_settings.installEventFilter(filter)

        time_label = self.window.findChild(QLabel, 'time_label')
        time_label.setText(QTime.currentTime().toString('hh:mm A'))

        self.window.show()
        # self.window.showFullScreen()

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    form = Form("./mainWindow.ui")
    sys.exit(app.exec_())