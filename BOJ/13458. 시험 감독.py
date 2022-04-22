# 13458. 시험 감독

def solution():
    answer = 0
    # Master 시행
    for i in range(N):
        if arr[i] > 0:
            arr[i] -= Master
            answer += 1
 
        if arr[i] > 0:
            answer += int(arr[i]/Sub)
 
            if arr[i] % Sub != 0:
                answer += 1
 
    return answer
 

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    Master, Sub = map(int, input().split())
    print(solution())
