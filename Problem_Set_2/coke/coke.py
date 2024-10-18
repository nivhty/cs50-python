total_money = 0
amount_due = 50
while total_money < 50:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in (25,10,5):
        total_money = total_money + coin
        amount_due = 50 - total_money
print(f"Change Owed: {abs(amount_due)}")
