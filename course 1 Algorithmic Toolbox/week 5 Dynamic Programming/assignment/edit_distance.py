# Uses python3

def edit_distance(s, t):
    #write your code here
    ns = len(s)
    nt = len(t)
    dis_mat = [[0]*(ns+1) for i in range(nt+1)]
    for i in range(ns+1):
        dis_mat[0][i] = i
    for i in range(nt+1):
        dis_mat[i][0] = i
    
    for i in range(1,nt+1):
        for j in range(1,ns+1):
            if t[i-1]==s[j-1]:
                cost = 0
            else:
                cost = 1
            dis_mat[i][j] = min((dis_mat[i-1][j]+1),(dis_mat[i][j-1]+1),(dis_mat[i-1][j-1]+cost))
    
    return dis_mat[nt][ns]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
