import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class pracWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        
        VBox = QVBoxLayout()
        
        hbox1 = QHBoxLayout()
        self.imageLable = QLabel(self)
        hbox1.addWidget(self.imageLable)
        
        hbox2 = QHBoxLayout()
        self.bt1 = QPushButton('Image 1',self)
        self.bt2 = QPushButton('Image 2',self)
        self.bt3 = QPushButton('Image 3',self)
        self.bt1.clicked.connect(lambda: self.Img('/Users/leegg/Documents/IoT개발자과정/Pythonprac/123.jpeg'))
        self.bt2.clicked.connect(lambda: self.Img('/Users/leegg/Documents/IoT개발자과정/Pythonprac/111.jpeg'))
        self.bt3.clicked.connect(lambda: self.Img('/Users/leegg/Documents/IoT개발자과정/Pythonprac/222.jpeg'))
        hbox2.addWidget(self.bt1)
        hbox2.addWidget(self.bt2)
        hbox2.addWidget(self.bt3)
        
        
        VBox.addLayout(hbox1)
        VBox.addLayout(hbox2)
        
        
        self.setLayout(VBox)
        
            
        self.setGeometry(300, 300, 300, 300)  # 창 크기 설정
        self.setWindowTitle('')  # 이름
        self.show()
    
    def Img(self,Path):
        pixmap = QPixmap(Path)
        self.imageLable.setPixmap(pixmap)
        self.imageLable.adjustSize()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = pracWidget()
    sys.exit(app.exec_())
