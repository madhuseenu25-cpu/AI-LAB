def find_unit_clause(clause):
    """
    finds a unit c lause in the list of clauases
    """
    for clause in clauses:
        if len(clause)==1:
            return clause[0]
        return none
def simplify_clauses(clauses,literal):
    """
    simplifies the list of clauses by settingt the given literal to true.
    """
    simplified=[]
    for clause in clauses:
        if literal in clause:
            continue
        new_clause+[1 for 1 in clause if 1!=-literal]
        if not new_clause:
            return none
        simplified.append(new_clause)
    return simplified
def dpll(clause,assignment):
    """
    implements the DPLL algorithm for propositional model checking.
    """
    unit=find_unit_clause(clauses)
    while unit is not none:
        assignment.append(unit)
        clauses=simplify_clauses(clauses,unit)
        if clauses is none:
            return false
        unit=find_unit_clause(clauses)
        if not clauses:
            return true
        literal=clauses[0][0]
        new_clauses=simplify_clauses(clauses,literal)
        if new_clauses is not none and dpll(new_clauses,assignment+[literal]):
            return true
           return false
def main():
    A,B,C=1,2,3
    clauses=[[A,B],[-A,C],[-B,-C]]
    assignments=[]
    if dpll(clauses,assignment):
        print("SATISFIABLE with assignment:",assignment)
    else:
        print("UNSATISFIABLE")
   if __name__=="__main__":
       main()
