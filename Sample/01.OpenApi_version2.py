#-*- coding: utf-8 -*-
import sys
import time

TR_REQ_TIME_INTERVAL = 5


class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()

    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._event_connect)
        self.OnReceiveTrData.connect(self._receive_tr_data)

    def comm_connect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()



if __name__ == "__main__":

    kiwoom = Kiwoom()
    kiwoom.comm_connect()

    kiwoom.set_input_value("종목코드", "000660")
    kiwoom.comm_rq_data("opt10001_req", "opt10001", 0, "2000")