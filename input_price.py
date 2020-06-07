"""
ターミナルに所持金と購入したいりんごの個数を入力させ、
合計金額と、残金に応じたメッセージを出力する。
"""

apple_price = 200

input_possession = input('所持金を入力してください。:')
possession = int(input_possession)

input_count = input('購入するりんごの個数を入力してください。:')
count = int(input_count)

#支払い合計額算出
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です。')
print('購入合計金額は' + str(total_price) + '円です。')
print('------')

#残金算出
remaining_money = possession - total_price

if remaining_money >= apple_price:
    print('りんごを' + str(count) + '個購入しました。')
    print('まだりんごを購入可能です。')
elif remaining_money == apple_price:
    print('りんごを' + str(count) + '個購入しました。')
    print('財布が空になりました。')
else:
    print('お金が足りずりんごが買えません。。。')
    print('ATMに行きましょう。')