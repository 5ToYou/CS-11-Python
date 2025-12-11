solution_set = []
coins = [5,2,1]

start_sum = 0
need_sum = 16

while start_sum != need_sum:
    i = len(solution_set)
    start_sum += coins[0]
    solution_set.append(coins[0])
    
    if start_sum >= need_sum:
        x = 0
        while x < 2:
            x += 1
            solution_set.pop(i - 1)

            start_sum -= coins[0]
            start_sum += coins[1]
            solution_set.append(coins[1])

    if start_sum >= need_sum:
        solution_set.pop(i - 1)
        start_sum -= coins[1]
        start_sum += coins[2]
        solution_set.append(coins[2])

print(solution_set)


