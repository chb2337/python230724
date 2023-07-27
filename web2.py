# web2.py
#웹서버와 통신
import requests
#크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
posts = soup.find_all("div", attrs={"class":"card-desc"})
#파일에 저장
f = open("c:\\work\\daangn.txt", "wt", encoding="utf-8") #파일 생성
for post in posts:
    title = post.find("h2", attrs={"class":"card-title"})
    price = post.find("div", attrs={"class":"card-price"})
    addr = post.find("div", attrs={"class":"card-region-name"})
    title = title.text.replace("\n", "") # 줄바꿈 제거
    price = price.text.replace("\n", "") # 줄바꿈 제거
    addr = addr.text.replace("\n", "") # 줄바꿈 제거
    print("{0},{1},{2}".format(title, price, addr))
    f.write(f"{title}, {price}, {addr}\n")  #파일에 내용쓰기

f.close() #작업완료후 파일 닫기 txt

# <div class="card-desc">
#       <h2 class="card-title">먹태깡 60봉</h2>
#       <div class="card-price ">
#         1,500원
#       </div>
#       <div class="card-region-name">
#         경기도 김포시 장기동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 19
#           </span>
#         ∙
#         <span>
#             채팅 30
#           </span>
#       </div>
#     </div>