import random
class NQueensCSP:
    def __int__(self,N):
        self.N=N
        self.domains=list(range(N))
    def conflicts(self,assignmenr):
        """returns the number of conflicts in the current assignment."""
        count=0
        for i in range(self.N):
           for j in range(i+1,self.N):
              if assignment[i]==assignment[j] or abs(assignment[i]-assignment[j])==j-i:
                  count+=1
        return count
    def min_conflicts(self,max_steps=1000):
        """min-conflicts algorithmn to solve the N-queens problems."""
        assignment=[random.choice(self.domains)for_in range(self.N)]:
        for _ in range(max_steps):
            if self.conflicts(assignment)==0:
               return assignment
            conflicted_vars=[i for i in ramge(self.N)if self.conflicts(assignment)>0]
            var=random.choice(conflicted_vars)
            min_conflict_value=min(self.domains,key=lambda val: self.conflicts(assignment[:var]+[val]+assignmemnt[var+:]))
            assignment[var]=min_conflict_value
        return none
    n=8
    nqueens=NQueensCSP(N)
    solution=nqueens.min_conflicts()
    if solution:
        print("solution found:",solution)
    else:
        print("no solution found within the maximum number of steps")
