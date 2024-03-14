import sys
from PyQt5.QtWidgets import QHBoxLayout,QPushButton,QApplication,QWidget,QVBoxLayout,QLineEdit,QLabel

class pracWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        vbox = QVBoxLayout() # main box 생성
        
        label1 = QLabel('*', self) # label값
        label2 = QLabel('=', self)
        self.label3 = QLabel('', self) # Multiple 결과값 출력
        
        self.qle1 = QLineEdit(self)
        self.qle2 = QLineEdit(self)
        
        hbox1 = QHBoxLayout() # hbox1 생성  
        self.b1 = QPushButton('B1', self) # 버튼 생성
        self.b1.clicked.connect(self.Multiple) # 버튼 클릭시 결과 출력
        
        hbox1.addWidget(self.b1) # 버튼 배치
        
        hbox2 = QHBoxLayout() # hbox2 생성
        hbox2.addWidget(self.qle1) # label,LineEdit 배치
        hbox2.addWidget(label1)
        hbox2.addWidget(self.qle2)
        hbox2.addWidget(label2)
        hbox2.addWidget(self.label3)
        
        
        vbox.addLayout(hbox2) # box를 수직으로 배치
        vbox.addLayout(hbox1)

        self.setLayout(vbox)  

        self.setGeometry(300, 300, 300, 200)  # 창 크기 설정
        self.setWindowTitle('box')  # 이름
        self.show()
        
    def Multiple(self): # 입력된 숫자 계산
   N1 = int(self.qle1.text())
   N2 = int(self.qle2.text())
   result = N1 * N2
   self.label3.setText(str(result)) # label3에 결과값 적용
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = pracWidget()
    sys.exit(app.exec_())
