import urllib.request
import json
import re


def get_express_detail(express_code, express_company):
    #url = "http://www.kuaidi100.com/query?type=yuantong&postid=812553308147"
    url = str.format("http://www.kuaidi100.com/query?type={}&postid={}", express_company, express_code)
    print(str.format("请求快递100，查询物流轨迹，url为{}", url))
    proxy = {}
    #proxy = {"http": "116.52.78.192:9999"}
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    # response = json.load(r.read())
    # print(response)
    return response.read().decode("utf-8")


def get_express_avg_days(express_company, start_code, end_code):
    url = "https://www.kuaidi100.com/time/comtimecostinfo_" + str(express_company) + "_CN" + str(
        start_code) + "_CN" + str(end_code) + ".htm?"
    try:
        response = urllib.request.urlopen(url, timeout=1)
        responseStr = response.read().decode("utf-8")
        index = responseStr.find("天 </td>")
        subStr = responseStr[index - 20: index]
        pattern = re.compile('[1-9]\d*.\d*|0.\d*[1-9]\d*')
        result = pattern.search(subStr)
        if (result == None):
            return "None"
        return result.group(0)
    except:
        return "None"


#get_express_detail("", "")