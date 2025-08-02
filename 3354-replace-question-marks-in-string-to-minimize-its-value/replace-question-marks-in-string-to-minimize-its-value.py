class Solution:
    def minimizeStringValue(self, s: str) -> str:
        heap = [[0, i] for i in range(26)]
        #arr = [[0, i] for i in range(26)]
        q = 0
        for c in s:
            if c == "?":
                q+=1
            else:
                idx = ord(c) - 97
                heap[idx][0] += 1
        heapify(heap)
        arr = [0 for i in range(26)]
        for i in range(q):
            val, idx = heappop(heap)
            heappush(heap, [val+1, idx])
            arr[idx]+=1
        # print(arr)
        # heapify(arr)
        #ans = 0
        ans = []
        ptr = 0
        #heap = list(heap)
        #heap.sort(key = lambda x : x[1])
        for char in s:
            # c = chr(idx + 97)
            # for x in range(a):
            #     ans.append(c)
            if char != "?":
                ans.append(char)
            else:
                # c,i = heappop(arr)
                # ans.append(i)
                # heappush(arr, [c+1, i])
                while ptr < 26 and arr[ptr] == 0:
                    ptr+=1
                ans.append(chr(ptr + 97))
                arr[ptr]-=1
        
        return ''.join(ans)