class Solution:
    def countSort(self, s: str):
        count_map = defaultdict(int)
        alphabet = list(string.ascii_lowercase)
        for c in s:
            count_map[c] += 1
        result = ''
        for let in alphabet:
            if let in count_map:
                result += let * count_map[let]
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