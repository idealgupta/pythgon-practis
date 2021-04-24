#discount 
bill_amount=int(input("enter the amount : "))
if bill_amount>=5000:
    bill_amount=bill_amount - 500
elif bill_amount>=4000 and bill_amount<=4999:
    bill_amount=bill_amount - 400
elif bill_amount>=3000 and bill_amount<=3999:
    bill_amount=bill_amount - 300
elif bill_amount>=2000 and bill_amount<=2999:
    bill_amount=bill_amount - 200
elif bill_amount>=1000 and bill_amount<=999:
    bill_amount=bill_amount -100
print("final amount ",bill_amount)