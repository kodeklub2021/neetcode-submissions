class Solution:
    def findnum(self,arr,target):
        if len(arr) == 1:
            return target == arr[0]
        l = 0
        r = len(arr)

        while l < r:
            print(arr[l:r])
            mid = (l+r)//2
            if arr[mid] > target:
                r = mid
            elif arr[mid] < target:
                l = mid + 1
            else:
                return True
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0,len(matrix)):
            if matrix[i][-1] >= target:
                if self.findnum(matrix[i],target):
                    return True
        return False
        