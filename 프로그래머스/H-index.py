# def solution(citations):
#     answer = 0

#     n = len(citations)

#     citations.sort() # 우선 정렬

#     temp_h = 1

#     while True:
#         if how_many_citation_more_than_h(citations, temp_h) < temp_h:
#             temp_h -= 1
#             break

#         temp_h += 1

#     answer = temp_h
#     return answer

# def how_many_citation_more_than_h(sorted_citations, h):
#     sorted_citations.append(h)
#     sorted_citations.sort()
#     index_h = sorted_citations.index(h)
#     sorted_citations.remove(h)

#     return len(sorted_citations) - index_h

def solution(citations):
    answer = 0

    citations.sort(reverse=True)

    n = len(citations)

    for i in range(n):
        if citations[i] <= i:
            return i

    return n

    return answer