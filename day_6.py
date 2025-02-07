class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        a = b = 0 
        n = len(arr)
        result  = []
        c1 = c2 = 0
        for i in arr:
            if i==a:
                c1+=1
            elif i == b:
                c2+=1
            elif c1 == 0:
                a = i
                c1 = 1
            elif c2 == 0:
                b = i
                c2 = 1
            else:
                c1-=1
                c2-=1
        c1 = c2 = 0        
        for i in arr:
            if i == a:
                c1+=1
            elif i == b:
                c2+=1
        if c1>n/3:
            result.append(a)
        if c2>n/3:
            result.append(b)
        result.sort()    
        return result if len(result) > 0 else []    
