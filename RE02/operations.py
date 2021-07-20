money = int(input())
frequency = int(input())
interest_rate = float(input())

TIME = 2

final_amount = money * (1 + interest_rate/frequency)**(frequency*TIME)
print(round(final_amount, 3))