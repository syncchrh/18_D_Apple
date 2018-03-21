#-*- coding: utf-8 -*-
#로그인 이벤트 처리하기

import sys, threading, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *
from Module_Sseung import CSVFileIO



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

    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        if rqname == 'opt10001_req':
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")
            currentPrice = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "현재가")

            print("종목명: " + name.strip())
            print("거래량: " + volume.strip())
            print("현재가: " + currentPrice.strip())
            #self.text_edit.append("종목명: " + name.strip())
            #self.text_edit.append("거래량: " + volume.strip())

        elif rqname == 'opt10005_req':
            date = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "날짜")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")

            print("날짜: " + date.strip())
            print("거래량: " + volume.strip())

        #elif rqname == 'opt10081_req':
        #    kospi_list = []
        #    for i in range(1, 11):
        #        date = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, i, "일자")
        #        volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, i, "현재가")
        #        #print("날짜: " + date.strip() + " 현재가: " + volume.strip())
        #        kospi_list.append(date.split(',') + volume.split(','))
        #    print(kospi_list)

        elif rqname == 'opt10081_req':
            nMaxRow = self.kiwoom.dynamicCall("CommRepeatCnt(QString, QString, QString)", trcode, rqname)
            temp = self.kiwoom.dynamicCall("GetCommDataEx(QString, QString)", trcode, "주식일봉차트조회")
            print(temp)
            CSVFileIO.setCsv("E:\99.Coding\\18_D_Apple\Data\output.csv", temp)


    def btn1_clicked(self):
        ret = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", ["0"])
        kospi_code_list = ret.split(';')
        kospi_code_name_list = []

        for x in kospi_code_list:
            name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)", [x])
            self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '종목코드', x)
            self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", 'opt10001_req', 'opt10001', '0', '0101')
            time.sleep(1)
            kospi_code_name_list.append(x + " : " + name)

        self.listWidget.addItems(kospi_code_name_list)

    def btn2_clicked(self):
        #조회 프로시저
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '종목코드', '017800')
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '기준일자', '20180320')
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '수정주가구분', '0')

        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", 'opt10081_req', 'opt10081', '0', '0101')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())