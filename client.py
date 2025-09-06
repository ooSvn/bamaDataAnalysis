from pydoc import cli
import requests as rq
from bs4 import BeautifulSoup
import json
import re
import socket
ses = rq.Session()

res = ses.get("http://utproject.ir/bp/Cars/page0.php")
res2 = ses.post("http://utproject.ir/bp/login.php",data={"username": "610300104","password": "97282481661656142055"})
max_lenth = 4
port = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', port))

print(f"connected to server {sock.getpeername()}")
pattern = re.compile(r'https://bama.ir/car/detail-(.+)')
patternFunc = re.compile(r'[0-9]+,[0-9]+')

class client:
    def __init__(self):
        self.run()

    def run(self):
        for i in range(500):
            res = ses.get(f"http://utproject.ir/bp/Cars/page{i}.php")
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text,'html.parser')
            carSigns = soup.find_all('li',class_='car-list-item-li list-data-main')
            self.send_signCount(carSigns)
            for carSign in carSigns:
                lilData = dict()
                # company, model, year, tream
                href = carSign.find('span',class_='photo')
                l = pattern.findall(str(href.a['href']))[0]
                details = re.split(r'-',l)
                lilData['company'] = details.pop(1)
                lilData['model'] = details.pop(1)
                lilData['year'] = details.pop(-1)
                # print(details)
                if len(details) >= 2:
                    lilData['tream'] = " ".join(details[1:])
                else:
                    lilData['tream'] = ''
                # cost
                if carSign.find('p', class_="cost installment-cost"):
                    lilData['price'] = 1
                else:
                    try:
                        cost = carSign.find('p', class_='cost')
                        lilData['price'] = int(cost.span['content'])
                    except ValueError:
                        lilData['price'] = 0
                # func
                func = carSign.find('div', class_="car-func-details")
                if patternFunc.findall(str(func.span.text)):
                    funcMass = patternFunc.findall(str(func.span.text))[0]
                    funcMass = funcMass.replace(",","")
                    lilData['kilometer'] = int(funcMass)
                else:
                    lilData['kilometer'] = int(0)
                self.sendMessage(lilData)
            self.giveMessage()
                
    def sendMessage(self,dic):
        json_obj = json.dumps(dic)
        max_lenth = str(len(json_obj)).ljust(5)
        sock.send(max_lenth.encode())
        sock.send(json_obj.encode())
    
    def giveMessage(self):
        max_lenth = int(sock.recv(5).decode())
        json_obj = sock.recv(max_lenth).decode()
        with open('file.txt','a') as file:
            file.write(json_obj)
            file.write('\n')

    def send_signCount(self,carSigns):
        lenth = str(len(carSigns)).ljust(3)
        sock.send(lenth.encode())

start = client()

# 97282481661656142055
# model haye cars
# sherkat haye sazande
# sale tolid
# karkard(meqdare kilo meter)
# qeimat ha