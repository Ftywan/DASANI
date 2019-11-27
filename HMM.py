# constant
SEQUENCE_PATH = 'data/training.txt'
CPG_POSITION_PATH = 'data/cpg_train.txt'
STATES = ['A+', 'G+', 'C+', 'T+', 'A-', 'G-', 'C-', 'T-']
OBSERVATIONS = ['A', 'G', 'C', 'T']

# global variable
state_sequence = []  # list of all training data
cpg_islands = []

def load_sequence_data():
    # read sequence data
    f = open(SEQUENCE_PATH, 'r')
    x = f.readlines()
    for line in x:
        for state in line:
            if state != '\n':
                state_sequence.append(state)
    # done reading sequence data

def load_cpg_data():
    # read cpg island positions
    f = open(CPG_POSITION_PATH, 'r')
    x = f.readlines()
    for line in x:
        position = line.split(' ')
        cpg_islands.append((position[0], position[1]))
    # done reading island positions

def calculate_probability():
    disjoint_count = {}
    transition_count = {}
    # initialize local variable
    for state in STATES:
        disjoint_count[state] = 0
    for state in STATES:
        temp = {}
        for state_2 in STATES:
            temp[state_2] = 0
            transition_count[state] = temp
    # done initializing

    # get counts
    index = 0
    for island in cpg_islands:
        start_index = int(island[0]) - 1
        end_index = int(island[1]) - 1
        while index < start_index:
            # disjoint count
            state = state_sequence[index] + '-'
            disjoint_count[state] += 1
            # transition count
            if index + 1 != start_index:
                next_state = state_sequence[index + 1] + '-'
            else:
                next_state = state_sequence[index + 1] + '+'
            transition_count[state][next_state] += 1
            # update index
            index += 1
        while index <= end_index:
            # disjoint count
            state = state_sequence[index] + '+'
            disjoint_count[state] += 1
            # transition count
            if index != end_index:
                next_state = state_sequence[index + 1] + '+'
            else:
                next_state = state_sequence[index + 1] + '-'
            transition_count[state][next_state] += 1
            # update index
            index += 1
    print(disjoint_count)
    print(transition_count)


if __name__ == "__main__":
    load_sequence_data()
    load_cpg_data()
    calculate_probability()
