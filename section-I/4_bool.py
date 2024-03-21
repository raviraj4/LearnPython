# two nested lists
l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]
l_one_ans = l_one[2][0]
l_two_ans = l_two[2]['k1']
print("answer 1:", l_one_ans)
print("answer 1:", l_two_ans)
print("answer:", l_one_ans >= l_two_ans)
