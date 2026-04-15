class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # returns list of lists, each list containing words that are anagrams
        # init defaultdict(), dict that resolves missing keys
        # specify type of value, list is default value
        dd = defaultdict(list)

        for s in strs:
            # stores numOccurences for each char, index mapped to letter
            wcount = [0] * 26

            for c in s:
                wcount[ord(c) - ord('a')] += 1

            # append string s to key's value = list of strings
            # key is wcount typecasted to tuple, only immutable types can be keys
            dd[tuple(wcount)].append(s)

        # returns list containing all values, each value is a list of strings that are anagrams of eachother
        return list(dd.values())
