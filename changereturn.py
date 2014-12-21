# Change Return Program

def change_return(cost, payment):
    cashback = payment - cost
    bills = cashback // 1
    change = cashback - bills
    coins = {"Quarters" : 0.25,
             "Dimes"    : 0.10,
             "Nickels"  : 0.05,
             "Pennies"  : 0.01}
    for coin in coins:
        print (coin)
    return cashback

print (change_return(7.50, 10))
