class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        arr = []
        for item in stack:
            if item == '':
                continue
            elif item == '.':
                continue
            elif item == '..':
                if len(arr) > 0:
                    arr.pop()
            else:
                arr.append(item)
        ans = "/"
        for item in arr:
            ans+=(item + "/")
        return ans[:-1] if len(ans) > 1 else "/"