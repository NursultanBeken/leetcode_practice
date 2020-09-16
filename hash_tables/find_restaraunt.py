class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map = {}
        result = []
        min_sum = len(list2) + len(list1)
        for ix, value in enumerate(list1):
            hash_map[value] = ix
        for ix, value in enumerate(list2):
            if value in hash_map:
                index_sum = ix + hash_map[value]
                if index_sum < min_sum:
                    result.clear()
                    result.append(value)
                    min_sum = index_sum 
                elif index_sum == min_sum:
                    result.append(value)
        return result