#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n = len(arr) - 1
        arr.sort()
        res = arr[n]-arr[0]
        for i in range(1,n+1):
            if arr[i]-k<0:
                continue
            minH = min(arr[i]-k,arr[0]+k)
            maxH = max(arr[i-1]+k,arr[n]-k)
            
            res = min(maxH-minH,res)
        return res    
