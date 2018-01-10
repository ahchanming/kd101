import urllib3
import urllib.request
import json

def get_express_detail(express_code, express_company):
    url = "http://www.kuaidi100.com/query?type=ems&postid=1003030947526&temp=0.31044663555669105"
    dict = {}
    dict['type'] = express_company
    dict['postid'] = express_code
    httpclient = urllib3.PoolManager()
    r = httpclient.request('GET', url)
    response = urllib.request.urlopen(url);
    #response = json.load(r.read())
    #print(response)
    print(response.read().decode("utf-8"))

get_express_detail("1003030947526", "ems")
