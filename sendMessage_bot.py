import requests


TOKEN = '1773022605:AAEQCLvDNGWwqjaouG53Dpf4pZzazT8GuJg'
APP_URL = f'https://api.telegram.org/bot{TOKEN}'

#응답 내용 저장하기
update_url = f'{APP_URL}/getUpdates'
response = requests.get(update_url).json()

#chat_id뽑아내기
chat_id = response['result'][0]['message']['chat']['id']

#print(chat_id)

text = '승훈님 별다방 아메리카노 당첨!'

message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(message_url)