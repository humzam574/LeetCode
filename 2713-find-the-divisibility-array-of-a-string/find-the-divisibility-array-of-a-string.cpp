class Solution {
public:
    vector<int> divisibilityArray(string word, int m) {
        const unsigned int wl = word.length();
        vector<int> ans;
        long num = 0;
        for (unsigned int i = 0; i < wl; i++) {
            num *= 10;
            num += word[i] - '0';
            num %= m;
            ans.push_back(num == 0);
        }
        return ans;
    }
};