import hashlib

# 每次读取的字节数
blk_size=2048
m=hashlib.md5()# 创建一个散列函数对象
with open("2004-199.pdf","rb") as f:
    while True:
        buf = f.read(blk_size)
        if not buf:
            break
        m.update(buf) #更新

print(m.hexdigest())

