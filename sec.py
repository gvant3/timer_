from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer
app = QApplication([])
from tim import *
win_s = QWidget()
win_s.setWindowTitle("Секундомер")
win_s.resize(200, 200)
layo_sec = QVBoxLayout()
win_s.setLayout(layo_sec)
lb_sec = QLabel("0")
layo_sec.addWidget(lb_sec)
sbtn = QPushButton("Старт")
layo_sec.addWidget(sbtn)
stbtn = QPushButton("Стоп")
layo_sec.addWidget(stbtn)
rebtn = QPushButton("Обновити")
layo_sec.addWidget(rebtn)
layo_tim = QVBoxLayout()
layo_sec.addLayout(layo_tim)
timbtn = QPushButton("Таймер")
layo_tim.addWidget(timbtn)
time = QTimer()
sec = 0
def update_sec():
    global sec
    sec += 1
    lb_sec.setText(str(sec))
time.timeout.connect(update_sec)
def start_sec():
    time.start(1000)  
sbtn.clicked.connect(start_sec)
def stop_sec():
    time.stop()
stbtn.clicked.connect(stop_sec)
def delete_sec():
    global sec
    sec *= 0
    time.stop()
rebtn.clicked.connect(delete_sec)

win_t = QWidget()
win_t.setWindowTitle("Таймер")
win_t.resize(200, 200)
layo_tim1 = QVBoxLayout()
win_t.setLayout(layo_tim1)
secbtn = QPushButton("Секундомер")
layo_tim1.addWidget(secbtn)
def tim_show():
    time.stop()
    win_t.show()
    win_s.hide()
timbtn.clicked.connect(tim_show)
def tim_hide():
    win_t.hide()
    win_s.show()
secbtn.clicked.connect(tim_hide)




win_s.show()
app.exec_()  
