# 가사 검색(Trie 알고리즘 사용)

from collections import defaultdict

class Node:
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.child = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr = self.head
        curr.count += 1

        for c in string:
            if c not in curr.child:
                curr.child[c] = Node(c)

            curr = curr.child[c]
            curr.count += 1

    def count(self, string):
        curr = self.head

        for c in string:
            if c not in curr.child:
                return 0
            curr = curr.child[c]

        return curr.count


def make_trie(words, reverse):
    trie_dict = defaultdict(Trie)

    for word in words:
        if reverse:
            word = word[::-1]

        trie_dict[len(word)].insert(word)

    return trie_dict


def solution(words, queries):
    answer = []

    tries = make_trie(words, False)
    reversed_tries = make_trie(words, True)

    for query in queries:
        length = len(query)
        start_index = query.index("?")  # 값이 0이면 접두사, 아니면 접미사
        end_index = length - 1 - query[::-1].index("?")

        if start_index == 0:  # "?" 로 시작 -> 뒤에서부터 시작
            curr_answer = reversed_tries[length].count(query[end_index + 1:][::-1])
        else:  # "?" 로 끝 -> 앞에서부터 시작
            curr_answer = tries[length].count(query[:start_index])

        answer.append(curr_answer)

    return answer