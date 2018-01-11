import urllib.request
import json
import re

def get_express_detail(express_code, express_company):
    url = "https://www.kuaidi100.com/time/comtimecostinfo_5_CN350213_CN440515.htm?"
    dict = {}
    dict['type'] = express_company
    dict['postid'] = express_code
    response = urllib.request.urlopen(url);
    #response = json.load(r.read())
    #print(response)
    print(response.read().decode("utf-8"))


def get_express_avg_days(express_company, start_code, end_code):
    url = "https://www.kuaidi100.com/time/comtimecostinfo_4_CN" + str (start_code) + "_CN" + str(end_code) + ".htm?"
    try:
        response = urllib.request.urlopen(url);
        responseStr = response.read().decode("utf-8")
        index = responseStr.find("天 </td>")
        subStr = responseStr[index - 20 : index]
        #print(responseStr[index - 20 : index])
        pattern = re.compile('[1-9]\d*.\d*|0.\d*[1-9]\d*')
        result = pattern.search(subStr)
        if (result == None):
            return "None"
        return pattern.search(subStr).group(0)
    except:
        return "None"

