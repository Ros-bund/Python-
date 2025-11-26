price = int(input())
coins = 0


coins += price // 25  
price %= 25           

coins += price // 10  
price %= 10           

coins += price // 5   
price %= 5            

coins += price        

print(coins)
