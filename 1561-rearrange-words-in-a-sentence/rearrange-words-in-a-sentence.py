class Solution:
    def arrangeWords(self, text: str) -> str: arr = sorted((chr(ord(text[0]) + ord('a') - ord('A')) + text[1:]).split(), key = lambda x : len(x)); arr[0] = chr(ord(arr[0][0]) - ord('a') + ord('A')) + arr[0][1:]; return ' '.join(arr)
        