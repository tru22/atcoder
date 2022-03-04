inputLine = list(map(int, input().split()))

stations = input().split(' ')
targetStations = set(input().split(' '))

for i in stations:
    print('Yes' if i in targetStations else 'No')

# listではなく，setの場合の"x in s"だとはハッシュテーブルを使うので計算量が少ないみたい．ずるい
# listではおそらく線形探索していて，平均計算量O(n)
# setやdictではハッシュテーブルを使っているっぽくて，平均計算量O(1)
# 2206ms vs 89ms
# https://qiita.com/Hironsan/items/68161ee16b1c9d7b25fb
