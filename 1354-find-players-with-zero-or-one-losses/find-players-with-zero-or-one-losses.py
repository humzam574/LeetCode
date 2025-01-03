class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        no_losses = set()
        one_loss = set()
        losers = set()

        for (winner, loser) in matches:
            if (winner not in losers and winner not in one_loss):
                no_losses.add(winner)

            if (loser in no_losses):
                no_losses.remove(loser)
                one_loss.add(loser)

            elif (loser in one_loss):
                one_loss.remove(loser)
                losers.add(loser)
            
            elif (loser not in losers):
                one_loss.add(loser)
        
        winners = sorted(list(no_losses))
        one_loss = sorted(list(one_loss))

        return [winners, one_loss]