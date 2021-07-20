a = int(input())
b = int(input())

dif = a - b
is_pair = dif % 2 == 0
weird_sum = a + b
weird_sum *= 1 + is_pair
weird_sum += int(not(is_pair))*a*b

print(weird_sum)