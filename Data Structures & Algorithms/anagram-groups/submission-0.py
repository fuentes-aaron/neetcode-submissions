class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) #mapping

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] +=1

            res[tuple(count)].append(s)

        return list(res.values())
        # O(m*n) didn't do this

        """
        for i in range (len(strs)):
            #print(i)
            for g in range (i+1,len(strs)):
                print(g)
        """

        
        

        