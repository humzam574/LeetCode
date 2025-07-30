class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        heap = []
        for a, b in zip(aliceValues, bobValues):
            heappush(heap, (-abs(a+b), a, b))
        alice = 0
        bob = 0
        turn = True
        # for h in heap:
        #     print(h)
        while heap:
            _, a, b = heappop(heap)
            # print("a: " + str(a) + ", b: " + str(b) + ", turn = " + str(turn))
            if turn:
                turn = False
                alice+=a
                # print("alice: " + str(alice))
            else:
                turn = True
                bob+=b
                # print("bob: " + str(bob))
        # print(alice)
        # print(bob)
        return 1 if alice > bob else (-1 if bob > alice else 0)