class Solution:
    def reverseArray(self, arr):
        # code here
        n = len(arr)
        if n == 1:
            return arr
        for i in range(n//2):
            arr[i],arr[-(i+1)] = arr[-(i+1)],arr[i]
        return arr
        
        
