import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QScroller, QScrollArea
from PyQt5.uic import loadUi

class HomePage(QMainWindow):      #home page 
    def __init__(self):
        super(HomePage,self).__init__()
        loadUi("./UI/homePage.ui",self)
        self.btn_diagnostics.clicked.connect(self.gotoDiagnostics)
        self.btn_parameters.clicked.connect(self.gotoParam)

    def gotoDiagnostics(self):
        widget.setCurrentIndex(1)

    def gotoParam(self):
        widget.setCurrentIndex(3)


class DiagnosticsInputsPage(QMainWindow): #diagnostics input page
    def __init__(self):
        super(DiagnosticsInputsPage,self).__init__()
        loadUi("./UI/diagnostics-inputs-Page.ui",self)
        self.btn_back.clicked.connect(self.gotoHome)    #call Back btn fuction
        self.btn_outputs.clicked.connect(self.gotoDiagOut)
        scroller = self.findChild(QScrollArea, "scrollArea")
        QScroller.grabGesture(scroller.viewport(), QScroller.LeftMouseButtonGesture)

    def gotoHome(self):
        widget.setCurrentIndex(0)

    def gotoDiagOut(self):
        widget.setCurrentIndex(2)

class DiagnosticsOutputsPage(QMainWindow): #diagnostics output page
    def __init__(self):
        super(DiagnosticsOutputsPage,self).__init__()
        loadUi("./UI/diagnostics-outputs-Page.ui",self)
        self.btn_back.clicked.connect(self.gotoHome)    #call Back btn fuction
        self.btn_inputs.clicked.connect(self.gotoDiagIn)
        scroller = self.findChild(QScrollArea, "scrollArea")
        QScroller.grabGesture(scroller.viewport(), QScroller.LeftMouseButtonGesture)

    def gotoHome(self):
        widget.setCurrentIndex(0)

    def gotoDiagIn(self):
        widget.setCurrentIndex(1)

class ParametersPage(QMainWindow): #diagnostics input page
    def __init__(self):
        super(ParametersPage,self).__init__()
        loadUi("./UI/parameters.ui",self)
        self.btn_back.clicked.connect(self.gotoHome)    #call Back btn fuction
        scroller = self.findChild(QScrollArea, "scrollArea")
        QScroller.grabGesture(scroller.viewport(), QScroller.LeftMouseButtonGesture)

    def gotoHome(self):
        widget.setCurrentIndex(0)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    homePage = HomePage()
    diagInPage = DiagnosticsInputsPage()
    diagOutPage = DiagnosticsOutputsPage()
    paramPage = ParametersPage()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(homePage)
    widget.addWidget(diagInPage)
    widget.addWidget(diagOutPage)
    widget.addWidget(paramPage)
    widget.setFixedWidth(800)
    widget.setFixedHeight(480)
    widget.show()
    sys.exit(app.exec_())