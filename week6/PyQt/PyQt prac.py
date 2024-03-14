import sys
from PyQt5.QtWidgets import QHBoxLayout,QPushButton,QApplication,QWidget,QVBoxLayout

class pracWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        vbox = QVBoxLayout() 
        
        hbox1 = QHBoxLayout()  
        b1 = QPushButton('B1', self) 
        b2 = QPushButton('B2', self) 
        hbox1.addWidget(b1) 
        hbox1.addWidget(b2) 

        hbox2 = QHBoxLayout() 
        b3 = QPushButton('B3', self) 
        b4 = QPushButton('B4', self)  
        hbox2.addWidget(b3)  
        hbox2.addWidget(b4)  

        vbox.addLayout(hbox1)  
        vbox.addLayout(hbox2)  

        self.setLayout(vbox)  

        self.setGeometry(300, 300, 300, 200)  
        self.setWindowTitle('box')  
        self.show()  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = pracWidget()
    sys.exit(app.exec_())
