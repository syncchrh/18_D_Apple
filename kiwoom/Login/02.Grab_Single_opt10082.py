#-*- coding: utf-8 -*-
#로그인 이벤트 처리하기

import sys, threading, time
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
        ## UI 창, 리스트, 텍스트
        self.setWindowTitle("종목 코드")
        self.setGeometry(300, 300, 600, 300)
        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(10, 10, 200, 280)
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(300, 200, 280, 80)
        self.text_edit.setEnabled(False)

        ## UI 버튼 (종목코드 얻기)
        btn1 = QPushButton("종목코드 얻기", self)
        btn1.move(480, 10)
        btn1.clicked.connect(self.btn1_clicked)

        ## UI 버튼 (정보 얻기)
        btn2 = QPushButton("정보 얻기", self)
        btn2.move(480, 50)
        btn2.clicked.connect(self.btn2_clicked)

        ## UI 버튼 (전체 정보 얻기)
        btn2 = QPushButton("정보 얻기", self)
        btn2.move(480, 50)
        btn2.clicked.connect(self.btn2_clicked)

        ## 이벤트
        self.kiwoom.OnEventConnect.connect(self.event_connect)

        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)



    def event_connect(self, err_code):
        #print(err_code)
        if err_code == 0:
            self.text_edit.append("로그인 성공")

    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next):
        if rqname == 'opt10082_req':
            nMaxRow = self.kiwoom.dynamicCall("GetRepeatCnt(QString, QString)", trcode, '주식주봉차트조회')
            #print (nMaxRow)
            data_array = self.kiwoom.dynamicCall("GetCommDataEx(QString, QString)", trcode, "주식주봉차트조회")
            print(screen_no, rqname, trcode, recordname, prev_next)
#            CSVFileIO.setCsv("E:\99.Coding\\18_D_Apple\Data\output.csv", data_array[1])

            for i in range(0, nMaxRow):
                CSVFileIO.setCsv("E:\99.Coding\\18_D_Apple\Data\csv\output_013580.csv", data_array[i])

    def btn1_clicked(self):
        print("없어")

    def btn2_clicked(self):
        #조회 프로시저
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '종목코드', "013580")
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '기준일자', '20181025')
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '끝일자', '20100101')
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '수정주가구분', '1')
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", 'opt10082_req', 'opt10082', '0', '0101')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())