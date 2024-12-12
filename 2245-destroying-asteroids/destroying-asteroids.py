class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        return all(mass := mass + a if mass >= a else False for a in sorted(asteroids))