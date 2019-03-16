class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis = []
        for num in nums:
            if not lis or num>lis[-1]:
                lis.append(num)
            else:
                l, r = 0, len(lis)
                while l !=r :
                    m = (l + r)//2
                    if num <= lis[m]:
                        r = m
                    else:
                        l = m + 1
                if lis[l] > num:
                    lis[l] = num
                
        return len(lis)
