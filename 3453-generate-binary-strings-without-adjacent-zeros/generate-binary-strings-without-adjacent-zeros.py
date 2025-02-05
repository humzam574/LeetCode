class Solution:

    def validStrings(self, n: int) -> List[str]:

        if n == 0:
            return []
        
        if n == 1:
            return [ "0", "1" ]

        sub_val_strs = self.validStrings(n - 1)

        response = []
        for val_str in sub_val_strs:
            if val_str[0] == "0":
                response.append("1" + val_str)
            else:
                response.append("1" + val_str)
                response.append("0" + val_str)

        return response
        