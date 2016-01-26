from hypothesis import given
import hypothesis.strategies as st

from pprint import pprint

def naive_max_buy_sell(prices):
    return max(b - a for i, a in enumerate(prices) for j, b in enumerate(prices) if i < j)

def max_buy_sell(prices):
    buy_index = 0
    sell_index = 1
    max_profit = prices[sell_index] - prices[buy_index]
    candidate_buy_index = None

    for index, price in list(enumerate(prices))[1:]:

        if candidate_buy_index is not None and max_profit < price - prices[candidate_buy_index]:
            sell_index = index
            old_max_profit = max_profit
            max_profit = prices[sell_index] - prices[candidate_buy_index]
            buy_index = candidate_buy_index
            candidate_buy_index = None
            assert max_profit > old_max_profit

        if max_profit < price - prices[buy_index]:
            sell_index = index
            old_max_profit = max_profit
            max_profit = prices[sell_index] - prices[buy_index]
            assert max_profit > old_max_profit

        if candidate_buy_index is not None and candidate_buy_index < sell_index \
           and prices[sell_index] - prices[candidate_buy_index] > max_profit:

            old_max_profit = max_profit
            max_profit = prices[sell_index] - prices[candidate_buy_index]
            assert max_profit > old_max_profit
            buy_index = candidate_buy_index
            candidate_buy_index = None

        if price < prices[buy_index] and (candidate_buy_index is None or price < prices[candidate_buy_index]):
            candidate_buy_index = index

    return max_profit


@given(st.lists(st.integers(min_value=0, max_value=200), min_size=2))
def print_naive_max_buy_sell_and_list(prices):
    naive = naive_max_buy_sell(prices)
    efficient = max_buy_sell(prices)

    assert naive == efficient

print_naive_max_buy_sell_and_list()
