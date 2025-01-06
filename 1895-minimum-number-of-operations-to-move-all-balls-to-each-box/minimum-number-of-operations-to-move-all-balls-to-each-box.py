class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # 001011
        #left  = 0, 0, 0, 1, 1, 2
        #right = Q, 3, 3, 2, 2, 1
        #combo = Q,-3,-3,-1,-1,1


        # 110
        #left  = Q, 1, 2
        #right = Q, 1, 0

        #combo = Q, 0, 2

        #dont include for left
        #do include for right

        #right = boxes.count('1')
        left = int(boxes[0] == "1")
        #curr = sum(i if boxes[char] == '1' else 0 for i, char in enumerate(boxes))
        right = -1 * (boxes[0] == "1")
        curr = 0
        for i, char in enumerate(boxes):
            if char == '1': right, curr = right + 1, curr + i
        ans = [curr] + [0] * (len(boxes) - 1)
        for i in range(1, len(ans)):
            ans[i] = ans[i - 1] - right + left
            #print(str(right) + " " + str(left))
            if boxes[i] == '1':
                right -= 1
                left += 1
            # if boxes[i - 1] == '1':
            #     left += 1
            
        return ans
