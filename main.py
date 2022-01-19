import threading
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QScroller, QScrollArea, QPushButton, QLabel
from PyQt5.uic import loadUi
from Parameters.parameters import param
from time import sleep

global parameters
global parameterNumber

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
        global parameters
        parameters = param.getData()
        btn_change = [0]*8
        self.label_parameters = [0]*8
        for i in range(8):
            btnNum = "btn_param_" + str(i)
            btn_change[i] = self.findChild(QPushButton, btnNum)
            label_param = "label_param_" + str(i)
            self.label_parameters[i] = self.findChild(QLabel, label_param)
            self.label_parameters[i].setText(parameters[str(i)])

        btn_change[0].clicked.connect(lambda: self.gotoParamInput(0))
        btn_change[1].clicked.connect(lambda: self.gotoParamInput(1))
        btn_change[2].clicked.connect(lambda: self.gotoParamInput(2))
        btn_change[3].clicked.connect(lambda: self.gotoParamInput(3))
        btn_change[4].clicked.connect(lambda: self.gotoParamInput(4))
        btn_change[5].clicked.connect(lambda: self.gotoParamInput(5))
        btn_change[6].clicked.connect(lambda: self.gotoParamInput(6))
        btn_change[7].clicked.connect(lambda: self.gotoParamInput(7))

        self.startParamUpdateThread()

    def gotoHome(self):
        widget.setCurrentIndex(0)

    def gotoParamInput(self, paramNum):
        global parameterNumber
        parameterNumber = str(paramNum)
        widget.setCurrentIndex(4)

    def reloadParameters(self):
        global parameters
        parameters = param.getData()
        for i in range(8):
            self.label_parameters[i].setText(parameters[str(i)])

#reloads parameter values when ever the page is clicked
    def paramUpdateThread(self):
        sleep(0.1)    #let the widget load 
        self.boolReload = True
        while True:
            try:
                if (widget.currentIndex()==3) and self.boolReload==True:
                    self.boolReload = False
                    self.reloadParameters()
                
                elif (widget.currentIndex()!=3) and self.boolReload==False:
                    self.boolReload = True
            
            except:
                pass
            
            sleep(0.1)

    def startParamUpdateThread(self):
        thread = threading.Thread(target=self.paramUpdateThread)
        thread.daemon = 1
        thread.start()
            
        
class ParametersInputPage(QMainWindow): #diagnostics input page
    def __init__(self):
        self.param=0
        self.digits=0
        super(ParametersInputPage,self).__init__()
        loadUi("./UI/parameter-input.ui",self)
        self.label_paramVal.setText(str(self.param))
        self.btn_ok.clicked.connect(self.updateParameters)
        self.btn_cancel.clicked.connect(self.gotoParam)

        btn_num = [0]*10
        for i in range(10):
            btn = "btn_num_" + str(i)
            btn_num[i] = self.findChild(QPushButton, btn)

        btn_num[0].clicked.connect(lambda: self.btn_num_pressed(0))
        btn_num[1].clicked.connect(lambda: self.btn_num_pressed(1))
        btn_num[2].clicked.connect(lambda: self.btn_num_pressed(2))
        btn_num[3].clicked.connect(lambda: self.btn_num_pressed(3))
        btn_num[4].clicked.connect(lambda: self.btn_num_pressed(4))
        btn_num[5].clicked.connect(lambda: self.btn_num_pressed(5))
        btn_num[6].clicked.connect(lambda: self.btn_num_pressed(6))
        btn_num[7].clicked.connect(lambda: self.btn_num_pressed(7))
        btn_num[8].clicked.connect(lambda: self.btn_num_pressed(8))
        btn_num[9].clicked.connect(lambda: self.btn_num_pressed(9))

        self.btn_clr.clicked.connect(self.btnClr_pressed)
        self.btn_backspace.clicked.connect(self.btnBackspace_pressed)

    def gotoParam(self):
        self.param=0
        self.digits=0
        widget.setCurrentIndex(3)
        self.label_paramVal.setText(str(self.param))

    def updateParameters(self):
        global parameters
        global parameterNumber
        parameters[str(parameterNumber)] = str(self.param)
        param.setData(parameters)
        self.param=0
        self.digits=0
        widget.setCurrentIndex(3)
        self.label_paramVal.setText(str(self.param))

    def btn_num_pressed(self, btnNumber):
        if self.digits < 4:
            self.param *= 10
            self.digits += 1
            self.param += btnNumber
            self.label_paramVal.setText(str(self.param))

    def btnClr_pressed(self):
        self.param=0
        self.digits=0
        self.label_paramVal.setText(str(self.param))

    def btnBackspace_pressed(self):
        if self.digits > 0:
            self.param = int(self.param/10)
            self.digits -= 1
            self.label_paramVal.setText(str(self.param))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    homePage = HomePage()
    diagInPage = DiagnosticsInputsPage()
    diagOutPage = DiagnosticsOutputsPage()
    paramPage = ParametersPage()
    paramInPage = ParametersInputPage()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(homePage)
    widget.addWidget(diagInPage)
    widget.addWidget(diagOutPage)
    widget.addWidget(paramPage)
    widget.addWidget(paramInPage)
    widget.setFixedWidth(800)
    widget.setFixedHeight(480)
    widget.show()
    sys.exit(app.exec_())