class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # if poured >= 4950:
        #     return 1
        #step 1: calculate topfill, how many cups are needed to be filled to make it to your row
        #step 2: poured-=topfill/(query_row-1) is the amount thats separated
        #some math to calculate the multiple
        #  1, 2, 1
        # 1, 3, 3, 1
        #1, 4, 6, 4, 1
        
        
        above = sum([i for i in range(query_row+1)])
        # query_row+=1
        # query_glass+=1
        # print("above: " + str(above))
        # if above >= poured:
        #     return 0
        #poured-=above
        #implement a dp to find the % amount that makes it to a given arr
        curr = [poured]
        for i in range(query_row):
            arr = [0] * (1+len(curr))
            for j in range(len(curr)):
                if curr[j] > 1:
                    arr[j]+=(curr[j]-1)/2
                    arr[j+1]+=(curr[j]-1)/2
            curr = arr
        # print(curr)
        return min(curr[query_glass], 1)
        