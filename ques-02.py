class Solution:
    def pascal(self,row):
        ans = 1
        ansRow = [1] 
        #formula for sepcific row ans=prevans*(row-col)//col
        for col in range(1,row):
            ans*=(row-col)
            ans//=col
            ansRow.append(ans)
        return ansRow
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(1,numRows+1):
            ans.append(self.pascal(i))
        return ans