solution_set = []
coins = [5,2,1]

start_sum = 0
need_sum = 18
remaining_sum = need_sum


for coin in coins:
    while remaining_sum >= coin:
        solution_set.append(coin)
        remaining_sum -= coin

if remaining_sum == 0:
    print(solution_set)
else:
    print("_")


