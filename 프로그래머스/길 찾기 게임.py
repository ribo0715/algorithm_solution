# 길 찾기 게임
"""
전위 순회(preorder) : Root -> L -> R
후위 순회(postorder) : L -> R -> Root

이진트리를 구성하는 노드들의 좌표가 담긴 배열 nodeinfo
-> 노드들로 구성된 이진트리를 전위 순회, 후위 순회한 결과 반환

x좌표 기준으로 정렬, y좌표 기준으로 정렬

현재 target 기준으로 x, y의 크기를 비교해가면서
"""

import sys

sys.setrecursionlimit(10 ** 6)  # recursion 최대치를 높임 -> 없으면 테스트 6, 7번에서 에러발생


def preorder(sorted_by_x, sorted_by_y, answer):  # root -> L -> R
    # 현재 가장 위에 있는 것부터 시작
    cur_node = sorted_by_y[0]
    index_x = sorted_by_x.index(cur_node)  # sorted_by_x에서 cur_node의 index

    LC_sorted_by_y = []
    RC_sorted_by_y = []

    for i in range(1, len(sorted_by_y)):
        if cur_node[0] > sorted_by_y[i][0]:  # cur_node보다 왼쪽에 위치 -> Left Child
            LC_sorted_by_y.append(sorted_by_y[i])
        else:
            RC_sorted_by_y.append(sorted_by_y[i])

    answer.append(cur_node[2])  # cur_node의 번호를 answer에 넣음
    if LC_sorted_by_y:
        preorder(sorted_by_x[:index_x], LC_sorted_by_y, answer)
    if RC_sorted_by_y:
        preorder(sorted_by_x[index_x + 1:], RC_sorted_by_y, answer)


def postorder(sorted_by_x, sorted_by_y, answer):  # L -> R -> root
    # 현재 가장 위에 있는 것부터 시작
    cur_node = sorted_by_y[0]
    index_x = sorted_by_x.index(cur_node)  # sorted_by_x에서 cur_node의 index

    LC_sorted_by_y = []
    RC_sorted_by_y = []

    for i in range(1, len(sorted_by_y)):
        if cur_node[0] > sorted_by_y[i][0]:  # cur_node보다 왼쪽에 위치 -> Left Child
            LC_sorted_by_y.append(sorted_by_y[i])
        else:
            RC_sorted_by_y.append(sorted_by_y[i])

    if LC_sorted_by_y:
        postorder(sorted_by_x[:index_x], LC_sorted_by_y, answer)
    if RC_sorted_by_y:
        postorder(sorted_by_x[index_x + 1:], RC_sorted_by_y, answer)
    answer.append(cur_node[2])  # cur_node의 번호를 answer에 넣음


def solution(nodeinfo):
    sorted_by_x = sorted(nodeinfo)  # 왼쪽에 있는 순서대로 정렬
    sorted_by_y = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))  # 위에 있는 순서대로 정렬

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)  # 해당 노드의 번호를 끝에 붙여 같이 저장해줌

    pre_answer = []
    post_answer = []

    preorder(sorted_by_x, sorted_by_y, pre_answer)
    postorder(sorted_by_x, sorted_by_y, post_answer)

    answer = [pre_answer, post_answer]
    return answer