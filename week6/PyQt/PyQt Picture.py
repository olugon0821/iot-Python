import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class pracWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        
        self.bt1 = QPushButton('출력',self)
        self.imageLable = QLabel(self)
        
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.bt1)
        vbox.addWidget(self.imageLable)
        self.setLayout(vbox)
        
        self.bt1.clicked.connect(lambda: self.Img('/Users/leegg/Documents/IoT개발자과정/Pythonprac/123.jpeg'))
            
        self.setGeometry(0, 0, 300, 300)  # 창 크기 설정
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
