class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping = {str(i): str(j) for i, j in enumerate(mapping)}
        def sort_map(a: int) -> int: return int("".join(map(mapping.get, str(a))))
        return sorted(nums, key=sort_map)