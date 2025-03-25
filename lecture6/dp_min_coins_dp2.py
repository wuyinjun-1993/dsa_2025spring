def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change +1):
        coinCount =cents
        newCoin=1 #初始化一下新加硬币
        for j in [c for c in coinValueList if c<= cents]:
            if minCoins[cents-j] + 1<coinCount :
                coinCount=minCoins[cents-j] + 1
                newCoin =j #对应最小数量，所减的硬币
        minCoins[cents]=coinCount
        coinsUsed[cents]=newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin =change
    while coin > 0:
        thisCoin =coinsUsed[coin]
        print(thisCoin)
        coin =coin - thisCoin

coinsUsed=[0]*64
        
dpMakeChange([1,5,10,21,25],63,[0]*64, coinsUsed)

printCoins(coinsUsed, 63)

