class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = 0
        n_len = len(nums)

        # Loop over n from 1 to 50
        for n in range(1, 51):
            # cnt will store partial results from the left
            cnt = [0]*(n_len + 1)
            edge = 0
            cnt_k = 0   # How many k's seen in the current segment
            cnt_n = 0   # How many n's seen in the current segment

            # Pass from left to right
            for i in range(n_len):
                if nums[i] == k:
                    cnt_k += 1
                if nums[i] == n:
                    cnt_n += 1

                # If we have at least as many k's as n's, absorb them into `edge`
                if cnt_k >= cnt_n:
                    edge += cnt_k
                    cnt_k = 0
                    cnt_n = 0

                cnt[i + 1] = edge + cnt_n

            # Pass from right to left
            edge = 0
            cnt_k = 0
            cnt_n = 0

            for i in range(n_len - 1, -1, -1):
                if nums[i] == k:
                    cnt_k += 1
                if nums[i] == n:
                    cnt_n += 1

                if cnt_k >= cnt_n:
                    edge += cnt_k
                    cnt_k = 0
                    cnt_n = 0

                # Update result using cnt[i] (from the left pass) plus what we have built from the right
                res = max(res, cnt[i] + edge + cnt_n)

        return res