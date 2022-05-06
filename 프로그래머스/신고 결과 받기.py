# 신고 결과 받기

"""
각 user별로 신고한 목록
전체 결과 정지된 아이디 목록

각 유저들에 의해 신고된 횟수를 배열에 저장
"""

def solution(id_list, report, k):
    answer = []

    count_dic = {}  # 각 유저들이 신고당한 횟수를 담음
    report_dic = {}  # 각 유저가 신고한 id들을 담을 딕셔너리
    for id in id_list:
        report_dic[id] = []
        count_dic[id] = 0

    for report_str in report:
        user_A, user_B = map(str, report_str.split())  # A가 B를 신고
        if user_B not in report_dic[user_A]:
            report_dic[user_A].append(user_B)
            count_dic[user_B] += 1  # 신고당한 횟수 +1

    banned_id_list = []  # 정지되는 사용자들의 id를 담을 배열
    for user_id in count_dic:
        if count_dic[user_id] >= k:
            banned_id_list.append(user_id)

    for user_id in report_dic:
        count = 0
        for target_id in report_dic[user_id]:  # user_id가 신고한 target_id들에 대해
            if target_id in banned_id_list:  # 정지된 id인 경우
                count += 1
        answer.append(count)

    return answer