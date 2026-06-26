def calculate_total_cost(price,quantity):
    result = price*quantity
    return result
apples_total_cost = calculate_total_cost(1.50, 10)
print(f"The total cost for apples is ${apples_total_cost}")