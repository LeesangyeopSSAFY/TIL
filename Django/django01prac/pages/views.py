import requests
import random
from django.shortcuts import render


# Create your views here.
def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'
    response = requests.get(url)
    lotto = response.json()

    winner = []
    bonus = lotto['bnusNo']
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    win_rate = {
        '1등': 0,
        '2등': 0,
        '3등': 0,
        '4등': 0,
        '5등': 0,
        '꽝': 0,
    }

    for i in range(1000):
        my_nums = random.sample(range(1, 46), 6)
        match = 0
        for n in my_nums:
            if n in winner:
                match += 1
        
        if match == 6:
            win_rate['1등'] += 1
        elif match == 5 and bonus in my_nums:
            win_rate['2등'] += 1
        elif match == 5:
            win_rate['3등'] += 1
        elif match == 4:
            win_rate['4등'] += 1
        elif match == 3:
            win_rate['5등'] += 1
        else:
            win_rate['꽝'] += 1
    
    context = {
        'winner': winner,
        'bonus': bonus,
        'win_rate': win_rate,
    }

    return render(request, 'pages/lotto.html', context)