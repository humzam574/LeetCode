class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(" ")
        words[0] = words[0].lower()
        max_length = max([len(word) for word in words])
        buckets = [[] for _ in range(max_length + 1)]
        for word in words:
            buckets[len(word)].append(word)
        res = []
        for bucket in buckets:
            res.extend(bucket)
        res[0] = res[0].capitalize()
        return " ".join(res)