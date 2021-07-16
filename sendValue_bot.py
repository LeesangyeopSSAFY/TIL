import requests

TOKEN = '1773022605:AAEQCLvDNGWwqjaouG53Dpf4pZzazT8GuJg'
APP_URL = f'https://api.telegram.org/bot{TOKEN}'
key = 'Vl8zyXtKLMGpkWvvqrqDwZxzxNb52Q2MDP5ezLGR2hgd%2FuzC9UTO4sPBRlG0IX87ZXOF2QwamXGOsAn8LDIKWw%3D%3D'
local = '울산'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={local}&returnType=json'


update_url = f'{APP_URL}/getUpdates'
response = requests.get(update_url).json()
result = requests.get(url).json()


chat_id = response['result'][0]['message']['chat']['id']
pm_10_Value = result['response']['body']['items'][0]['pm10Value']
stationName = result['response']['body']['items'][0]['stationName']

message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={local} {stationName}의 미세먼지 농도는 {pm_10_Value}입니다.'

requests.get(message_url)
