prices = [100, 102, 101, 99, 98, 105, 107, 103]
def maxProfit(prices):
    if not prices:
        return 0
    
    left = 0   # Buy pointer
    right = 1  # Sell pointer
    max_profit = 0
    
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit,profit)
        else:
            left = right
        right+=1
    return max_profit

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5