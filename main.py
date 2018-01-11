#coding:utf-8


import spider.kuaidi100
import json

print (spider.kuaidi100.get_express_avg_days(1, 350213, 440515))


fileInput = open("area.txt")
while True:
    str = fileInput.readline()
    if not str:
        break
    code = fileInput.readline().split(',')[0]
    print(code[0:6] + "," + spider.kuaidi100.get_express_avg_days(1, 320583, code[0:6]))

