class Solution:
    def pushZerosToEnd(self,arr):
        # code here
        i = 0 
        j = 0
        n = len(arr)
        while i < n:
            if arr[i]!=0:
                arr[j] = arr[i]
                j+=1
            i+=1

        while j < n:
            arr[j] = 0
            j+=1
