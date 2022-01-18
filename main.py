import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class HomePage(QMainWindow):      #home page 
    def __init__(self):
        super(HomePage,self).__init__()
        loadUi("./UI/homePage.ui",self)
        self.btn_diagnostics.clicked.connect(self.gotoDiagnostics)

    def gotoDiagnostics(self):
        widget.setCurrentIndex(1)


class DiagnosticsPage(QMainWindow): #diagnostics page
    def __init__(self):
        super(DiagnosticsPage,self).__init__()
        loadUi("./UI/diagnosticsPage.ui",self)
        self.btn_back.clicked.connect(self.gotoHome)

    def gotoHome(self):
        widget.setCurrentIndex(0)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    homePage = HomePage()
    diagPage = DiagnosticsPage()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(homePage)
    widget.addWidget(diagPage)
    widget.setFixedWidth(800)
    widget.setFixedHeight(480)
    widget.show()
    sys.exit(app.exec_())