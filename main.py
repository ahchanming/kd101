# coding:utf-8


import spider.kuaidi100
import threading
import json
import net.server
import time
from proto import request_pb2

fileInput = open("data/area.txt")
area_codes = []
start_codes = [121111, 350213, 320583]
company_codes = [4]

while True:
    strLine = fileInput.readline()
    if not strLine:
        break
    code = strLine.split(',')[0]
    area_codes.append(strLine[0: 6])
print("读取地区数据，数据总数为", len(area_codes))


def read_avg_from_kd100(area_codes, start_code, express_company, resultmap):
    print(str.format("准备从快递100爬取快递信息，开始地区为{}，快递公司编号为{}", start_code, express_company))
    result = []
    for end_code in area_codes:
        days = spider.kuaidi100.get_express_avg_days(express_company, start_code, end_code)
        print(days)
        if days != "None":
            result.append({'start': start_code, 'end': end_code, 'days': days})
    resultmap[(start_code, express_company)] = result


def dump2file(resultmap):
    while True:
        # time.sleep(3600)
        file_output = open("output.txt", "w")
        # data = {'data': resultmap, 'version': time.time()}
        file_output.write(json.dumps(resultmap))
        file_output.close()


def dump_data_from_kd100():
    threads = []
    result_map = {}
    for start in start_codes:
        for company_code in company_codes:
            print(str.format("创建从kd100读取线程，起始地址为{},快递公司为{}", start, company_code))
            th = threading.Thread(target=read_avg_from_kd100, args=[area_codes, start, company_code, result_map])
            threads.append(th)
    for each in threads:
        each.start()
        each.join()
    dump2file(result_map)


if __name__ == '__main__':
    net.server.start_host(9999)
    while True:
        client_socket, addr = net.server.accept()
        tmp_request = net.server.get_request(client_socket)
        print(tmp_request.type, tmp_request.expressCom, tmp_request.expressCode)
        client_socket.send("HelloWorld".encode("utf-8"))
        client_socket.close()
