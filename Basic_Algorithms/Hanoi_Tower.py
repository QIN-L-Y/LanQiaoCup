def move(start, bridge, goal, n): #从start移动n个到goal，借助bridge
    if n == 1:
        print(start, '->', goal)
    else:
        move(start, goal, bridge, n - 1)
        print(start, '->', goal)
        move(bridge, start, goal, n - 1)

move('a', 'b', 'c', 3)