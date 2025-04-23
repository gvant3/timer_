from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer
app = QApplication([])
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
    lb_sec.setText(str(sec))
rebtn.clicked.connect(delete_sec)

sec2 = 0

win_t = QWidget()
win_t.setWindowTitle("Таймер")
win_t.resize(400, 200)
layo_tim1 = QVBoxLayout()
win_t.setLayout(layo_tim1)
secbtn = QPushButton("Секундомер")
layo_tim1.addWidget(secbtn)
stmbtn = QPushButton("Старт")
layo_tim1.addWidget(stmbtn)
sttmbtn = QPushButton("пауза")
layo_tim1.addWidget(sttmbtn)
resbtn = QPushButton("Обновити")
layo_tim1.addWidget(resbtn)
addsec = QPushButton("Добавитити секунду")
layo_tim1.addWidget(addsec)
addmin = QPushButton("Добавити хвилину")
layo_tim1.addWidget(addmin)
minussec = QPushButton("відняти секунду")
layo_tim1.addWidget(minussec)
minmin = QPushButton("відняти хвилину")
layo_tim1.addWidget(minmin)
layo_sec1 = QVBoxLayout()
lb_sec1 = QLabel("0")
layo_tim1.addWidget(lb_sec1)






def tim_show():
    time.stop()
    win_t.show()
    win_s.hide()
timbtn.clicked.connect(tim_show)
def tim_hide():
    win_t.hide()
    win_s.show()
secbtn.clicked.connect(tim_hide)

def add_sec():
    global sec2
    sec2 += 1
    lb_sec1.setText(str(sec2))
addsec.clicked.connect(add_sec)
def minus_sec():    
    global sec2
    sec2 -= 1
    if sec2 <= 0:
        sec2 = 0
    lb_sec1.setText(str(sec2))   
minussec.clicked.connect(minus_sec)
def update_tim():
    global sec2
    sec2 -= 1
    lb_sec1.setText(str(sec2))
    if sec2 <= 0:
        sec2 = 0
        time.stop()
time.timeout.connect(update_tim)
def start_tim():
    time.start(1000)
stmbtn.clicked.connect(start_tim)
def stop_tim():
    time.stop() 
sttmbtn.clicked.connect(stop_tim)

def reset_tim():
    global sec2
    sec2 = 0
    lb_sec1.setText(str(sec2))
    time.stop()
resbtn.clicked.connect(reset_tim)

def add_min():
    global sec2
    sec2 += 60
    lb_sec1.setText(str(sec2))
addmin.clicked.connect(add_min)

def minus_min():
    global sec2
    sec2 -= 60
    if sec2 <= 0:
        sec2 = 0
    lb_sec1.setText(str(sec2))
minmin.clicked.connect(minus_min)










win_s.show()
app.exec_()  




win_s.show()
app.exec_()  
