principal = 1000
rate = 0.05
num_years = 5
year = 1
while year <= num_years:
    principal = principal * (1 + rate)
    print(f"{year:>3d} {principal:0.2f}")
    year += 1
