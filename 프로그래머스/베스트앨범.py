import operator


def solution(genres, plays):
    answer = []

    dic = {}
    dic_sum = {}

    # for genre, play in zip(genres, plays):
    #     if genre in list(dic.keys()):
    #         dic[genre] += play
    #     else:
    #         dic[genre] = play

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if not (genre in list(dic.keys())):
            dic[genre] = {}
            dic_sum[genre] = 0

        dic[genre][i] = play
        dic_sum[genre] += play

    sorted_dic_sum = sorted(dic_sum.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(len(sorted_dic_sum)):
        genre = sorted_dic_sum[i][0]

        sorted_dic = sorted(dic[genre].items(), key=operator.itemgetter(1), reverse=True)

        answer.append(sorted_dic[0][0])
        if len(sorted_dic) >= 2:
            answer.append(sorted_dic[1][0])

    return answer