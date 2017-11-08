from CircuitBoardCSP import CircuitBoardCSP
from Constraint import Constraint

# test_CircuitBoardCSP.py
# Eisner Oct 2017
#
# Test CircuitBoardCSP.py with circuit board example from
# http://www.cs.dartmouth.edu/~devin/cs76/04_constraint/constraint.html


variable_strings = ['a', 'b', 'c', 'e']
variable_dimensions = [(3, 2), (5, 2), (2, 3), (7, 1)]  # (width, height)
board_dimensions = (10, 3)  # width, height

# Add all possible values to a set (for domain)
values = set()
for x in range(board_dimensions[0]):
    for y in range(board_dimensions[1]):
        values.add((x, y))

# For each variable, add a set of domain values to domain_list
domain_list = []
for variable in range(len(variable_strings)):
    domain_list.append(values)

# Set up constraints
constraint_01 = [
    ((0, 0), (3, 0)),
    ((0, 0), (4, 0)),
    ((0, 0), (5, 0)),
    ((0, 1), (3, 0)),
    ((0, 1), (4, 0)),
    ((0, 1), (5, 0)),
    ((0, 0), (3, 1)),
    ((0, 0), (4, 1)),
    ((0, 0), (5, 1)),
    ((0, 1), (3, 1)),
    ((0, 1), (4, 1)),
    ((0, 1), (5, 1)),  # V
    ((7, 0), (2, 0)),
    ((7, 0), (1, 0)),
    ((7, 0), (0, 0)),
    ((7, 1), (2, 0)),
    ((7, 1), (1, 0)),
    ((7, 1), (0, 0)),
    ((7, 0), (2, 1)),
    ((7, 0), (1, 1)),
    ((7, 0), (0, 1)),
    ((7, 1), (2, 1)),
    ((7, 1), (1, 1)),
    ((7, 1), (0, 1)),
]

constraint_02 = [
    ((0, 0), (3, 0)),
    ((0, 0), (4, 0)),
    ((0, 0), (5, 0)),
    ((0, 0), (6, 0)),
    ((0, 0), (7, 0)),
    ((0, 0), (8, 0)),
    ((0, 1), (3, 0)),
    ((0, 1), (4, 0)),
    ((0, 1), (5, 0)),
    ((0, 1), (6, 0)),
    ((0, 1), (7, 0)),
    ((0, 1), (8, 0)),
    ((1, 0), (4, 0)),
    ((1, 0), (5, 0)),
    ((1, 0), (6, 0)),
    ((1, 0), (7, 0)),
    ((1, 0), (8, 0)),
    ((1, 1), (4, 0)),
    ((1, 1), (5, 0)),
    ((1, 1), (6, 0)),
    ((1, 1), (7, 0)),
    ((1, 1), (8, 0)),  # V
    ((2, 0), (5, 0)),
    ((2, 0), (6, 0)),
    ((2, 0), (7, 0)),
    ((2, 0), (8, 0)),
    ((2, 1), (5, 0)),
    ((2, 1), (6, 0)),
    ((2, 1), (7, 0)),
    ((2, 1), (8, 0)),  # V
    ((3, 0), (6, 0)),
    ((3, 0), (7, 0)),
    ((3, 0), (8, 0)),
    ((3, 1), (6, 0)),
    ((3, 1), (7, 0)),
    ((3, 1), (8, 0)),  # V
    ((4, 0), (7, 0)),
    ((4, 0), (8, 0)),
    ((4, 1), (7, 0)),
    ((4, 1), (8, 0)),  # V
    ((5, 0), (8, 0)),
    ((5, 1), (8, 0)),  # V
    ((7, 0), (5, 0)),
    ((7, 1), (5, 0)),
    ((7, 0), (4, 0)),
    ((7, 1), (4, 0)),
    ((7, 0), (3, 0)),
    ((7, 1), (3, 0)),
    ((7, 0), (2, 0)),
    ((7, 1), (2, 0)),
    ((7, 0), (1, 0)),
    ((7, 1), (1, 0)),
    ((7, 0), (0, 0)),
    ((7, 1), (0, 0)),  # V
    ((6, 0), (4, 0)),
    ((6, 1), (4, 0)),
    ((6, 0), (3, 0)),
    ((6, 1), (3, 0)),
    ((6, 0), (2, 0)),
    ((6, 1), (2, 0)),
    ((6, 0), (1, 0)),
    ((6, 1), (1, 0)),
    ((6, 0), (0, 0)),
    ((6, 1), (0, 0)),  # V
    ((5, 0), (3, 0)),
    ((5, 1), (3, 0)),
    ((5, 0), (2, 0)),
    ((5, 1), (2, 0)),
    ((5, 0), (1, 0)),
    ((5, 1), (1, 0)),
    ((5, 0), (0, 0)),
    ((5, 1), (0, 0)),  # V
    ((4, 0), (2, 0)),
    ((4, 1), (2, 0)),
    ((4, 0), (1, 0)),
    ((4, 1), (1, 0)),
    ((4, 0), (0, 0)),
    ((4, 1), (0, 0)),  # V
    ((3, 0), (1, 0)),
    ((3, 1), (1, 0)),
    ((3, 0), (0, 0)),
    ((3, 1), (0, 0)),  # V
    ((2, 0), (0, 0)),
    ((2, 1), (0, 0)),
]

