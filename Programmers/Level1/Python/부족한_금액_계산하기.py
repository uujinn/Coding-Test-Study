def solution(price, money, count):
    total_price = 0

    for i in range(count):
        total_price += price * (i+1)
    
    return total_price - money if total_price - money > 0 else 0
