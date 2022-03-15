import numpy as np
def trasnformAugmentedMatrix(net, num) :
    A = np.full((len(net), num+1), 0)
    #코드 구현 부
    return A

networks = [['x1', 300, 'x2', 400],
            ['x2', 100, 'x3', 250],
            ['x3', 120, 'x4', 150],
            ['x4', 300, 'x1', 320]]
            
A = trasnformAugmentedMatrix(networks, 4)
print(A)
