def get_token(rarity, expected_price, start_price):
    import requests
    url = f'https://api-crypto.letmespeak.org/api/escrow?sortBy=LowestPrice&page=1&rarity={rarity}'
    response = requests.get(url=url)
    result = response.json()
    price = result['items'][0]['price']
    spreads = round(((price - start_price) / start_price) * 100, 2)

    if rarity == 2:
        rarity_str = "Uncommon"
    elif rarity == 3:
        rarity_str = "Rare"
    elif rarity == 4:
        rarity_str = "Epic"
    else:
        rarity_str = "Legendary"
    print(f"稀有度：{rarity_str} 目前地板价：{price} 高于官方定价：{spreads} %")
    for item in result['items']:
        if item['price'] < expected_price and item['nft']['details']['attributes'][7]['value'] == \
                item['nft']['details']['attributes'][8]['value'] and item['nft']['details']['attributes'][11][
            'value'] == item['nft']['details']['attributes'][12]['value']:
            return item['nft']['details']['name'], item['id']
    return None, None

def main():
    while True:
        price_2 = 99
        price_3 = 250
        price_4 = 600
        price_5 = 2000
        result2, id_2 = get_token(2, 120, price_2)
        result3, id_3 = get_token(3, 300, price_3)
        result4, id_4 = get_token(4, 650, price_4)
        result5, id_5 = get_token(5, 2200, price_5)
        url = 'https://market.letmespeak.org/#/escrow/'
        if result2 is not None:
            print(f'稀有度 Uncommon 的{result2} 低于地板价')
            print(url + id_2)
        elif result3 is not None:
            print(f'稀有度 Rare 的{result3} 低于地板价')
            print(url + id_3)
        elif result4 is not None:
            print(f'稀有度 Epic 的{result4} 低于地板价')
            print(url + id_4)
        elif result5 is not None:
            print(f'稀有度 Legendary 的{result5} 低于地板价')
            print(url + id_5)
        else:
            import time
            print('本轮无异常', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            time.sleep(5)
        while True:
           try:
            main()
            break
           except Exception as e:
            print('error')
main()