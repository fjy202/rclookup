import requests
from sys import exit
import json

#settings
base="https://sffc.sh-service.com/wx_miniprogram/sites/feiguan/trashTypes_2/Handler/Handler.ashx?a=GET_KEYWORDS&kw=%s"

def getResultDict(kw):
    json_=requests.get(base%kw).text
    return json.loads(json_)
def main():
    while 1:
        x=input("> ")
        if x=="":
            continue
        result=getResultDict(x) if x!="exit" else exit()
        if result["kw_arr"]!=None:
            for x in result["kw_arr"]:
                print(x["Name"]+":"+x["TypeKey"]+"\n"+x["Note"])
        else:
            print("找不到。")
if __name__=="__main__":
    main()