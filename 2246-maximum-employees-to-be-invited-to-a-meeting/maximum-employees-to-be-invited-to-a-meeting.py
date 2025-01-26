class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        visited_time = [0] * n
        the_time = 1
        ans = 0
        dd_node_dict = {}
        for i in range(n):
            if visited_time[i]:
                continue
            start = the_time
            tmp = i
            visited_time[tmp] = the_time
            while not visited_time[favorite[tmp]]:
                the_time += 1
                tmp = favorite[tmp]
                visited_time[tmp] = the_time
            the_time += 1
            circle_end = favorite[tmp]
            if visited_time[circle_end] >= start:
                new_circle = the_time-visited_time[circle_end]
                ans = max(ans, new_circle)
                if new_circle == 2:
                    dd_node_dict[tmp] = {
                        'l': [0] * n,
                        'r': [0] * n
                    }
                    start_idx = i
                    for back_time in range(start, the_time):
                        dd_node_dict[tmp]['l'][start_idx] = the_time - back_time - 1
                        start_idx = favorite[start_idx]
                    dd_node_dict[tmp]['r'][tmp] = 1
            else:
                for dd_node in dd_node_dict:
                    for k in ['l', 'r']:
                        if dd_node_dict[dd_node][k][circle_end] > 0:
                            start_idx = i
                            for back_time in range(start, the_time):
                                dd_node_dict[dd_node][k][start_idx] = the_time - back_time + dd_node_dict[dd_node][k][circle_end]
                                start_idx = favorite[start_idx]
        dd_link_num = 0
        for dd_node in dd_node_dict:
            dd_link_num += max(dd_node_dict[dd_node]['l']) + max(dd_node_dict[dd_node]['r'])

        return ans if ans > dd_link_num else dd_link_num
                
                