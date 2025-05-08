import requests
import json

# 모집공고
def get_recruitment_notice():

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd", 
        "Accept-Language": "ko,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "74",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "WL_PCID=17464413246217491680114; JSESSIONID=5F38014256842E87F249B0695A53FF2A; _ga_KPFHM49NRN=GS2.1.s1746710175$o2$g0$t1746710175$j0$l0$h0; _ga=GA1.3.1746424900.1746441325; _gid=GA1.3.435384688.1746710176; _gat_gtag_UA_222727054_1=1",
        "Host": "soco.seoul.go.kr",
        "Origin": "https://soco.seoul.go.kr",
        "Referer": "https://soco.seoul.go.kr/youth/bbs/BMSR00015/list.do?menuNo=400008",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors", 
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }

    data = {
        "bbsId": "BMSR00015",
        "pageIndex": 2,
        "searchAdresGu": "",
        "searchCondition": "",
        "searchKeyword": ""
    }

    url = "https://soco.seoul.go.kr/youth/pgm/home/yohome/bbsListJson.json"

    response = requests.post(url, headers=headers, data=data)
    data = json.loads(response.text)['resultList']
    
    return data