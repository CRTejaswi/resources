"""
Python3: UVa10026 - Shoemaker's Problem
 Refer: https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=967
"""
class job:
    def __init__(self,id,duration,fineRate):
        self.id = id
        self.duration = duration
        self.fineRate = fineRate
    def __lt__(self, other):
        return(self.duration * other.fineRate < other.duration * self.fineRate)
    def __repr__(self):
        return(str(self.id))

N = int(input()) 
jobs = []
for i in range(N):
    T,S = [int(x) for x in input().split(' ',maxsplit=1)]
    jobs.append(job(i+1,T,S))
    print(jobs)
print(jobs)
print(' '.join([str(x) for x in sorted(jobs)]))

"""
Note
 1. Problem statement is slightly altered by NPTEL
 2. Make changes if large inputs are drawn from a txt file 
"""
