# import heapq

def solution(jobs):
    answer = 0
    
    time = 0
    sum_term = 0
    
    n = len(jobs)
    
    jobs = sorted(jobs, key = lambda x : x[0])
    waiting_jobs = [] # 작업 대기중
    
    while jobs or waiting_jobs:
        # 작업 목록에 현재 시간에 작업 가능한 것들을 빼냄
        while jobs:
            if time >= jobs[0][0]:
                waiting_jobs.append(jobs.pop(0))
            else:
                break
                
        # 작업할 수 있는게 없는 경우
        if not waiting_jobs:
            time += 1
            continue
        
        # 작업시간이 적은 순서대로 정렬
        waiting_jobs = sorted(waiting_jobs, key = lambda x : x[1])
        cur_job = waiting_jobs.pop(0)
        
        time += cur_job[1]
        sum_term += time - cur_job[0] # 요청부터 종료까지 걸린 시간
                    
        
    answer = sum_term // n
    
    return answer
