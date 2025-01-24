class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, arr, ans = path.split("/"), [], "/"
        for item in stack:
            if item == '..': len(arr) > 0 and arr.pop()
            elif item != '' and item != '.': arr.append(item)
        for item in arr: ans+=(item + "/")
        return ans[:-1] if len(ans) > 1 else "/"