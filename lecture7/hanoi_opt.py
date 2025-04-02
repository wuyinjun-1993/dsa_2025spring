def moveTower(height,fromPole, withPole, toPole): 
#n个盘子从a移动到c,用b中转
	while height > 0:
		moveTower(height -1,fromPole, toPole, withPole)
		moveDisk(height, fromPole, toPole)
		height -= 1
		fromPole, withPole, toPole = withPole,fromPole,toPole

def moveDisk(disk,fromPole, toPole):
    print(f"Moving disk[{disk}] from {fromPole} to {toPole}")