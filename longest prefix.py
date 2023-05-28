#! /usr/bin/env python 
def solution(strs):
        ans=""
        v=sorted(strs)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 

print(solution(["abab","aba","abc"]))
print(solution(["aaa","aa","aaa"]))
print(solution(["flower","flow","flight"]))
