def best_time_buy_sell_stock(prices):
    
    current_buy = float('inf')

    max_profit = float('-inf')

    for val in prices:

        current_buy = min(current_buy,val)

        current_profit = val - current_buy

        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit




print(best_time_buy_sell_stock([7,1,5,3,6,4]))
print(best_time_buy_sell_stock([7,6,4,3,1]))