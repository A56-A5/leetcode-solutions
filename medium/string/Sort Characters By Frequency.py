class Solution:
    def frequencySort(self, s):
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        items = list(freq.items())
        items.sort(key=lambda item: item[1], reverse=True)

        result = ""
        for ch, count in items:
            result += ch * count

        return result
