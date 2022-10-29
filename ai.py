import sys
import requests
import json

# API 환경설정
client_id = "6dw6q9kwdt"
client_secret = "jSx5zUfdQAMKU2MrvQrPGwWm72LenRa0PKOtrN2j"

url="https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze"
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/json"
}

# 감정분석 할 문구 
content = "싸늘하다. 가슴에 비수가 날아와 꽂힌다."

data = {
    "content": content
}

json.dumps(data, indent=4, sort_keys=True)


# 통신이 정상적인지 확인하는 코드
response = requests.post(url, data=json.dumps(data), headers=headers)
rescode = response.status_code
if(rescode == 200):
    print (json.loads(response.text)['document'])
else:
    print("Error : " + response.text)