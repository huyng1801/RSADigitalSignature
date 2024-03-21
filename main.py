import sys
import rsa
import hashlib
import time
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow
from part1 import Ui_Bengui
from part2 import Ui_Mothongdiep
from part3 import Ui_Bennhan
from part4 import Ui_Form
class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_Bengui()
        self.uic.setupUi(self.main_win)
        self.main_win_2 = QMainWindow()
        self.uic_2 = Ui_Mothongdiep()
        self.uic_2.setupUi(self.main_win_2)
        self.main_win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.main_win.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.main_win_2.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.main_win_2.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.main_win_3 = QMainWindow()
        self.uic_3 = Ui_Bennhan()
        self.uic_3.setupUi(self.main_win_3)
        self.main_win_4 = QMainWindow()
        self.uic_4 = Ui_Form()
        self.uic_4.setupUi(self.main_win_4)
        self.main_win_3.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.main_win_3.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.main_win_4.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.main_win_4.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.uic.PBTudong.clicked.connect(lambda: self.tudong())
        self.uic.PBXoakhoa.clicked.connect(lambda: self.xoakhoa())
        self.uic.PBTinh.clicked.connect(lambda: self.tinh())
        self.uic.PBTaochuky.clicked.connect(lambda: self.taochuky())
        self.uic.PBXoachuky.clicked.connect(lambda: self.xoachuky())
        self.uic.PBGui.clicked.connect(lambda: self.gui())
        self.uic.PBThoat.clicked.connect(lambda: self.thoattaochuky())
        self.uic_2.PBCo.clicked.connect(lambda: self.co())
        self.uic_2.PBKhong.clicked.connect(lambda: self.khong())
        self.uic_3.PBThoat.clicked.connect(lambda: self.thoatthamdinhchuky())
        self.uic_3.PBQuaylai.clicked.connect(lambda: self.quaylai())
        self.uic_3.PBXacminh.clicked.connect(lambda: self.xacminh())
        self.uic_4.PBDong.clicked.connect(lambda: self.dong())
        self.url = QtCore.QUrl.fromLocalFile("button19.mp3")
        self.content = QtMultimedia.QMediaContent(self.url)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)
        self.player.play()
    def tudong(self):
        self.player.play()
        self.uic.TEChukyso.clear()
        self.uic.LEp.setText(str(rsa.choice_p()))
        self.uic.LEq.setText(str(rsa.choice_q()))
        self.uic.LEn.setText(str(int(self.uic.LEp.text())*int(self.uic.LEq.text())))
        self.uic.LEPn.setText(str((int(self.uic.LEp.text())-1)*(int(self.uic.LEq.text())-1)))
        self.uic.LEe.setText(str(rsa.choice_e(int(self.uic.LEPn.text()))))
        self.uic.LEd.setText(str(rsa.choice_d(int(self.uic.LEPn.text()), int(self.uic.LEe.text()))))
        self.uic.Lne.setText("(" + self.uic.LEn.text() + " " + "," + self.uic.LEe.text() + ")")
        self.uic.Lnd.setText("(" + self.uic.LEn.text() + " " + "," + self.uic.LEd.text() + ")")
    
    def dong(self):
        self.player.play()
        self.main_win_4.close()

    def thoattaochuky(self):
        self.player.play()
        time.sleep(1)
        self.main_win.close()
    def thoatthamdinhchuky(self):
        self.player.play()
        time.sleep(1)
        self.main_win_3.close()
    def quaylai(self):
        self.player.play()
        self.main_win_3.close()
        self.main_win.show()
    def tinh(self):
        self.player.play()
        if not self.uic.LEp.text():
            self.uic.LEp.setText(str(rsa.choice_p()))
        if not self.uic.LEq.text():
            self.uic.LEq.setText(str(rsa.choice_q()))
        if not self.uic.LEn.text():
            self.uic.LEn.setText(str(int(self.uic.LEp.text())*int(self.uic.LEq.text())))
        if not self.uic.LEPn.text():
            self.uic.LEPn.setText(str((int(self.uic.LEp.text())-1)*(int(self.uic.LEq.text())-1)))
        if not self.uic.LEe.text():
            self.uic.LEe.setText(str(rsa.choice_e(int(self.uic.LEPn.text()))))
        if not self.uic.LEd.text():
            self.uic.LEd.setText(str(rsa.choice_d(int(self.uic.LEPn.text()), int(self.uic.LEe.text()))))
        self.uic.Lne.setText("(" + self.uic.LEn.text() + " " + "," + self.uic.LEd.text() + ")")
        self.uic.Lnd.setText("(" + self.uic.LEn.text() + " " + "," + self.uic.LEe.text() + ")")  
    def xoakhoa(self):
        self.player.play()
        self.uic.LEp.clear()
        self.uic.LEq.clear() 
        self.uic.LEn.clear() 
        self.uic.LEPn.clear() 
        self.uic.LEe.clear() 
        self.uic.LEd.clear()
        self.uic.Lne.clear()
        self.uic.Lnd.clear()  
    def taochuky(self):
        self.player.play()
        if (self.uic.LEp.text() and self.uic.LEq.text() and self.uic.LEn.text()
            and self.uic.LEPn.text() and self.uic.LEe.text() and self.uic.LEd.text()):
                self.uic.LEMabamSHA1.setText(hashlib.sha1(self.uic.TEThongdiepdulieu.toPlainText().encode()).hexdigest())
                self.uic.TEChukyso.setText(rsa.en(int(self.uic.LEn.text()), int(self.uic.LEd.text()), self.uic.LEMabamSHA1.text()))
    
    def xoachuky(self):
        self.player.play()
        self.uic.TEThongdiepdulieu.clear()
        self.uic.TEChukyso.clear()
        self.uic.LEMabamSHA1.clear()
    
    
    def gui(self):
        self.player.play()
        if (self.uic.LEp.text() and self.uic.LEq.text() and self.uic.LEn.text()
            and self.uic.LEPn.text() and self.uic.LEd.text() and self.uic.TEChukyso.toPlainText() and self.uic.LEMabamSHA1.text()):
                self.main_win.close()
                self.main_win_2.show()
    def co(self):
        self.player.play()
        self.main_win_3.show()
        self.main_win_2.close()
        self.main_win.close()
        self.uic_3.TEThongdiepnhanduoc.setText(self.uic.TEThongdiepdulieu.toPlainText())
        self.uic_3.TEChukynhanduoc.setText(self.uic.TEChukyso.toPlainText())
    def khong(self):
        self.player.play()
        self.main_win_2.close()
        self.main_win.show()
            
    def xacminh(self):
        self.player.play()
        self.uic_3.TEMabamSHA1.setText(hashlib.sha1(self.uic_3.TEThongdiepnhanduoc.toPlainText().encode()).hexdigest())
        self.uic_3.TEGiaimachuky.setText(rsa.de(int(self.uic.LEn.text()), int(self.uic.LEe.text()), self.uic_3.TEChukynhanduoc.toPlainText()))
        if self.uic_3.TEMabamSHA1.toPlainText() == self.uic_3.TEGiaimachuky.toPlainText():
            self.uic_4.TBThongbao.setText("Thông điệp và chữ ký toàn vẹn dữ liệu")
        elif self.uic_3.TEGiaimachuky.toPlainText() == "Giải mã chữ ký không thành công!":
            self.uic_4.TBThongbao.setText("Thông điệp hoặc chữ ký đã bị thay đổi")
        else:
            self.uic_4.TBThongbao.setText("Thông điệp hoặc chữ ký đã bị thay đổi")
        self.main_win_4.show()
        
    def show(self):
        self.main_win.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
