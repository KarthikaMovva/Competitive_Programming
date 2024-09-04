from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        result = []
        target_p_count = Counter(p)
        string_count = Counter()

        target_p_length = len(p)

        for i in range(len(s)):
            string_count[s[i]] += 1

            if i >= target_p_length:
                if string_count[s[i - target_p_length]] == 1:
                    del string_count[s[i - target_p_length]]
                else:
                    string_count[s[i - target_p_length]] -= 1
            if string_count == target_p_count:
                result.append(i - target_p_length + 1)

        return result
        