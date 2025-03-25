

def candy(ratings):
    cds =[1]* len(ratings) #糖果列表
    for i in range(1, len(ratings)):
        if ratings[i-1]< ratings[i]:
            cds[i]=cds[i-1]+1 #分数高，比前面多1颗糖
        elif ratings[i-1]== ratings[i]:
            cds[i]=1 #分数相同，给最低标准1颗糖
        else:
            cds[i]=1 #分数低，给最低标准1颗糖
            if cds[i-1]== 1:# 但如果前面仅有1颗糖，需要加糖:
                for k in range(i-1,-1,-1):
                    cds[k] += 1# 评分向前递增而糖果数没有递增的话，，才加糖
                    if k> 0 and (ratings[k]>= ratings[k-1] or cds[k]<cds[k-1]):
                        break
                    
                    
                    


def candy(ratings):
    n = len(ratings)
    left = [0] * n
    # 向右扫描
    for i in range(n):
        if i > 0 and ratings[i] > ratings[i - 1]:
            left[i] = left[i - 1] + 1
        else:
            left[i] = 1
    
    # 向左扫描
    right = ret = 0
    for i in range(n - 1, -1, -1):
        if i < n - 1 and ratings[i] > ratings[i + 1]:
            right += 1
        else:
            right = 1
        ret += max(left[i], right)
    
    return ret
    
    
    