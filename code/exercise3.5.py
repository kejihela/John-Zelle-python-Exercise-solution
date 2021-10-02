def coffee():
    n = int(input("How many number of goods doyou wwant to order "))
    coffee_price = (10.50 - 0.86) * n
    over_head = 1.50 * n
    shipping = 0.86 * n
    cost_of_order = coffee_price + over_head + shipping
    print("total cost of order is", cost_of_order)
coffee()

    
