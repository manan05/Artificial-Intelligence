Name: Manan Arora
UTA ID: 1002143328

Programming Language Used: Python 3.9.7

Code Structure:

1. learn_cpts(data): Learns Conditional Probability Tables (CPTs) from the training data. Counts the occurrences of each variable value conditioned on its parents and calculates probabilities.

2. get_probability(var, value, parent_values): Retrieves the conditional probability of a variable given its parent values. Returns 0.0 if the probability is not found.

3. joint_probability(assignment): Computes the joint probability of a complete assignment by multiplying the probabilities of each variable conditioned on its parents.

4. inference_by_enumeration(query, evidence): Performs probabilistic inference using enumeration. Calculates P(query | evidence) by summing over all possible assignments of hidden variables.

5. Helper Functions:
   - read_query(query): Parses the user input query and splits it into query and evidence variables, converting them into dictionary format.
   - read_variables(var_str): Converts variables provided in the format (e.g., Bt Gf) into a dictionary representation.
   - read_training_data(file_path): Reads training data from the specified file and maps it to a structured format for Bayesian Network learning.

6. main():
   - Defines the structure of the Bayesian Network.
   - Loads training data from the specified file.
   - Learns CPTs from the training data.
   - Allows the user to interactively query the Bayesian Network or exit by typing "none".

How to Run the Code:
Requirements: Python 3.9.7

Command Line Execution:
python bnet.py <training_data_file>
    <training_data_file>: Path to the file containing the training data.

Query Input Format:
1. Query a probability: <query variables>
   Example: Bt
2. Query conditional probability: <query variables> given <evidence variables>
   Example: Bt given Cf
3. Exit: Type none.
