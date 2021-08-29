N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort() # 카드를 오름차순 정렬
sum_list = []
for x in range(-1, -len(cards)+1, -1): #뒤에서부터 3장을 한 장씩 보면서
    for y in range(x-1, -len(cards), -1):
        for z in range(y-1, -len(cards)-1, -1):
            if cards[x] + cards[y] + cards[z] <= M:
                sum_list.append(cards[x] + cards[y] + cards[z])

print(max(sum_list))