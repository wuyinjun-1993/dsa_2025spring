#merge sort
#归并排序

def merge_sort(lst):#递归结束条件
    if len(lst)<=1:
        return lst
    # 分解问题，并递归调用
    middle=len(lst)//2
    left = merge_sort(lst[:middle]) #左半部排好序
    right = merge_sort(lst[middle:]) #右半部排好序
    
    #合并左右半部，完成排序
    merged=[]
    while left and right:
        if left[0]<= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged


