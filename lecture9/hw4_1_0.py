def solve():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    while True:
        n = int(input[ptr])
        ptr += 1
        if n == 0:
            break
        sticks = list(map(int, input[ptr:ptr+n]))
        # sticks.sort(reverse=True)
        ptr += n
        
        total = sum(sticks)
        max_len = max(sticks)
        
        # Generate possible L's in ascending order
        possible_Ls = []
        for L in range(max_len, total + 1):
            if total % L == 0:
                possible_Ls.append(L)
        
        # Check each L in ascending order
        for L in possible_Ls:
            k = total // L
            used = [False] * n
            if can_form(0, k, L, sticks, used):
                print(L)
                break

def can_form(current_len, remaining, target, sticks, used):
    if remaining == 0:
        return True
    if current_len == target:
        return can_form(0, 0, remaining - 1, target, sticks, used)

    for i in range(0, len(sticks)):
        if not used[i] and current_len + sticks[i] <= target:
            used[i] = True
            if can_form(current_len + sticks[i], remaining, target, sticks, used):
                return True
            used[i] = False

    return False

solve()

