
maxRoomArea = roomNum = roomArea = 0
def Dfs(i, k):
	global roomNum,roomArea
	if color[i][k]:
		return
	roomArea = roomArea + 1
	color[i][k] = roomNum
	if (rooms[i][k] & 1) == 0:  Dfs(i,k-1)   # 向西走
	if (rooms[i][k] & 2) == 0:  Dfs(i-1,k)   # 向北
	if (rooms[i][k] & 4) == 0:  Dfs(i,k+1)  # 向东
	if (rooms[i][k] & 8) == 0:  Dfs(i+1,k)  # 向南

RC = list( map( int, input().split() ) ) #输入格式和题目描述不一致
if len(RC) == 1:
	R = RC[0]
	C = int(input())
else:
	R, C = RC


rooms = [ [ ] ] #第0行没用
color = [ [ 0 for i in range(C+2)] for i in range(R+2) ]
for i in range(R):
	rooms.append( [0] + list( map( int, input().split() ) ))
for i in range(1,R+1):
	for k in range(1,C+1):
		if not color[i][k]:
			roomNum +=  1
			roomArea = 0
			Dfs(i,k)
			maxRoomArea = max(roomArea,maxRoomArea)
print( roomNum )
print( maxRoomArea )
