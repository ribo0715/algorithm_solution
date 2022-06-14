def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = [0] * bridge_length  # 다리의 상황을 나타낼 배열

    while len(bridge):
        bridge.pop(0)  # 다리 위의 모든 트럭들 한칸 앞으로 이동

        if len(truck_weights) != 0:
            if sum(bridge) + truck_weights[0] > weight:  # 다음 트럭이 올라갈 수 없는 상황이라면
                bridge.append(0)  # 0을 넣어줌
            else:  # 다음 트럭이 건널 수 있다면
                next_truck = truck_weights.pop(0)
                bridge.append(next_truck)

        answer += 1

    return answer