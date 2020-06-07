"""
ターミナルに所持金と購入したいりんごの個数を入力させ、
合計金額と、残金に応じたメッセージを出力する。
"""

input_possession = input('所持金を入力してください。:')
possession = int(input_possession)

items = {'りんご':120, 'バナナ':200, 'オレンジ':130}

for item_name in items:
    print('-----------------')
    print('現在の所持金は' + str(possession) + '円です。')
    print(item_name + 'は、1個' + str(possession) + '円です。')

    input_count = input('購入する' + item_name + 'の個数を入力してください。')
    count = int(input_count)

    print('購入するりんごの個数は' + str(count) + '個です。')

    #支払い合計額算出
    total_price = items[item_name] * count
    print('購入合計金額は' + str(total_price) + '円です。')

    if possession >= total_price:
        print(item_name + 'を' + str(count) + '個購入しました。')
        possession -= total_price
        if possession == 0:
            print('残金は0円です。')
            break
    else:
        print('お金が足りず' + item_name + 'が買えません。。。')
        print('ATMに行きましょう。')
print('全種類購入しました。残金は' + str(possession) + '円です。')