import itertools

class propositionalLogic:
    def __init__(self):
        self.clauses=[]
    def add_clause(self,clause):
        self.clause.append(clause)
    def pl_resolution(self):
        """perform propositional logic resolution to determine satisfiability."""
        new=set()
        while true:
            mn=len(self.clause)
            pairs=[(self.clause[i],self.clause[j],for i in range(n) for j in range(i+1,n)]
            for (ci,cj)in pairs
                   resolvents=self.pl_resolve(ci,cj)
                   if[] in resolvents:
                       return false
                    for res in resolvents:
                        new.add(tuple(res))
            if new.issubset(set(map(tuple,self.clause))):
                return true
            for clause in new:
                if list(clause)not in self.clauses:
                    self.clause.append(list(clause))
            new=ser()
    def pl_resolve(self,ci,cj):
        """resolve two clause to produce a set of resolvents."""
        resolvents=[]
        for di in ci:
            for dj in cj:
                if di==dj:
                    resolvents=list(set(ci)-{di})+list(set(cj)-{dj})
                    resolvents.append(resolvent)
            return resolvents
    pl=propositionalLogic
    pl.add_clause([1,2])
    pl.add_clause([-1,3])
    pl.add_clause([-2,-3])
    is_satisfiable=pl.pl_resolution()
    if is_satisfiable:
        print("the knowledge base is satisfiable.")
    else:
        print("the knowledge base is not satisfiable.")
