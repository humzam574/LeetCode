class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        '''
        1. Find numbers that are common to all rows.
        2. Find numbers that are common to all cols.
        3. Find numbers that are common to 1 and 2 and get the minimum.
        '''
        ROWS = len(mat)
        COLS = len(mat[0])
        unique = set()
        
        
        def search(target: int, nums: List[int]) -> bool:
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right) //2
                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return False

        mini = mat[0][0]
        maxi = mat[0][COLS-1]
        for r in range(ROWS):
            mini = max(mini, mat[r][0])
            maxi = min(maxi, mat[r][COLS-1])
        for num in mat[0]:
            if mini <= num <= maxi:
                is_present = True
                for row in range(1, ROWS):
                    if not search(num, mat[row]):
                        is_present = False
                        break
                if is_present:
                    return num
        return -1