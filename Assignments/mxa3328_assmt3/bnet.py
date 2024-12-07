# Manan Arora
# 1002143328

import sys

class BayesianNetwork:
    def __init__(self, structure):
        self.structure = structure
        self.cpts = {}

    def learn_cpts(self, data):
        counts = {}
        totals = {}

        for values in data:
            for var in self.structure:
                parent_values = tuple(values[parent] for parent in self.structure[var])

                if var not in counts:
                    counts[var] = {}
                
                if (values[var], parent_values) not in counts[var]:
                    counts[var][(values[var], parent_values)] = 0
                counts[var][(values[var], parent_values)] += 1

                if (var, parent_values) not in totals:
                    totals[(var, parent_values)] = 0
                totals[(var, parent_values)] += 1

        for var in counts:
            self.cpts[var] = {}
            for (value, parent_values), count in counts[var].items():
                self.cpts[var][(value, parent_values)] = count / totals[(var, parent_values)]

    def get_probability(self, var, value, parent_values):
        return self.cpts[var].get((value, parent_values), 0.0)
    
    def joint_probability(self, assignment):
        prob = 1.0
        for var in self.structure:
            parent_values = tuple(assignment[parent] for parent in self.structure[var])
            prob *= self.get_probability(var, assignment[var], parent_values)
        return prob
    
    def inference_by_enumeration(self, query, evidence):
        all_vars = set(self.structure.keys())

        hidden_vars = all_vars - set(query.keys()) - set(evidence.keys())

        full_query = {**query, **evidence}

        def extend_and_sum(curr_query, remaining_vars):
            if not remaining_vars:
                return self.joint_probability(curr_query)

            next_var = remaining_vars.pop()
            total_prob = 0.0

            for value in [0, 1]:
                curr_query[next_var] = value
                total_prob += extend_and_sum(curr_query.copy(), remaining_vars.copy())
            return total_prob

        numerator = extend_and_sum(full_query.copy(), list(hidden_vars))

        evidence_query = evidence.copy()
        denominator = extend_and_sum(evidence_query, list(hidden_vars | set(query.keys())))

        if denominator == 0:
            print("Error: Denominator (P(evidence)) is 0. Cannot compute conditional probability.")
            return 0

        return numerator / denominator

def read_query(query):
    if "given" in query:
        parts = query.split("given")
        if len(parts) != 2:
            print("Invalid format. Use <query variables> given <evidence variables>")
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

    allowed_vars = {"B", "G", "C", "F"}
    t_or_f = {"t", "f"}

    for var in var_str.split():
        if len(var) != 2 or var[0] not in allowed_vars or var[1].lower() not in t_or_f:
            print(f"Invalid variable: {var}. Use format 'Bt', 'Bf', etc.")
            return
        variables[var[0]] = 1 if var[1] == 't' else 0
    
    return variables

def read_training_data(file_path):
    with open(file_path, "r") as file:
        data = [list(map(int, line.strip().split())) for line in file.readlines()]
    
    mapped_data = [{"B": row[0], "G": row[1], "C": row[2], "F": row[3]} for row in data]
    return mapped_data

def main():
    if len(sys.argv) != 2:
        print("Usage: python bnet.py <training_data_file>")
        sys.exit(1)

    training_data_file = sys.argv[1]

    structure = {
        "B": [],
        "G": ["B"],
        "C": [],
        "F": ["G", "C"]
    }

    bnet = BayesianNetwork(structure)

    try:
        training_data = read_training_data(training_data_file)
    except FileNotFoundError:
        print(f"Error: File '{training_data_file}' not found.")
        sys.exit(1)

    bnet.learn_cpts(training_data)

    while True:
        query_str = input("Query: ").strip()
        if query_str.lower() == "none":
            print("Exiting program.")
            break

        query, evidence = read_query(query_str)
        if query is not None:
            probability = bnet.inference_by_enumeration(query, evidence)
            print(f"Probability: {probability:.10f}")

if __name__ == "__main__":
    main()