constraint_03 = [
    ((0, 0), (0, 2)),
    ((0, 0), (1, 2)),
    ((0, 0), (2, 2)),
    ((0, 0), (3, 2)),  # V
    ((1, 0), (0, 2)),
    ((1, 0), (1, 2)),
    ((1, 0), (2, 2)),
    ((1, 0), (3, 2)),  # V
    ((2, 0), (0, 2)),
    ((2, 0), (1, 2)),
    ((2, 0), (2, 2)),
    ((2, 0), (3, 2)),  # V
    ((3, 0), (0, 2)),
    ((3, 0), (1, 2)),
    ((3, 0), (2, 2)),
    ((3, 0), (3, 2)),  # V
    ((4, 0), (0, 2)),
    ((4, 0), (1, 2)),
    ((4, 0), (2, 2)),
    ((4, 0), (3, 2)),  # V
    ((5, 0), (0, 2)),
    ((5, 0), (1, 2)),
    ((5, 0), (2, 2)),
    ((5, 0), (3, 2)),  # V
    ((6, 0), (0, 2)),
    ((6, 0), (1, 2)),
    ((6, 0), (2, 2)),
    ((6, 0), (3, 2)),  # V
    ((7, 0), (0, 2)),
    ((7, 0), (1, 2)),
    ((7, 0), (2, 2)),
    ((7, 0), (3, 2)),  # V
    ((0, 1), (0, 0)),
    ((0, 1), (1, 0)),
    ((0, 1), (2, 0)),
    ((0, 1), (3, 0)),  # V
    ((1, 1), (0, 0)),
    ((1, 1), (1, 0)),
    ((1, 1), (2, 0)),
    ((1, 1), (3, 0)),  # V
    ((2, 1), (0, 0)),
    ((2, 1), (1, 0)),
    ((2, 1), (2, 0)),
    ((2, 1), (3, 0)),  # V
    ((3, 1), (0, 0)),
    ((3, 1), (1, 0)),
    ((3, 1), (2, 0)),
    ((3, 1), (3, 0)),  # V
    ((4, 1), (0, 0)),
    ((4, 1), (1, 0)),
    ((4, 1), (2, 0)),
    ((4, 1), (3, 0)),  # V
    ((5, 1), (0, 0)),
    ((5, 1), (1, 0)),
    ((5, 1), (2, 0)),
    ((5, 1), (3, 0)),  # V
    ((6, 1), (0, 0)),
    ((6, 1), (1, 0)),
    ((6, 1), (2, 0)),
    ((6, 1), (3, 0)),  # V
    ((7, 1), (0, 0)),
    ((7, 1), (1, 0)),
    ((7, 1), (2, 0)),
    ((7, 1), (3, 0)),  # V
    ((0, 0), (3, 0)),
    ((0, 0), (3, 1)),
    ((0, 0), (3, 2)),  # V
    ((0, 1), (3, 0)),
    ((0, 1), (3, 1)),
    ((0, 1), (3, 2)),  # V
    ((7, 0), (0, 0)),
    ((7, 0), (0, 1)),
    ((7, 0), (0, 2)),  # V
    ((7, 1), (0, 0)),
    ((7, 1), (0, 1)),
    ((7, 1), (0, 2)),
]

constraint_12 = [
    ((0, 0), (5, 0)),
    ((0, 0), (6, 0)),
    ((0, 0), (7, 0)),
    ((0, 0), (8, 0)),  # V
    ((0, 1), (5, 0)),
    ((0, 1), (6, 0)),
    ((0, 1), (7, 0)),
    ((0, 1), (8, 0)),  # V
    ((1, 0), (6, 0)),
    ((1, 0), (7, 0)),
    ((1, 0), (8, 0)),  # V
    ((1, 1), (6, 0)),
    ((1, 1), (7, 0)),
    ((1, 1), (8, 0)),  # V
    ((2, 0), (7, 0)),
    ((2, 0), (8, 0)),  # V
    ((2, 1), (7, 0)),
    ((2, 1), (8, 0)),  # V
    ((3, 0), (8, 0)),  # V
    ((3, 1), (8, 0)),  # V
    ((5, 0), (3, 0)),
    ((5, 1), (3, 0)),
    ((5, 0), (2, 0)),
    ((5, 1), (2, 0)),
    ((5, 0), (1, 0)),
    ((5, 1), (1, 0)),
    ((5, 0), (0, 0)),
    ((5, 1), (0, 0)),  # V
    ((4, 0), (2, 0)),
    ((4, 1), (2, 0)),
    ((4, 0), (1, 0)),
    ((4, 1), (1, 0)),
    ((4, 0), (0, 0)),
    ((4, 1), (0, 0)),  # V
    ((3, 0), (1, 0)),
    ((3, 1), (1, 0)),
    ((3, 0), (0, 0)),
    ((3, 1), (0, 0)),  # V
    ((2, 0), (0, 0)),
    ((2, 1), (0, 0)),
]

