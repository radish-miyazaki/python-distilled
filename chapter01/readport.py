# readport.py
#
# "NAME,SHARES,PRICE" 形式のデータを持つファイルを読み込む

import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name = row[0]
                shares = int(row[1])
                price = float(row[2])
                holding = (name, shares, price)
                portfolio.append(holding)
            except ValueError as err:
                print("Bad row: ", row)
                print("Reason: ", err)

    return portfolio


def main(argv):
    if len(argv) == 1:
        filename = input('Enter filename: ')
    elif len(argv) == 2:
        filename = argv[1]
    else:
        raise SystemExit(f"Usage: {argv[0]} [filename]")

    portfolio = read_portfolio(filename)
    for name, shares, price in portfolio:
        print(f"{name:>10s} {shares:>10d} {price:>10.2f}")


if __name__ == '__main__':
    import sys

    main(sys.argv)
