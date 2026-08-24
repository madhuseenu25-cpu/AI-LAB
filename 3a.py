def unify(x,y,subst={}):
    if x==y:
        return subst
    elif isinstance(x,str)and x.islower():
        return{x:y}
    elif isinstance(y,str)and y.islower():
        return{y:x}
    else:
        return none
def resolve(c1,c2):
    for lit1 in c1:
        for lit2 in c2:
            if lit1=="~"+lit2 or "~"+lit1== lit2:
                new_clause=list(set(c1+c2)-{lit1,lit2})
                return new_clause
    return none
def resolution(kb,query):
    clauses=kb=[["~"+q for q in query]]
    while true:
         new_clause=[]
         for i in range(len(clauses)):
            for j in range(i+1,len(clauses)):
                resolvent=resolve(clauses[i],clauses[j])
                if resolvent is not none:
                    if not resolvent:
                        return true
                    new_clauses.append(resolvent)
      if not any(cl not in clauses for cl in new_clauses):
         return false
        clauses.extend(new_clauses)
     kb=[
       ["P(a)"],
       ["~P(a)","Q(a)"]
     ]
     query=["Q(a)"]
     if resolution(kb,query):
         print("query is entailed by the knowledge base.")
     else:
         print("query is not entailed by the knowledge base.")
               
