# 1218. [SW 문제해결 기본] 4일차 - 괄호 짝짓기

par = ["(", "[", "{", "<", ")", "]", "}", ">"] # 괄호 리스트

if __name__ == "__main__":
    # 10개 테스트케이스
    for test_case in range(1, 11):
        length = int(input())
        is_ok = 1 # 문제가 있으면 0으로 바꾸고 바로 출력

        line = input()
        stack = []
        for x in line: # 하나씩 읽어서 확인
            if stack: # stack 에 뭐가 들어있으면
                if par.index(x) == (par.index(stack[-1]) + 4) % 8: # 가장 마지막 것과 확인
                    stack.pop()
                else:
                    stack.append(x)

            else:
                stack.append(x)

        if stack:
            is_ok = 0

        print("#{} {}".format(test_case, is_ok))

