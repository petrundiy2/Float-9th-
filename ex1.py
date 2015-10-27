from decimal import Decimal, getcontext
>>> getcontext().prec = 2
>>> Decimal('1.10') / 3
Decimal('0.37')
