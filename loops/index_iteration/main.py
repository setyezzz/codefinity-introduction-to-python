prices = [29.99, 45.50, 12.75, 38.20]
discounts = [0.1,0.2,0.15,0.05]
for item in range(len(prices)):
    original_price = prices[item]
    discount = discounts[item]
    new_price = original_price * (1 - discount)
    prices[item] = new_price
    print(f'Updated price for item {item}: ${new_price:.2f}')