# DemoForm.py

# Demoform.py(로직 코딩) + Demoform.ui(화면을 XML문서 저장)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#디자인 문서를 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]
#윈도우 클래스 정의
class DemoForm(QDialog, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")
#모듈을 직접 실행했는지를 체크(진입점)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()