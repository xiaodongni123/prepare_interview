# @Date ：2024/05/23 20:13

def maxProfit(prices):
    min_price = float('inf')
    max_price = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_price:
            max_price = price - min_price
    return max_price


# 测试用例
if __name__ == '__main__':
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 4, 3, 1]
    print(maxProfit(prices1))  # 输出: 5
    print(maxProfit(prices2))  # 输出: 0





