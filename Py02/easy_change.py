price = int(input())
received = int(input())

change = received-price

fifty = change//50
change %= 50

twenty = change//20
change %= 20

ten = change//10
change %= 10

five = change//5
change %= 5

print(fifty, twenty, ten, five)