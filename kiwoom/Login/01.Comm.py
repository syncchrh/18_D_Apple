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
        btnStockNumber = QPushButton("종목코드 얻기", self)
        btnStockNumber.move(480, 10)
        btnStockNumber.clicked.connect(self.btnStockNumber_clicked)

        ## UI 버튼 (정보 얻기)
        btnGetInformationSingle = QPushButton("단일 정보 얻기", self)
        btnGetInformationSingle.move(480, 90)
        btnGetInformationSingle.clicked.connect(self.btnGetInformationSingle_clicked)

        ## UI 버튼 (정보 얻기)
        btnGetInformation = QPushButton("정보 얻기", self)
        btnGetInformation.move(480, 50)
        btnGetInformation.clicked.connect(self.btnGetInformation_clicked)

        ## UI 버튼 (전체 정보 얻기)
        btnGetInformationAll = QPushButton("전체 정보 얻기", self)
        btnGetInformationAll.move(480, 50)
        btnGetInformationAll.clicked.connect(self.btnGetInformationAll_clicked)

        ## 이벤트
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)
        #self.kiwoom.OnReceiveRealData.connect(self.receive_realData)


    def event_connect(self, err_code):
        #print(err_code)
        if err_code == 0:
            self.text_edit.append("로그인 성공")

    # def receive_realData(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
    #     if rqname == 'opt10001_req':
    #         name = self.kiwoom.dynamicCall("CommGetRealData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
    #         volume = self.kiwoom.dynamicCall("CommGetRealData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")
    #         currentPrice = self.kiwoom.dynamicCall("CommGetRealData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "현재가")
    #         PER = self.kiwoom.dynamicCall("CommGetRealData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "PER")
    #         EPS = self.kiwoom.dynamicCall("CommGetRealData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "EPS")
    #         ROE = self.kiwoom.dynamicCall("CommGetRealData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "ROE")
    #         PBR = self.kiwoom.dynamicCall("CommGetRealData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "PBR")
    #         EV = self.kiwoom.dynamicCall("CommGetRealData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "EV")
    #         BPS = self.kiwoom.dynamicCall("CommGetRealData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "BPS")
    #
    #         information = [name.strip(), volume.strip(), currentPrice.strip(), PER.strip(), EPS.strip(), ROE.strip(), PBR.strip(), EV.strip(), BPS.strip()]
    #         #for i in information:
    #         CSVFileIO.setCsv("E:\99.Coding\\18_D_Apple\Data\csv\\baseInformationKospi.csv", information)
    #
    #         print("저장완료")
    #         time.sleep(1)

    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        if rqname == 'opt10001_req':
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
            code = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목코드")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")
            currentPrice = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "현재가")
            PER = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "PER")
            EPS = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "EPS")
            ROE = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "ROE")
            PBR = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "PBR")
            EV = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0,  "EV")
            BPS = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "BPS")
            salesAccount = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "매출액")
            operatingProfit = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "영업이익")
            perProfit = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "당기순이익")
            total = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "시가총액")

            information = [code.strip(), name.strip(), volume.strip(), currentPrice.strip(), PER.strip(), EPS.strip(), ROE.strip(), PBR.strip(), EV.strip(), BPS.strip(), salesAccount.strip(), operatingProfit.strip(), perProfit.strip(), total.strip()]

#            for i in information:
            CSVFileIO.setCsv("E:\99.Coding\\18_D_Apple\Data\csv\\baseInformationKosdaq.csv", information)

            print("저장완료")
            time.sleep(1)


        elif rqname == 'opt10005_req':
            date = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "날짜")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")
            temp = self.kiwoom.dynamicCall("GetCommDataEx(QString, QString)", trcode, "주식일주월시분")
            print(temp)

        #elif rqname == 'opt10081_req':
        #    kospi_list = []
        #    for i in range(1, 11):
        #        date = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, i, "일자")
        #        volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, i, "현재가")
        #        #print("날짜: " + date.strip() + " 현재가: " + volume.strip())
        #        kospi_list.append(date.split(',') + volume.split(','))
        #    print(kospi_list)

        elif rqname == 'opt10082_req':
            nMaxRow = self.kiwoom.dynamicCall("CommRepeatCnt(QString, QString, QString)", trcode, rqname)
            temp = self.kiwoom.dynamicCall("GetCommDataEx(QString, QString)", trcode, "주식주봉차트조회")
            print(temp)
            CSVFileIO.setCsv("E:\99.Coding\\18_D_Apple\Data\output.csv", temp)

        elif rqname == 'opt10086_req':
            nMaxRow = self.kiwoom.dynamicCall("CommRepeatCnt(QString, QString, QString)", trcode, rqname)
            temp = self.kiwoom.dynamicCall("GetCommDataEx(QString, QString)", trcode, "일별주가")
            print(temp)
            CSVFileIO.setCsv("E:\99.Coding\\18_D_Apple\Data\output.csv", temp)

    #단일 종목 정보 얻기
    def btnGetInformationSingle_clicked(self):
        x = "018000";
        name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)", [x])
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '종목코드', x)
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", 'opt10001_req', 'opt10001', '0', '0101')


    ##전체 종목 정보 얻기
    def btnGetInformationAll_clicked(self):
        getCodeList = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", ["10"])
        kospi_code_list = getCodeList.split(';')
        print(kospi_code_list)

        # 전체 종목 데이터 요청
        for x in kospi_code_list:
            self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '종목코드', x)
            self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", 'opt10001_req', 'opt10001', '0','0101')

        # #뒷부분 짤린거
        # index = kospi_code_list.index("206560")
        # length = len(kospi_code_list)
        #
        # for i in range(index, length):
        #     self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '종목코드', kospi_code_list[i])
        #     self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", 'opt10001_req', 'opt10001', '0','0101')

    def btnStockNumber_clicked(self):
        ret = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", ["0"])
        kospi_code_list = ret.split(';')
        kospi_code_name_list = []

        # for x in kospi_code_list:
        #     name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)", [x])
        #     self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '종목코드', x)
        #     self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", 'opt10001_req', 'opt10001', '0', '0101')
        #     time.sleep(1)
        #     kospi_code_name_list.append(x + " : " + name)

        self.listWidget.addItems(kospi_code_name_list)

    def btnGetInformation_clicked(self):
        #조회 프로시저
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '종목코드', '017800')
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '조회일자', '20180320')
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", '표시구분', '0')

        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", 'opt10082_req', 'opt10082', '0', '0101')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())