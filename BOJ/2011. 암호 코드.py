# 2011. 암호 코드

code = [0] + list(map(int, input()))

dp = [1] * (len(code))

dp[1] = 1

if code[1] == 0:
    print(0)
    quit()
else:
    for i in range(2, len(code)):
        if code[i - 1] == 1:
            if code[i] == 0:  # 10만 가능
                dp[i] = dp[i - 2]
            elif code[i] > 0:  # 붙여도 되고 띄어도 되고
                dp[i] = dp[i - 2] + dp[i - 1]
        elif code[i - 1] == 2:
            if code[i] == 0:  # 20만 가능
                dp[i] = dp[i - 2]
            elif code[i] <= 6:  # 붙여도 되고 띄어도 되고
                dp[i] = dp[i - 2] + dp[i - 1]
            else:  # 따로
                dp[i] = dp[i - 1]
        else:
            if code[i] == 0:
                print(0)
                quit()
            else:
                dp[i] = dp[i - 1]

    print(dp[-1] % 1000000)

