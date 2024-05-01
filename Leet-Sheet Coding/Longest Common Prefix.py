'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        longest_prefix = ""
        flag = False
        if 1 <= len(strs) <= 200:
            if len(strs) == 1:
                longest_prefix += strs[0]
                return longest_prefix
            else:
                smallest_element = sorted(strs, key=len)[0]
                for j in range(0,len(smallest_element)):
                    temp_node = strs[0][j]
                    for i in range(1,len(strs)):
                        if strs[i][j] == temp_node:
                            flag = True
                        else:
                            flag = False
                            return longest_prefix
                    if flag:
                        longest_prefix += temp_node
                return longest_prefix
