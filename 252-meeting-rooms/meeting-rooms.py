class Solution:
    def canAttendMeetings(self, v): v.sort(key = lambda x : x[0]); return all(v[i][1] <= v[i+1][0] for i in range(len(v) - 1))