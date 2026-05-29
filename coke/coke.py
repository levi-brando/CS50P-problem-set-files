coke_price = 50

while (coke_price > 0):
    coin = int(input("Insert Coin: "))
    match coin:
        case 25:
            coke_price -= 25
        case 10:
            coke_price -= 10
        case 5:
            coke_price -= 5

    if coke_price < 0:
        break

    print(f"Amount Due: {coke_price}")

if coke_price <= 0:
    print(f"Change Owed: {abs(coke_price)}")

