# mortgage.py
#
# Exercise 1.7

# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0 and principal >= payment:
  if month <= 12 :
    principal = principal * (1+rate/12) - (payment +extra_payment)
    total_paid = total_paid + (payment +extra_payment)
    month = month + 1
    print (month , total_paid, principal)
  elif month > extra_payment_start_month and month <= extra_payment_end_month:
    principal = principal * (1+rate/12) - (payment + extra_payment)
    total_paid = total_paid + payment + extra_payment
    month = month + 1
    print (month , total_paid, principal)
  else:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    month = month + 1
    print (month , total_paid, principal)


print('Total paid', total_paid)
print ('The number of months', month)
