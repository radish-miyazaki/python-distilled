# pcost.py
#
# "NAMES,SHARES,PRICE"形式のデータを持つファイルを読み込む
# 次のような形式を想定する
#
#   SYM,123,456,78

import sys

import readport as rp


def portfolio_cost(filename):
    """
    ポートフォリオの総株式数 * 株価を計算する
    """
    port = rp.read_portfolio(filename)
    return sum(shares * price for _, shares, price in port)


if len(sys.argv) != 2:
    raise SystemExit(f"Usage: {sys.argv[0]} filename")

rows = []
with open(sys.argv[1], 'rt') as file:
    for line in file:
        rows.append(line.split(','))

total = sum([int(row[1]) * float(row[2]) for row in rows])
print(f"total cost: {total:0.2f}")
