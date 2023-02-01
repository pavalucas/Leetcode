class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = defaultdict(list)
        for cur_str in strs:
            print(cur_str)
            sorted_str = ''.join(sorted(cur_str))
            print(sorted_str)
            result_map[sorted_str].append(cur_str)    
        result = []
        for val in result_map.values():
            result.append(val)
        return result