# 주차 요금 계산

from collections import defaultdict


# time 시간에 대한 요금을 구함
def get_fee(basic_time, basic_fee, unit_time, unit_fee, time):
    if time <= basic_time:
        return basic_fee

    if (time - basic_time) % unit_time == 0:
        unit = (time - basic_time) // unit_time
        return basic_fee + unit * unit_fee
    else:
        unit = (time - basic_time) // unit_time
        return basic_fee + (unit + 1) * unit_fee


def solution(fees, records):
    answer = []

    basic_time, basic_fee, unit_time, unit_fee = fees

    last_time = 23 * 60 + 59  # 23:59에 모두 out

    time_dic = {}  # 각 차량의 최근 in 시간을 저장
    total_time_dic = defaultdict(int)  # 각 차량의 전체 사용 시간
    fee_dic = defaultdict(int)  # 각 차량의 주차 요금을 저장

    for record in records:
        # print(time_dic)
        cur_time, car_num, history = record.split()

        cur_time = int(cur_time[0:2]) * 60 + int(cur_time[3:5])  # 분으로 바꿈

        if history == "IN":
            time_dic[car_num] = cur_time
        else:
            temp_time = cur_time - time_dic[car_num]
            total_time_dic[car_num] += temp_time

            # print(car_num,"번 차량", temp_time, "분 만큼 사용")
            del time_dic[car_num]

    # 남은 차량들은 23:59에 모두 out
    for car_num in time_dic:
        temp_time = last_time - time_dic[car_num]
        total_time_dic[car_num] += temp_time

    # 각 차량별 요금 계산
    for car_num in total_time_dic:
        total_time = total_time_dic[car_num]
        total_fee = get_fee(basic_time, basic_fee, unit_time, unit_fee, total_time)
        # print(car_num, "번 차량", total_time, "만큼 사용 ->", total_fee, "원 요금나옴")
        fee_dic[car_num] = total_fee

    fee_list = sorted(fee_dic.items())  # 차량 번호 작은 순서대로 정렬
    for i in range(len(fee_list)):
        # print(fee_list[i][1],"번 차량 요금 :", fee_list[i][1])
        answer.append(fee_list[i][1])

    return answer