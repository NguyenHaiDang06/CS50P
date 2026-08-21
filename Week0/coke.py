amount=50
a=[5,10,25]
tien_da_tra=0
while tien_da_tra<amount:
    amountDue=amount-tien_da_tra
    print("Amount Due:",amountDue)
    coin=int(input("Insert Coin:"))
    
    if coin in a:
        tien_da_tra+=coin
        
tien_thua=tien_da_tra-amount
print("Change Owed:",tien_thua)

