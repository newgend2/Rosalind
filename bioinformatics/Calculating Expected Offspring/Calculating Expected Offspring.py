with open('rosalind_iev.txt') as f:
    num_list = map(int, f.readline().split())
    num_list = [num * 2 for num in num_list]
    prob_list = [1, 1, 1, .75, .5, 0]
    expected_value = sum(num * prob for num, prob in zip(num_list, prob_list))
    print(expected_value)
