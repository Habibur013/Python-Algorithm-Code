#int(input("Enter the number of queen:"))
n=4
Q=[False]*n

solution=[]
def Qattack(Q,r):
    if(r==n):
        solution.extend(Q)
    else:
            for j in range (0,n):
                legal=True

                for i in range(0,r):
                    if(Q[i]==j) or (Q[i]==j+r-i) or (Q[i]==j-r+i):
                     legal=False
                if legal:
                    Q[r]=j
                    Qattack(Q,r+1)
Qattack(Q,0)


solution1=solution[:int(len(solution)/2)]

print(solution1)
board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

count=0
for i in solution1:
    board[count][i]='Q'
    count=count+1

print(board)
