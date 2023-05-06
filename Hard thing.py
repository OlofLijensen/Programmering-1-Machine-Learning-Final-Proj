flat_list = [0.52, 1, 0.47, 0, 0.62 , 1, 0.7, 0, 0.8, 1]

Distances_worth = []
procent_list = []
changing_list = []
tot = 0
x = 0
y = 1

for elements in flat_list:
    worth = 1 * 0.25 ** flat_list[x]
    Distances_worth.append(worth)
    x += 2
    tot += worth
    print("here1")
    if x == 10:
        x = 0
        for elements in Distances_worth:
            worth = Distances_worth[x] / tot
            procent_list.append(worth)
            x += 1
            if x == 5:
                x = 0
                for elements in flat_list:
                    print("here2")
                    if x == 5 or y == 11:
                        x = 0
                        y = 0
                        print(changing_list)
                        changing_list = []
                        break

                    elif flat_list[y] == 0:
                        worth = 1 - procent_list[x]
                        changing_list.append(worth)
                        y += 2
                        x += 1

                    elif flat_list[y] == 1:
                        worth = 1 + procent_list[x]
                        changing_list.append(worth)
                        y += 2
                        x += 1
        break

