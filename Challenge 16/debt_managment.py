#CHALLENGE 16
def totalpaid(debt, interest, repayment):
  total = 0
  payments = 0
  while debt > 0:
    debt += round(debt * interest, 2)
    if debt < 50:
      total += debt
      payments += 1
      break
    if debt * repayment > 50:
      total += round(debt * repayment,2)
      debt -= round(debt * repayment,2)
      payments +=1
    else:
      debt -= 50
      total += 50
      payments += 1
    interest = round(debt / 1000,2)
    
  print(f'Total Paid: {round(total,2)}\nPayments made: {payments}\n----------------')


totalpaid(100,0.1,0.5)
totalpaid(100,0.43,0.46)
totalpaid(1500,0.25,0.5)
totalpaid(400,0.45,0.3)
