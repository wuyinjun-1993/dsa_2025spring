#作者：北京大学 郭炜  版权所有 未经授权不得复制 copyright：Guo Wei, Peking University
#程序来自中国水利水电出版社《数据结构与算法(Python语言实现)》教材(作者：郭炜)
#程序在书中有详细注释和讲解

def isPopSeq(s1,s2):
	stack = []
	if len(s1) != len(s2):
		return False
	else:
		L = len(s1)
		stack.append(s1[0])
		p1,p2 = 1,0
		while p1 < L:
			if len(stack) > 0 and stack[-1] == s2[p2]:
				stack.pop()
				p2 += 1
			else:
				stack.append(s1[p1])
				p1 += 1
		return "".join(stack[::-1]) == s2[p2:]
s1 = input()
while True:
	try:
		s2 = input()
	except:
		break
	if isPopSeq(s1,s2):
		print("YES")
	else:
		print("NO")

