import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class pracWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        CB = QCheckBox('Try Check',self)
        CB.move(20,20)
        CB.toggle()
        CB.stateChanged.connect(self.Print)

        self.setGeometry(300, 300, 300, 200)  # 창 크기 설정
        self.setWindowTitle('')  # 이름
        self.show()
        
    def Print(self,check):
        if check == Qt.Checked:
            print('Checked')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = pracWidget()
    sys.exit(app.exec_())
