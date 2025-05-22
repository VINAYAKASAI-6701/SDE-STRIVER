#User function Template for python3
class Solution:
    # Function to find if there exists a triplet in the array arr[] which sums up to target.
    def hasTripletSum(self, arr, target):
        # Your Code Here
        n=len(arr)
        arr.sort()
        res=[]
        for i in range(n):
            if i>0 and arr[i]==arr[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                s=arr[i]+arr[j]+arr[k]
                if s==target:
                    return True
                elif s<target:
                    j+=1
                else:
                    k-=1
        return False