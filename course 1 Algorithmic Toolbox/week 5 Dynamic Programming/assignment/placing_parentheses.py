# Uses python3

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i,j,nums,ops,m,M):
    min_val = float('inf')
    max_val = float('-inf')
    
    val_sel = []
    for k in range(i,j):
        opk = ops[k]
        val_sel.append(evalt(M[i][k], M[k+1][j], opk))
        val_sel.append(evalt(M[i][k], m[k+1][j], opk))
        val_sel.append(evalt(m[i][k], M[k+1][j], opk))
        val_sel.append(evalt(m[i][k], m[k+1][j], opk))
    
    new_min = min(val_sel)
    new_max = max(val_sel)
    
    min_val = min(min_val,new_min)
    max_val = max(max_val,new_max)
    return (min_val,max_val)
    
def get_maximum_value(dataset):
   
    nums = list(map(int,dataset[::2]))
    ops = dataset[1::2]
    
    n = len(nums)
    M = [[0]*n for i in range(n)]
    m = [[0]*n for i in range(n)]
    for i in range(n):
        M[i][i] = nums[i]
        m[i][i] = nums[i]
    
    for s in range(1,n):
        for i in range(n-s):
            j = i+s
            m[i][j],M[i][j] = MinAndMax(i,j,nums,ops,m,M)
            
    return M[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
