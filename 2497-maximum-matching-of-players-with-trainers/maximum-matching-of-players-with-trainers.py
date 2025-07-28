class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        j, m = 0, len(players)
        for t in trainers:
            if j < m and players[j] <= t:
                j += 1
        return j