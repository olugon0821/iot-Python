import sys
from PyQt5.QtWidgets import QHBoxLayout,QPushButton,QApplication,QWidget,QVBoxLayout,QLineEdit,QLabel

class pracWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        vbox = QVBoxLayout() # main box 생성
        
        self.label1 = QLabel('안녕하세요', self)
        self.label1.hide()
        label2 = QLabel('출력 : ', self)
        self.label3 = QLabel('', self)
        
        self.qle1 = QLineEdit(self)
        
        hbox1 = QHBoxLayout() # hbox1 생성  
        self.b1 = QPushButton('B1', self) # 버튼 생성
        self.b2 = QPushButton('B2', self)
        self.b1.clicked.connect(self.Print1)
        self.b2.clicked.connect(self.label_show)
        hbox1.addWidget(self.b1)
        hbox1.addWidget(self.b2)# 버튼 배치
        
        hbox2 = QHBoxLayout() # hbox2 생성
        hbox2.addWidget(self.label1)
        hbox2.addWidget(self.qle1)
        hbox2.addWidget(label2)
        hbox2.addWidget(self.label3)
        
        
        
        vbox.addLayout(hbox2) # box를 수직으로 배치
        vbox.addLayout(hbox1)

        self.setLayout(vbox)  

        self.setGeometry(300, 300, 300, 200)  # 창 크기 설정
        self.setWindowTitle('box')  # 이름
        self.show()
       
        
    def Print1(self):
        P1 = self.qle1.text()
        result1 = P1
        self.label3.setText(str(result1))
    
    def label_show(self):
        self.label1.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = pracWidget()
    sys.exit(app.exec_())
