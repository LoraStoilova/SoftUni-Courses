train_ticket = 150
items = input().split("|")
budget = float(input())
sell_price_list = []
profit = 0

for item in items:
    type, price = item.split("->")
    price = float(price)
    if type == "Clothes":
        if price <= 50.00 and price <= budget:
            budget -= price
            sell_price = price * 1.4
            profit += sell_price - price
            sell_price_list.append(sell_price)


    elif type == "Shoes":
        if price <= 35.00 and price <= budget:
            budget -= price
            sell_price = price * 1.4
            profit += sell_price - price
            sell_price_list.append(sell_price)

    elif type == "Accessories":
        if price <= 20.50 and price <= budget:
            budget -= price
            sell_price = price * 1.4
            profit += sell_price - price
            sell_price_list.append(sell_price)
total_income = budget + sum(sell_price_list)

for sold_item in sell_price_list:
    print(f"{float(sold_item):.2f}", end= " ")
print()

print(f"Profit: {profit:.2f}")
if total_income >= train_ticket:
    print(f"Hello, France!")
else:
    print('Not enough money.')
