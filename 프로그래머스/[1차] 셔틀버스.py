# [1차] 셔틀버스

def solution(n, t, m, timetable):
    answer = ''

    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()

    last_time = 9 * 60 + (n - 1) * t # 막차 시간

    for i in range(n):
        if len(timetable) < m:  # 남은 인원이 모두 타고도 한 자리가 남는 경우
            answer = "%02d:%02d"%(last_time // 60, last_time % 60) # 막차 시간에 맞춰서 오면 됨
            break

        if i == n - 1: # 막차인 경우
            if timetable[0] <= last_time:
                last_time = timetable[m - 1] - 1 # 마지막에 타게 되는 사람보다 1분 빨리
            answer = "%02d:%02d" % (last_time // 60, last_time % 60)
            break

        bus_time = 9 * 60 + i * t # 버스 도착 시간
        for j in range(m): # m 명을 태움
            if timetable[0] <= bus_time:
                timetable.pop(0)
            else:
                break

    return answer