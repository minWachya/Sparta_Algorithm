import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    count = 0
    last_added_date_index = 0 # 마지막으로 공급한 날짜
    max_heap = []

    # stock이 k보다 많아야 k날까지 버틸 수 있음
    # k날까지 버티기(재고가 k보다 많을 때까지)
    while stock <= k:
        # 재고(버틸 수 있는 날)가 공급 일자보다 작아질 때까지(공장이 멈추기 직전까지)
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
            heapq.heappush(max_heap, -supplies[last_added_date_index])
            last_added_date_index += 1

        # 지나온 날 줄 가장 큰 말가루 수량을 담음(날짜는 상관 없음, 가장 큰 값만 가져오면 됨)
        count += 1
        heappop = heapq.heappop(max_heap)
        stock += -heappop

    return count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))

print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))