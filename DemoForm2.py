# DemoForm.py

# Demoform.py(로직 코딩) + Demoform.ui(화면을 XML문서 저장)
import sys 
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#디자인 문서를 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]
#폼 클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")
    #슬롯메서드 
    def firstClick(self):
        url = "https://www.daangn.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        #파일에 저장
        f = open("daangn.txt", "wt", encoding="utf-8") #파일 생성
        for post in posts:
            title = post.find("h2", attrs={"class":"card-title"})
            price = post.find("div", attrs={"class":"card-price"})
            addr = post.find("div", attrs={"class":"card-region-name"})
            title = title.text.replace("\n", "") # 줄바꿈 제거
            price = price.text.replace("\n", "") # 줄바꿈 제거
            addr = addr.text.replace("\n", "") # 줄바꿈 제거
            print("{0},{1},{2}".format(title, price, addr))
            f.write(f"{title}, {price}, {addr}\n")  #파일에 내용쓰기

        f.close()

        self.label.setText("당근 마켓 크롤링 완료")
    def secondClick(self):
        self.label.setText("두번재 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번재 버튼을 클릭")
#모듈을 직접 실행했는지를 체크(진입점)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()