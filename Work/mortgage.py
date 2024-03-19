# mortgage.py
#
# Exercise 1.7

# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

while principal > 0 : 
  while month <= 12 :
    principal = principal * (1+rate/12) - (payment +1000)
    total_paid = total_paid + (payment +1000)
    month = month + 1
  else:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    month = month + 1
    
    
print('Total paid', total_paid)
print ('The number of months', month)
