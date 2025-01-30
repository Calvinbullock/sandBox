"""
A problem I was given in an interview and was not able to solve in time.
So I went back to solve it after.
"""

import math

def calculateMaximumProfit(cost, x):
    # Initialize variables
    max_profit = 0
    current_cost = 0
    itemlist = []

    # create and add each item to itemlist
    for i, c in enumerate(cost):
        itemlist.append({
            "profit": math.ceil(2 ** i),
            "index" : i,
            "cost": c
        })

    itemlist.sort(key=lambda item: item['profit'], reverse=True)

    # add to current cost and max profit
    for item in itemlist:
        cost = item['cost']
        profit = item['profit']

        # check that we don't go over x (max cost)
        if current_cost + cost <= x:
            current_cost += cost
            max_profit += profit


    # Return the maximum profit modulo (109 + 7)
    return max_profit % (10**9 + 7)

if __name__ == '__main__':
    # Sample input (replace with actual input)
    # cost = [10, 20, 14, 40, 50]
    # x = 70
    cost = [3, 4, 1]
    x = 8
    ans = 7
    result = calculateMaximumProfit(cost, x)
    print("res: ", result)
    print("ans: ", ans)
    print()

    cost = [10, 20, 14, 40, 50]
    x = 70
    ans = 20
    result = calculateMaximumProfit(cost, x)
    print("res: ", result)
    print("ans: ", ans)
    print()

    cost = [19, 78, 27, 18, 20]
    x = 25
    ans = 16
    result = calculateMaximumProfit(cost, x)
    print("res: ", result)
    print("ans: ", ans)
