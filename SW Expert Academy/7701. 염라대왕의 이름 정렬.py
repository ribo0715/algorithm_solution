# 7701. 염라대왕의 이름 정렬
"""
이름의 길이가 짧을수록 이 앞에 있었고, 같은 길이면 사전 순으로 앞에 있었다.
같은 이름은 하나만 남겨놓기
-> set으로 해서 먼저 같은 이름을 제거하도록 하려했는데,
heap으로 해서 먼저 일단 다 받는게 좋을지도 -> 굳이 그러지 않아도 되겠다

길이가 짧은순서, 사전순서

길이에 따라 dictionary를 만들고 적은 순서대로 일단 받아넣고 그 안을 sort해서 빼냄
"""

if __name__ == "__main__":
    T = int(input())

    for test_case in range(1, T + 1):
        name_dic = {}
        for i in range(1, 51):
            name_dic[i] = set() # 각 길이별로 주어진 아이템들

        N = int(input())
        for _ in range(N):
            name = input()
            length = len(name)

            name_dic[length].add(name)

        print("#{}".format(test_case))
        for i in range(1, 51):
            if name_dic[i]:
                name_dic[i] = list(name_dic[i])
                name_dic[i].sort()
                for name in name_dic[i]:
                    print(name)


"""
2
5
my
name
is
ho
seok
12
s
a
m
s
u
n
g
j
j
a
n
g
"""



