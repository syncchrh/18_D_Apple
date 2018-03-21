#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *
from Module_Sseung import CSVFileIO
import csv

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        self.setWindowTitle("Test")
        self.setGeometry(300, 300, 300, 150)

        btn1 = QPushButton("Test", self)
        btn1.move(190, 10)
        btn1.clicked.connect(self.btn1_clicked)

        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(10, 10, 170, 130)

    def btn1_clicked(self):
        ret = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", ["0"])
        kospi_code_list = ret.split(';')
        kospi_code_name_list = []

        #print(ret)
        #print("ret[0] = " + ret[0])

        #for x in kospi_code_list:
        #    name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)", [x])
        #    test = self.kiwoom.dynamicCall("GetMasterLastPrice(QString)", [x])
        #    kospi_code_name_list.append(x + " : " + name + " : " + test)
        #    print(kospi_code_name_list)
        #self.listWidget.addItems(kospi_code_name_list)


        #종목 코드의 한글명 반환
        name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)", '017800')
        nStock = self.kiwoom.dynamicCall("GetMasterListedStockCnt(QString)", '017800')
        sJudge = self.kiwoom.dynamicCall("GetMasterConstruction(QString)", '017800')
        record = self.kiwoom.dynamicCall("GetRepeatCnt(QString)", 'OPT100001', '주식기본정보')
        info = self.kiwoom.dynamicCall("GetLoginInfo(QString)", 'ACCNO')

        test = self.kiwoom.dynamicCall("GetMasterLastPrice(QString)", '017800')
        test2 = self.kiwoom.dynamicCall("GetCommRealData(Qstring)", '017800', 10);

        #조회 프로시저
        self.kiwoom.dynamicCall("SetInputValue(QString)", '종목코드', '017800')
        test = self.kiwoom.dynamicCall("CommRqData(QString)", '주식기본정보', 'OPT10001', '0', '1001')
        self.kiwoom.dynamicCall("OnReceiveMsg(QString)", '주식기본정보', 'OPT10001', '0')
        self.kiwoom.dynamicCall("OnReceiveTrData(QString)", '주식기본정보', 'OPT10001', '0')


        print(name)
        print(nStock)
        print(sJudge)
        print(record)
        print(info)
        print(test)


        #kospi_code_name_list.append("017800" + " : " + name + " : " + test + " : ")
        #print(kospi_code_name_list)
        #print(kospi_code_name_list[0])



        CSVFileIO.setCsv("E:\99.Coding\\18_D_Apple\Data\output.csv", kospi_code_name_list)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())