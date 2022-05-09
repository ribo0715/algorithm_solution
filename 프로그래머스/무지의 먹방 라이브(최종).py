# 무지의 먹방 라이브 -> 이분 탐색

def solution(food_times, k):
    low, high = 0, 100000000
    n = len(food_times)
    target_num = 0 # food_times 전체에 빼줄 수
    time_count = 0 # 마지막 index를 가리키게 될 시간

    while low <= high: # 이분탐색
        mid = (low + high) // 2
        time_for_last = n * mid # 마지막 index를 가리키게 될 시간

        for food_time in food_times:
            temp = food_time - mid
            if temp < 0:
                time_for_last += temp

        if time_for_last <= k:
            target_num = mid
            time_count = time_for_last
            low = mid + 1
        else:
            high = mid - 1

    food_times = [food_time - target_num for food_time in food_times]
    # print(food_times)
    
    for i in range(n):
        if food_times[i] > 0 and time_count == k:
            return i + 1 # 몇 번째 음식을 먹을 차례인지
        elif food_times[i] > 0:
            time_count += 1
            
    return - 1