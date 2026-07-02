class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_of_list = {}
        for i in strs:
            dict_key = "".join(sorted(i))

            if dict_key not in dict_of_list:
                dict_of_list[dict_key]=[]

            dict_of_list[dict_key].append(i) 
        return list(dict_of_list.values())

