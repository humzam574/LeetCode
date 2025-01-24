class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, arr = path.split("/"), []
        for item in stack:
            if item == '..': len(arr) > 0 and arr.pop()
            elif item != '' and item != '.': arr.append(item)
        return "/" + "/".join(arr)