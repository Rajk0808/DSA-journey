class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        indx = -1
        for i in range(n-1,-1,-1):
            if arr[i-1] < arr[i]:
                indx = i-1
                break
        if indx == -1:
            return arr.reverse()
        for i in range(n-1,indx,-1):
            if arr[indx] < arr[i]:
                arr[indx] , arr[i] = arr[i] , arr[indx]
                break
        arr[indx+1:] = reversed(arr[indx+1:])   
        
        return arr  
