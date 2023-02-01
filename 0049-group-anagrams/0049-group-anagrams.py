class Solution:
    def countSort(self, s: str):
        count_list = [0] * 26
        for c in s:
            count_list[ord(c) - 97] += 1
        result = ''
        for idx, count in enumerate(count_list):
            result += chr(idx + 97) * count
        return result
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = defaultdict(list)
        for cur_str in strs:
            print(cur_str)
            # sorted_str = ''.join(sorted(cur_str))
            sorted_str = self.countSort(cur_str)
            print(sorted_str)
            result_map[sorted_str].append(cur_str)    
        result = []
        for val in result_map.values():
            result.append(val)
        return result