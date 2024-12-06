# Manan Arora
# 1002143328

from collections import defaultdict

class BayesianNetwork:
    def __init__(self, structure):
        self.structure = structure
        self.cpts = {}  # Conditional Probability

    def learn_cpts(self, data):
        counts = {}
        totals = {}

        for row in data:
            values = {var: row[idx] for idx, var in enumerate(self.structure.keys())}

            for var in self.structure:
                parent_values = tuple(values[parent] for parent in self.structure[var])

                if var not in counts:
                    counts[var] = {}
                
                if (values[var] , parent_values) not in counts[var]:
                    counts[var][(values[var], parent_values)] = 0
                counts[var][(values[var], parent_values)] += 1

                if (var, parent_values) not in totals:
                    totals[(var, parent_values)] = 0
                totals[(var, parent_values)] += 1

        for var in counts:
            self.cpts[var] = {}
            for (value, parent_values), count in counts[var].items():
                self.cpts[var][(value, parent_values)] = count/ totals[(var, parent_values)]

    def get_probability(self, var, value, parent_values):
        return self.cpts[var].get((value, parent_values), 0.0)
    
    def joint_probability(self, query):
        prob = 1.0
        for var in query:
            parent_values = [query[parent] for parent in self.structure[var]]
            prob *= self.get_probability(var, query[var], tuple(parent_values))
        return prob
    
    def inference_by_enumeration(self, query, evidence):
        hidden_vars = set(self.structure.keys()) - set(query.keys()) - set(evidence.keys())
        full_query = {**query, **evidence}

        def extend_query(curr_query, remaining_vars):
            if not remaining_vars:
                return [curr_query]
            next_var = remaining_vars.pop()
            extended_queries = []
            for value in [0, 1]:
                new_query = curr_query.copy()
                new_query[next_var] = value
                extended_queries.extend(extend_query(new_query, remaining_vars.copy()))
            return extended_queries
        
        all_queries = extend_query(full_query, hidden_vars.copy())
        numerator = sum(self.joint_probability(q) for q in all_queries)

        all_evidence = extend_query(evidence, hidden_vars.copy())
        denominator = sum(self.joint_probability(q) for q in all_evidence)

        return numerator / denominator if denominator > 0 else 0


def read_query(query):
    if "given" in query:
        parts = query.split("given")
        if len(parts) != 2:
            print("Inavlid format. Use <query variables> given <evidence variables>")
            return
        
        query_part = parts[0].strip()
        evidence_part = parts[1].strip()
    
    else:
        query_part = query.strip()
        evidence_part = None

    query = read_variables(query_part)
    if evidence_part:
        evidence = read_variables(evidence_part)
    else:
        evidence = {}

    if (query is None or (evidence_part and evidence is None)):
        print("Invalid variable format in the query or evidence")
        return

    return query, evidence

def read_variables(var_str):
    variables = {}

    # set for allowed variables
    allowed_vars = {"B", "G", "C", "F"}
    t_or_f = {"t", "f"}

    for var in var_str.split():
        if(len(var) != 2 or var[0] not in allowed_vars or var[1].lower() not in t_or_f):
            print(f"Invalid variable: {var}. Use format 'Bt', 'Bf', etc.")
            return
        variables[var[0]] = 1 if var[1] == 't' else 0
    
    return variables

def main():
    while True:
        query_str = input("Query: ").strip()
        if (query_str.lower()) == "none":
            print("Exiting program.")
            break

        query, evidence = read_query(query_str)
        if (query is not None):
            print(f"Parsed Query: {query}")
            print(f"Parsed Evidence: {evidence}")

if (__name__ == "__main__"):
    main()
    