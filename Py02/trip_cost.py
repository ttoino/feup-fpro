distance = int(input())
fuel_efficiency = float(input())
fuel_price = float(input())

total_cost = distance*fuel_efficiency*fuel_price/100

print(round(total_cost, 2))