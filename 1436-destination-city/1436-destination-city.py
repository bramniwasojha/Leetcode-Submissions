class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hash1={}
        for city in paths:
            hash1[city[0]]=1
        for city in paths:
            if hash1.get(city[1],0)==0:
                return city[1]
        return