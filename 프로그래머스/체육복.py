def solution(n, lost, reserve):
    # n : 전체 학생 수
    # lost : 도난당한 학생들
    # reserve : 여분을 가지고 있는 학생들
    answer = 0
    cannot_num = 0

    lost.sort()

    # 여분을 가지고 있었는데 도난을 당했다 -> 본인의 여분 체육복 사용
    # lost, reserve 둘다 포함되는 학생은 생각하지 않아도 됨
    lost_and_reserve = list(set(lost) & set(reserve))
    lost = list(set(lost) - set(lost_and_reserve))
    reserve = list(set(reserve) - set(lost_and_reserve))

    for x in lost:
        # 앞번호가 여분 체육복 보유
        if x - 1 in reserve:
            # 앞번호에게서 우선 빌림
            # lost.remove(x)
            reserve.remove(x - 1)
        # 뒷번호가 여분 체육복 보유
        elif x + 1 in reserve:
            # 뒷번호에게서 빌림
            # lost.remove(x)
            reserve.remove(x + 1)
        else:
            cannot_num += 1

    print(lost)
    answer = n - cannot_num

    return answer