constraint_13 = [
    ((0, 0), (0, 2)),
    ((0, 0), (1, 2)),
    ((0, 0), (2, 2)),
    ((0, 0), (3, 2)),  # V
    ((1, 0), (0, 2)),
    ((1, 0), (1, 2)),
    ((1, 0), (2, 2)),
    ((1, 0), (3, 2)),  # V
    ((2, 0), (0, 2)),
    ((2, 0), (1, 2)),
    ((2, 0), (2, 2)),
    ((2, 0), (3, 2)),  # V
    ((3, 0), (0, 2)),
    ((3, 0), (1, 2)),
    ((3, 0), (2, 2)),
    ((3, 0), (3, 2)),  # V
    ((4, 0), (0, 2)),
    ((4, 0), (1, 2)),
    ((4, 0), (2, 2)),
    ((4, 0), (3, 2)),  # V
    ((5, 0), (0, 2)),
    ((5, 0), (1, 2)),
    ((5, 0), (2, 2)),
    ((5, 0), (3, 0)),  # V N
    ((0, 1), (0, 0)),
    ((0, 1), (1, 0)),
    ((0, 1), (2, 0)),
    ((0, 1), (3, 0)),  # V
    ((1, 1), (0, 0)),
    ((1, 1), (1, 0)),
    ((1, 1), (2, 0)),
    ((1, 1), (3, 0)),  # V
    ((2, 1), (0, 0)),
    ((2, 1), (1, 0)),
    ((2, 1), (2, 0)),
    ((2, 1), (3, 0)),  # V
    ((3, 1), (0, 0)),
    ((3, 1), (1, 0)),
    ((3, 1), (2, 0)),
    ((3, 1), (3, 0)),  # V
    ((4, 1), (0, 0)),
    ((4, 1), (1, 0)),
    ((4, 1), (2, 0)),
    ((4, 1), (3, 0)),  # V
    ((5, 1), (0, 0)),
    ((5, 1), (1, 0)),
    ((5, 1), (2, 0)),
    ((5, 1), (3, 0)),  # V
]

constraint_23 = [
    ((0, 0), (2, 0)),
    ((0, 0), (2, 1)),
    ((0, 0), (2, 2)),
    ((0, 0), (3, 0)),
    ((0, 0), (3, 1)),
    ((0, 0), (3, 2)),  # V
    ((1, 0), (3, 0)),
    ((1, 0), (3, 1)),
    ((1, 0), (3, 2)),  # V
    ((8, 0), (0, 0)),
    ((8, 0), (0, 1)),
    ((8, 0), (0, 2)),
    ((8, 0), (1, 0)),
    ((8, 0), (1, 1)),
    ((8, 0), (1, 2)),  # V
    ((7, 0), (0, 0)),
    ((7, 0), (0, 1)),
    ((7, 0), (0, 2)),
]

# More constraints
constraint_10 = [(i, j) for (j, i) in constraint_01]
constraint_20 = [(i, j) for (j, i) in constraint_02]
constraint_30 = [(i, j) for (j, i) in constraint_03]
constraint_21 = [(i, j) for (j, i) in constraint_12]
constraint_31 = [(i, j) for (j, i) in constraint_13]
constraint_32 = [(i, j) for (j, i) in constraint_23]

# Build Constraint object
circuit_constraints = Constraint()

# Add constraints to Constraint object
circuit_constraints.add_constraint((0, 1), constraint_01)
circuit_constraints.add_constraint((0, 2), constraint_02)
circuit_constraints.add_constraint((0, 3), constraint_03)
circuit_constraints.add_constraint((1, 0), constraint_10)
circuit_constraints.add_constraint((1, 2), constraint_12)
circuit_constraints.add_constraint((1, 3), constraint_13)
circuit_constraints.add_constraint((2, 0), constraint_20)
circuit_constraints.add_constraint((2, 1), constraint_21)
circuit_constraints.add_constraint((2, 3), constraint_23)
circuit_constraints.add_constraint((3, 0), constraint_30)
circuit_constraints.add_constraint((3, 1), constraint_31)
circuit_constraints.add_constraint((3, 2), constraint_32)

# Finally, create a CircuitBoardCSP object
circuit = CircuitBoardCSP(variable_strings, domain_list, circuit_constraints,
                          values, variable_dimensions, board_dimensions,
                          mrv=True, lcv=True, ac3=True)

print(circuit.solve())