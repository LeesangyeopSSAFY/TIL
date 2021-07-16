import requests

key = 'Vl8zyXtKLMGpkWvvqrqDwZxzxNb52Q2MDP5ezLGR2hgd%2FuzC9UTO4sPBRlG0IX87ZXOF2QwamXGOsAn8LDIKWw%3D%3D'
local = '제주'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={local}&returnType=json'
result = requests.get(url).json()

pm_10_Value = result['response']['body']['items'][0]['pm10Value']
print(pm_10_Value)