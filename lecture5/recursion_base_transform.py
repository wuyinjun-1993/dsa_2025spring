def tostr(n,base):
    convertstring="0123456789ABCDEF"
    if n < base :
        return convertstring[n]

    else:
        return tostr(n//base, base)+ convertstring[n%base]

print(tostr(1453, 16))