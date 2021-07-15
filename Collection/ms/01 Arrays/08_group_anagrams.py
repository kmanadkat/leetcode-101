from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary
        dt = {}

        for item in strs:
            # Sort String
            sortedItem = "".join(sorted(item))

            # Check if sorted string in dictionary; "aet" : ["eat", "tea"]
            if sortedItem not in dt:
                dt[sortedItem] = [item]
            else:
                dt[sortedItem].append(item)

        return dt.values()
