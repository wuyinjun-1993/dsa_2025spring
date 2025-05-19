import collections
class step:
    def __init__(self,x,steps):
        self.x = x     #位置
        self.steps = steps   #到达x所需的步数
MAXN = 100000
N,K = map(int,input().split())
q = collections.deque()  #队列,即Open表
visited = [False] * (MAXN+10)
q.append(step(N,0))
visited[N] = True


while len(q) > 0:
    s = q.popleft()
    if s.x == K:  #找到目标
        print(s.steps)
        break
    else:
        if s.x - 1 >= 0 and not visited[s.x-1]:
            q.append(step(s.x-1,s.steps+1))
            visited[s.x-1] = 1
        if s.x + 1 <= MAXN and not visited[s.x+1]:
            q.append(step(s.x+1,s.steps+1))
            visited[s.x+1] = 1
        if s.x * 2 <= MAXN and not visited[s.x*2]:
            q.append(step(s.x*2,s.steps+1))
            visited[s.x*2]  = 1
