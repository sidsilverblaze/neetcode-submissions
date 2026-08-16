class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p_dict = {}
        for k in strs:
            s_str = "".join(sorted(k))
            if s_str in p_dict:
                p_dict[s_str].append(k)
            else:
                p_dict[s_str] = [k]
        return list(p_dict.values())