class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count ={} #dictionary
        for i in nums:
            count[i] = count.get(i,0) + 1 # if num has 0 add it and add 1
        sortedc = sorted(count, key=count.get, reverse=True)
        print(sortedc)
        return sortedc[:k]
        """  
        for g in count:
            if count[g] >= k:
                tmp.append(g)

        return tmp
"""



        