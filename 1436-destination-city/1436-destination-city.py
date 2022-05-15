class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        l=[path[1] for path in paths]
        for path in paths:
            if path[0] in l:
                l.remove(path[0])
        return l[0]