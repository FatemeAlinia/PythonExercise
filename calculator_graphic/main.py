# This Python file uses the following encoding: utf-8
import sys
import os
import math

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from functools import partial

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        loader = QUiLoader()
        self.r=0
        self.rop=''
        self.num1=0
        self.num2=0
        self.ui=loader.load('form.ui')
        self.ui.show()
        self.ui.btn1.clicked.connect(partial(self.shownumber,'1'))
        self.ui.btn2.clicked.connect(partial(self.shownumber,'2'))
        self.ui.btn3.clicked.connect(partial(self.shownumber,'3'))
        self.ui.btn4.clicked.connect(partial(self.shownumber,'4'))
        self.ui.btn5.clicked.connect(partial(self.shownumber,'5'))
        self.ui.btn6.clicked.connect(partial(self.shownumber,'6'))
        self.ui.btn7.clicked.connect(partial(self.shownumber,'7'))
        self.ui.btn8.clicked.connect(partial(self.shownumber,'8'))
        self.ui.btn9.clicked.connect(partial(self.shownumber,'9'))
        self.ui.btn0.clicked.connect(partial(self.shownumber,'0'))
        self.ui.btnplus.clicked.connect(partial(self.opr,'+'))
        self.ui.btnsub.clicked.connect(partial(self.opr,'-'))
        self.ui.btnmul.clicked.connect(partial(self.opr,'*'))
        self.ui.btndiv.clicked.connect(partial(self.opr,'/'))
        self.ui.btncos.clicked.connect(partial(self.opr,'cos'))
        self.ui.btnsin.clicked.connect(partial(self.opr,'sin'))
        self.ui.btntan.clicked.connect(partial(self.opr,'tan'))
        self.ui.btncot.clicked.connect(partial(self.opr,'cot'))
        self.ui.btnsqrt.clicked.connect(partial(self.opr,'qrt'))
        self.ui.btnpow.clicked.connect(partial(self.opr,'^'))
        self.ui.btneq.clicked.connect(self.rlt)
        self.ui.btncleare.clicked.connect(self.Clr)
        self.ui.btndelete.clicked.connect(self.dell)
        

    def shownumber(self,txt):
        text=self.ui.label.text()
        self.ui.label.setText(text + txt)

    def opr(self,opera):
        self.num1=self.ui.label.text()
        self.ui.label.setText("")
        self.op=opera

    def Clr(self):
        self.ui.label.setText('')

    def dell(self):
        self.dle = self.ui.label.text()
        self.ui.label.setText(self.dle[:len(self.dle) - 1])
        

    def rlt(self):
        self.num2=self.ui.label.text()
        if self.op=='+':
            self.r=float(self.num1)+float(self.num2)
        self.ui.label.setText(str(self.r)) 

        if self.op=='-':
            self.r=float(self.num1)-float(self.num2)
        self.ui.label.setText(str(self.r)) 

        if self.op=='*':
            self.r=float(self.num1)*float(self.num2)
        self.ui.label.setText(str(self.r))   

        if self.op=='/':
            self.r=float(self.num1)/float(self.num2)
        self.ui.label.setText(str(self.r))            

        if self.op=='cos':
            self.r=float(math.cos(float(self.num1)))
        self.ui.label.setText(str(self.r))  

        if self.op=='sin':
            self.r=float(math.sin(float(self.num1)))
        self.ui.label.setText(str(self.r))   

        if self.op=='tan':
            self.r=float(math.tan(float(self.num1)))
        self.ui.label.setText(str(self.r))  

        if self.op=='cot':
            self.r=float(1/math.cos(float(self.num1)))
        self.ui.label.setText(str(self.r))  

        if self.op=='qrt':
            self.r=float(math.sqrt(float(self.num1)))
        self.ui.label.setText(str(self.r))    

        
        
        if self.op=='^':
            self.r=math.pow(float(self.num1),float(self.num2))
        self.ui.label.setText(str(self.r)) 




        


                                                          
                                                                   


            

if __name__ == "__main__":
    app = QApplication([])
    widget = Calculator()
    sys.exit(app.exec())


