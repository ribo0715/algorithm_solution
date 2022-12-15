def solution(numbers):
    answer = 0
     
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer_list = []
    
    last = 0
    while last < len(numbers) - 1:
        for i in range(3, 6):
            temp = numbers[last:last+i]
            if temp in num_list:
                answer_list.append(str(num_list.index(temp)))
                last += i
                break
                
    answer = int("".join(answer_list))
    return answer
