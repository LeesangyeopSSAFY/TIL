from itertools import combinations

OTT = [900, 850]
fee = [350, 300, 300, 250, 200]

bigList = [
    [1, 1.2, 1.5, 1.8, 1],
    [1.2, 1, 0.7, 1.1, 2],
    [1.5, 0.7, 1, 1.7, 1.8],
    [1.8, 1.1, 1.7, 1, 2],
    [1, 2, 1.8, 2, 1]
]

actors = [2, 2, 2, 2, 2]
combi = list(combinations([0, 1, 2, 3, 4], 3))

synergyList = []
feeList = []
for tmp in combi:
    synergy = 1
    total = 0
    for i in tmp:
        total += fee[i]
    feeList.append(total)

    for i in range(2):
        for j in range(i+1, len(tmp)):
            synergy *= bigList[tmp[i]][tmp[j]]

    synergyList.append(synergy)

# print(combi)
# print(feeList)
# print(synergyList)
maxi_list = []
actor_list = []
for production_cost in OTT:
    max_synergy = 0
    best_combi = []
    for i in range(len(combi)):
        possible = 1
        if feeList[i] <= production_cost:
            for j in range(len(combi[i])):
                if actors[combi[i][j]] == 0:
                    possible = 0

        if possible == 0:
            continue
        if feeList[i] <= production_cost and synergyList[i] > max_synergy:
            max_synergy = synergyList[i]
            best_combi = combi[i]
    actor_list.append(best_combi)
