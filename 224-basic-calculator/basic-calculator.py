class Solution:
    def calculate(self, s: str) -> int:
        p1 = []
        dict = {"-": -1, "+": 1}
        for char in s:
            if char == ' ':# or char == '(' or char == ')':
                continue
            if char.isdigit() and p1 and p1[-1].isdigit():
                p1[-1]+=char
            else:
                p1.append(char)
        undo = [1] * (len(p1) + 1)
        order = []
        for i, char in enumerate(p1):
            if char == "(":
                if i > 0 and p1[i - 1] == "-":
                    undo[i] = undo[i - 1] * (-1)
                    order.append(-1)
                else:
                    order.append(1)
                    undo[i] = undo[i - 1]
            elif char == ")":
                undo[i] = undo[i - 1] * order.pop()
            else:
                undo[i] = undo[i - 1]
        # print(p1)
        # print(undo)
        # for i in range(len(p1)):
        #     print(str(i) + ": " + str(p1[i]) + " " + str(undo[i]))
        #     #print(str(p1[i]) + " " + str(undo[i]))
        # print()
        ans = 0
        prev = 1
        for i in range(len(p1)):
            if p1[i] == "(" or p1[i] == ")":
                prev = 1
                continue
            elif p1[i] == "-":
                prev = -1
            elif p1[i] == "+":
                prev = 1
            else:
                ans = ans + (int(p1[i]) * prev * undo[i])
            #print(str(i) + " " + str(ans))
        return ans

            