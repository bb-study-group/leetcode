from collections import deque
#bfs - fast
class Solution1:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:  return
        dir=[[1,0],[0,1],[-1,0],[0,-1]]
        i,j=0,0
        for d in dir:
            while True:
                q=[]
                if board[i][j]=='O':
                    q.append([i,j])
                while q:
                    ii,jj=q.pop()    
                    board[ii][jj]='R'
                    for dd in dir:
                        iii,jjj=ii+dd[0],jj+dd[1]
                        if 0<=iii<len(board) and  0<= jjj<len(board[0]) and board[iii][jjj] == 'O':
                            q.append([iii,jjj])
                if 0<=i+d[0]<len(board) and  0<= j+d[1]<len(board[0]):
                    i+=d[0]
                    j+=d[1]
                else:
                    break
        #print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='R':
                    board[i][j]='O'
                else:
                    board[i][j]='X'
#union find - slow
class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        if not board:  return
        parents={}
        dir=[[1,0],[0,1],[-1,0],[0,-1]]
        def find(coordinates):    
            if coordinates not in parents:
                parents[coordinates]=coordinates
            else:
                while coordinates!=parents[coordinates] and parents[coordinates]!=(-1,-1):
                    parents[coordinates]=parents[parents[coordinates]]
                    coordinates=parents[coordinates]
            return parents[coordinates]
        def union(c1, c2):
            p1,p2=find(c1),find(c2)
            parents[p2]=p1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    if (i,j) not in parents:
                        if i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1:
                            parents[(i,j)]=(-1,-1)
                        else:
                            parents[(i,j)]=(i,j)
                    for dd in dir:
                        ii, jj=i+dd[0], j+dd[1]
                        if 0<=ii<len(board) and  0<= jj<len(board[0]) and board[ii][jj] == 'O':
                            if ii==0 or ii==len(board)-1 or jj==0 or jj==len(board[0])-1:
                                union((-1,-1),(i,j))
                                union((i,j),(ii,jj))
                            else:
                                union((i,j),(ii,jj))
        #print(parents)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) in parents and find((i,j))==(-1,-1):
                    board[i][j]='O'
                else:
                    board[i][j]='X'
        """
