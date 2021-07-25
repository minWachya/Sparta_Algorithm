shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 쿠폰 내림차순 정렬
    coupons.sort(reverse=True)
    # 가격 내림차순 정렬
    prices.sort(reverse=True)

    price_index = 0
    coupon_index = 0
    result = 0

    # 가장 높은 가격에 가장 높은 할인 쿠폰 적용
    while price_index < len(prices) and coupon_index < len(coupons):
        result += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    # 계산할 물건이 더 많을 때 그냥 더하기
    while price_index < len(prices):
        result += prices[price_index]
        price_index += 1

    return result


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.