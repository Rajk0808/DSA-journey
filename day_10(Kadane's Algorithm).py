#User function Template for python3

#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        sum = 0
        maxi = arr[0]
        for i in arr:
            sum +=i
            maxi = max(sum , maxi)
            if sum < 0:
                sum = 0
        return maxi    
