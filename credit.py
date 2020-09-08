# source: https://calcus.ru/kalkulyator-ipoteki
MONTHS_IN_YEAR = 12

PERSENT = 0.079
PRICE = 1200000
YEARS = 10
MONTHS = YEARS * MONTHS_IN_YEAR

# PERSENT = 0.10
# PRICE = 600000
# # YEARS = 10
# MONTHS = 6

# MONEY_PER_DAY = PRICE / (DAYS_IN_YEAR * YEARS)

MONTH_PERSENT = PERSENT / MONTHS_IN_YEAR
# DAYS_IN_YEAR = 365
# PERSENT_DAY = PERSENT / DAYS_IN_YEAR

def step(state, price, persent, time_in_months, payments):
  month_money = price / time_in_months
  money, credit, main_money = state
  month_persent = persent / MONTHS_IN_YEAR
  delta = money * month_persent
  payments.append(month_money + delta)
  return (money - month_money, credit + month_money + delta, main_money + month_money)

def calc(price, persent, time_in_months):
  state = (price, 0, 0) # starting state
  payments = []
  for _ in range(time_in_months):
    state = step(state, price, persent, time_in_months, payments)
  return (state, payments)


# month = calc(START_STATE, PERSENT, MONEY_PER_DAY, 31)

(finish, payments) = calc(PRICE, PERSENT, MONTHS)

print("-- Differentiated --")
print("All money: ", finish[1])
print("Payments: ", f"{payments[0]} ... {payments[-1]}")
print("Payments: ", f"{payments}")
print(finish)
print("-- Annuity --")
# print(month)

def coef(month_persent, time_in_months):
  p = month_persent
  return p / (pow (1 + p, time_in_months) - 1)

def all_money(price, month_persent, time_in_months):
  p = month_persent
  a = price * coef(p, time_in_months)
  b = price * p
  return (a + b) * time_in_months

ALL_MONEY = all_money(PRICE, MONTH_PERSENT, MONTHS)
print(f'a = {PRICE * coef(MONTH_PERSENT, MONTHS)}')
print(f'b = {PRICE * MONTH_PERSENT}')
print(f'All money = {ALL_MONEY}')
print(f'average per month = {ALL_MONEY / MONTHS}')

print()
print(f"DELTA: {ALL_MONEY - finish[1]}")


"""
Аннуитетный
6 900,00
6 859,92
6 819,60
6 779,05
6 738,27
...
79,30

Дифференцированный
6 900,00
6 842,50
6 785,00
6 727,50
6 670,00
...
57,50


Аннуитетный
h = y + p*(x + y) => (1+p)*y + p*x => y = (h - p*x)/(1+p)
=> y = x/(1+p)

мы знаем отношение первого платежа к последнему (по основному долгу)
13791.95 / 6971.25 = 1.9784041... = pow(1+p, 120 - 1)

b = price * p

((a+b)/(1+p))/a = (1 + p)^(120 - 1)
(a+b)/a = (1 + p)^120
b/a = (1 + p)^(120) - 1
a = b / ( (1 + p)^(120) - 1 )

a = price * p / ( (1 + p)^120 )

all_money = (a+b) * 120 = 1664549.9703673585

"""