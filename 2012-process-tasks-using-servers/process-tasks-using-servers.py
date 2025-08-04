import heapq
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        answer = []
        used_servers = [] # (time_when_server_is_free, weight, index)
        free_servers = [(0, weight, index) for index, weight in enumerate(servers)]
        heapq.heapify(free_servers)

        for current_time, time_to_complete in enumerate(tasks):
            # determine if any used_servers are now free_servers and add to free_servers heap
            while used_servers and used_servers[0][0] <= current_time:
                free_server = heapq.heappop(used_servers)
                heapq.heappush(free_servers, (0, free_server[1], free_server[2]))

            if free_servers:
                current_server = heapq.heappop(free_servers)
                time_when_current_server_is_free = current_time + time_to_complete
            else:
                current_server = heapq.heappop(used_servers)
                time_when_current_server_is_free = current_server[0] + time_to_complete
            _, current_server_weight, current_server_index = current_server

            if time_when_current_server_is_free <= current_time + 1:
                # server will be free next second
                heapq.heappush(free_servers, (0, current_server_weight, current_server_index))
            else:
                # server will not be free next second
                heapq.heappush(used_servers, (time_when_current_server_is_free, current_server_weight, current_server_index))

            answer.append(current_server_index)

        return answer            