import numpy as np
def trasnformAugmentedMatrix(net, num) :
    A = np.full((len(net), num+1), 0)
    for ridx, point in enumerate(net) :
        for cidx, p in enumerate(point) : 
            if type(p) is str :
                A[ridx][int(p.split('x')[1])-1] = 1 if cidx < num/2 else -1
            else :
                A[ridx][num] += -p if cidx < num/2 else p
    return A

networks = [['x1', 'x3', 'x2', 400],
            ['x2', 100, 'x3', 250],
            ['x3', 120, 'x4', 150],
            ['x4', 300, 'x1', 320]]

A = trasnformAugmentedMatrix(networks, 4)
print(A)
