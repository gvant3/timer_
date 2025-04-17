from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer
app = QApplication([])
#вікно с секундомером
win_s = QWidget()
win_s.setWindowTitle("Секундомер")
win_s.resize(200, 200)
#лайоут де буде все що буде с секундомером
layo_sec = QVBoxLayout()
win_s.setLayout(layo_sec)
#напис секунд
lb_sec = QLabel("0")
layo_sec.addWidget(lb_sec)
#кнопка старт
sbtn = QPushButton("Старт")
layo_sec.addWidget(sbtn)
#кнопка стоп
stbtn = QPushButton("Стоп")
layo_sec.addWidget(stbtn)
#кнопка обновити
rebtn = QPushButton("Обновити")
layo_sec.addWidget(rebtn)
#лайоут у якому буде кнопка для переключення на таймер
layo_tim = QVBoxLayout()
layo_sec.addLayout(layo_tim)
#кнопка для переключення на таймер
timbtn = QPushButton("Таймер")
layo_tim.addWidget(timbtn)
#QTimer який стартуе рахування та змінна для рахування секунд (тому що другий 0 у нас str а щоб рахувати треба int)
time = QTimer()
sec = 0
#рахування секунд
def update_sec():
    global sec
    sec += 1
    lb_sec.setText(str(sec))
time.timeout.connect(update_sec)
#початок рахування
def start_sec():
    #швидкість рахування в мс
    time.start(1000)  
sbtn.clicked.connect(start_sec)
#стоп рахування
def stop_sec():
    time.stop()
stbtn.clicked.connect(stop_sec)
#оновлення таймеру
def delete_sec():
    global sec
    sec *= 0
    time.stop()
    lb_sec.setText(str(sec))
rebtn.clicked.connect(delete_sec)
#вікно з таймером
win_t = QWidget()
win_t.setWindowTitle("Таймер")
win_t.resize(200, 200)
#лайоут у якому буде усе що потрібно для таймеру
layo_tim1 = QVBoxLayout()
win_t.setLayout(layo_tim1)
#кнопка яка буде переключати назад на секундомер
secbtn = QPushButton("Секундомер")
layo_tim1.addWidget(secbtn)
#добавлення вікна с таймером та приховання вікна с секундомером
def tim_show():
    time.stop()
    win_t.show()
    win_s.hide()
timbtn.clicked.connect(tim_show)
#добавлення вікна с секундомером та приховання вікна с таймером
def tim_hide():
    win_t.hide()
    win_s.show()
secbtn.clicked.connect(tim_hide)




win_s.show()
app.exec_()  
