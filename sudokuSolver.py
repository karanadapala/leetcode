class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        

        self.preFillrows(board)
        self.preFillcols(board)
        self.preFillrows(board)
        self.preFillcols(board)
        self.solve(board)
        print(board)
        

    def possible(self,x,y,n, grid):
        for index in range(9):
            if (grid[x][index] == str(n)) or (grid[index][y]==str(n)):
                return False
        xo = int(x/3)*3
        yo = int(y/3)*3
        for xx in range(xo,xo+3):
            for yy in range(yo,yo+3):
                if grid[xx][yy]==str(n):
                    return False
        return True

    def preFillrows(self,preFillD):
        for preFillnum in range(1,10):
            for preFillsplit in range(3):
                preFillCount = 0
                tempx =3*preFillsplit
                tempy = 3*preFillsplit+3
                matColindex = 0
                for preFillx in range(tempx, tempy):
                    if str(preFillnum) in preFillD[preFillx]:
                        preFillCount += 1
                        matColindex -= int(preFillD[preFillx].index(str(preFillnum))/3)
                    else:
                        tempz = preFillx
                matCol = 3 + matColindex
                if preFillCount == 2:
                    preFillCal = 0
                    for preFilly in range(matCol*3,matCol*3+3):
                        if preFillD[tempz][preFilly] == '.':
                            if self.possible(tempz,preFilly,preFillnum, preFillD):
                                preFillCal += 1
                                fillx = tempz
                                filly = preFilly
                    if preFillCal==1:
                        preFillD[fillx][filly] = str(preFillnum)
        return preFillD

    def preFillcols(self,preFillD):
        for preFillnum in range(1,10):
            for preFillsplit in range(3):
                preFillCount = 0
                tempx =3*preFillsplit
                tempy = 3*preFillsplit+3

                for preFillx in range(tempx, tempy):
                    matRowindex = 0

                    for temprow in range(9):
                        if str(preFillnum) == preFillD[temprow][preFillx]:
                            preFillCount += 1
                            matRowindex +=0
                    if matRowindex== 0:
                        tempz = preFillx
                tempz = int(tempz/3)*3
                if preFillCount == 2:
                    preFillCal = 0
                    for preFilly in range(9):
                        for preFilltemp in range(tempz, tempz+3):

                            if preFillD[preFilly][preFilltemp] == '.':
                                if self.possible(preFilly,preFilltemp,preFillnum, preFillD):
                                    preFillCal += 1
                                    filly = preFilltemp
                                    fillx = preFilly
                    if preFillCal==1:
                        preFillD[fillx][filly] = str(preFillnum)
        return preFillD

    
    def postPrefill(preFillD):
        for postPrefillnum in range(1,10):
            for postx in range(3):
                xIndex = postx*3
                for posty in range(3):
                    yIndex=posty*3
                    postPrefillCount = 0
                    for subMatx in range(xIndex, xIndex+3):
                        
                        for subMaty in range(yIndex, yIndex+3):
                            if preFillD[subMatx][subMaty]=='.':
                                if possible(subMatx,subMaty,postPrefillnum, preFillD):
                                    print(postPrefillnum, subMatx, subMaty)
                                    postPrefillCount +=1
                                    tempX = subMatx
                                    tempY = subMaty
                    if postPrefillCount == 1:
                        preFillD[tempX][tempY] = str(postPrefillnum)
                        #driver.find_element_by_id('f{}{}'.format(tempY,tempX)).send_keys('{}'.format(postPrefillnum))
        return preFillD


    def solve(self,grid):
        for solx in range(9):
            for soly in range(9):
                if grid[solx][soly] == '.':
                    for num in range(1,10):
                        if self.possible(solx,soly, num, grid):
                            grid[solx][soly] = str(num)
                            self.solve(grid)
                            count = 0
                            for tt in grid:
                                if '.' not in tt:
                                    count += len(tt)
                                if count == 81:
                                    return
                            grid[solx][soly] = '.'
                    return
        #print(np.matrix(grid))

x = Solution()
print(x.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
)) 

        


    