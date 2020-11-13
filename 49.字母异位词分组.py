#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for value in strs:
            key = ''.join(sorted(value))
            if key not in dic:
                dic[key] = [value]
            else:
                dic[key].append(value)
        result = []
        for key, value in dic.items():
            result.append(value)
        return result

# print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# @lc code=end

