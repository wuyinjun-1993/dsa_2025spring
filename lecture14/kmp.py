

def kmp(a,b,Next):#a是母串，b是子串
	La,Lb = len(a),len(b)
	pa = pb = 0 #母串指针和子串指针
	while pa < La and pb < Lb:
		if pb == -1 or a[pa] == b[pb]:
			#pb==-1说明b[0]失配,因为只有next[0]才为-1
			pa,pb = pa + 1,pb + 1
		else:
			pb = Next[pb] #执行次数不会多于ps+1的执行次数，即pa+1次数
	if pb == Lb:
		return pa - pb
	return -1


def countNext(b):
	i,k,Lb = 0,-1,len(b)
	Next = [-1 for i in range(Lb)]
	while i < Lb - 1:
		if k == -1 or b[i] == b[k]:
			Next[i+1] = k + 1
			i,k = i + 1,k + 1
		else:
			k = Next[k]
	return Next



def countNext2(b):
	i, k, L = 0, -1, len(b)  # 开始k就是Next[0]
	Next = [-1] * L
	while i < L - 1:
		if k == -1 or b[i] == b[k]: 
			if b[i+1] == b[k+1]:  
				Next[i+1] = Next[k+1]
			else: 
				Next[i+1] = k+1
			i, k = i + 1, k + 1
		else:
			k = Next[k]
	return Next
