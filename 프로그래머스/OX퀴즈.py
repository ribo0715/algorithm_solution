def solution(quiz):
    answer = []

    for cur in quiz:
        cur_list = cur.split()
        X, op, Y, equal, Z = cur_list
        X, Y, Z = int(X), int(Y), int(Z)

        if op == "+":
            if X + Y == Z:
                answer.append("O")
            else:
                answer.append("X")

        elif op == "-":
            if X - Y == Z:
                answer.append("O")
            else:
                answer.append("X")

    return answer