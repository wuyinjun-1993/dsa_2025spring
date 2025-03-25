
def recMC(coinValueList,change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c<= change]:
            numCoins =1+recMC(coinValueList,change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

print(recMC([1,5,10,25],63))



def recDC(coinValueList,change,knownResults):
    minCoins = change
    if change in coinValueList: #递归基本结束条件
        knownResults[change]=1 #记录最优解
        return 1
    elif knownResults[change]>0:
        return knownResults[change] #查表成功，
    else:
        for i in [c for c in coinValueList if c<= change]:
            numCoins=1+recDC(coinValueList,change -i,knownResults)
        if numCoins < minCoins:
            minCoins =numCoins#找到最优解，记录到表中
            knownResults[change]=minCoins
    return minCoins
print(recDC([1,5,10,25],63,[0]*64))

