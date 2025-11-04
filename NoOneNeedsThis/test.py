import time
start_time = time.perf_counter()

arr = [4,8,-2,6,14,3,10,5,-54,3,11,64,30,0,-7,4,-66]

lengh = len(arr)
for x in range(lengh - 1):
    for y in range(lengh - x - 1):
        if arr[y] > arr[y + 1]:
            arr[y],arr[y + 1] = arr[y + 1],arr[y]

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"{arr}, {elapsed_time:.10f}")