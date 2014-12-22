# Change Return Program
from collections import OrderedDict as od



def change_return(cost, payment):
    cashback = payment - cost
    bills = cashback // 1
    change = cashback - bills
    quarters = 0
    coin_return ={  "Quarters"    : 0,
                    "Dimes"       : 0,
                    "Nickels"     : 0,
                    "Pennies"     : 0}
    coin_values = od([ ("Quarters", 0.25),
                                ("Dimes"    , 0.10),
                                ("Nickels"  , 0.05),
                                ("Pennies"  , 0.01)])
    for coin in coin_values:
        print (coin, coin_values[coin], "  >>  ", change // coin_values[coin])
    
print (change_return(7.52, 10))

print (50// 25)

