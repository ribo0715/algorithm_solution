def solution(M, N):
    answer = 0
    
    if M > N:
        M, N = N, M
    
    answer += M - 1
    
    answer += (N - 1) * (M)
    
    return answer
