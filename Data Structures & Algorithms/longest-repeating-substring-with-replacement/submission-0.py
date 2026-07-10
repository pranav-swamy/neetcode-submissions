class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        counts = defaultdict(int)
        maxfreq = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            maxfreq = max(maxfreq, counts[s[right]])

            # if window becomes invalid, move left to shrink the window
            while (right - left + 1) - maxfreq > k:
                counts[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result

            
