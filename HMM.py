# constant
SEQUENCE_PATH = 'data/training.txt'
CPG_POSITION_PATH = 'data/cpg_train.txt'
STATES = ['A+', 'G+', 'C+', 'T+', 'A-', 'G-', 'C-', 'T-']
OBSERVATIONS = ['A', 'G', 'C', 'T']

# global variable
state_sequence = []  # list of all training data
cpg_islands = []
disjoint_prob = {}
transition_prob = {}
emission_prob = {'A+': {'A': 1.0, 'G': 0.0, 'C': 0.0, 'T': 0.0},
                 'A-': {'A': 1.0, 'G': 0.0, 'C': 0.0, 'T': 0.0},
                 'G+': {'A': 0.0, 'G': 1.0, 'C': 0.0, 'T': 0.0},
                 'G-': {'A': 0.0, 'G': 1.0, 'C': 0.0, 'T': 0.0},
                 'C+': {'A': 0.0, 'G': 0.0, 'C': 1.0, 'T': 0.0},
                 'C-': {'A': 0.0, 'G': 0.0, 'C': 1.0, 'T': 0.0},
                 'T+': {'A': 0.0, 'G': 0.0, 'C': 0.0, 'T': 1.0},
                 'T+': {'A': 0.0, 'G': 0.0, 'C': 0.0, 'T': 1.0}}


def load_sequence_data():
    # read sequence data
    f = open(SEQUENCE_PATH, 'r')
    x = f.readlines()
    for line in x:
        for state in line:
            if state != '\n':
                state_sequence.append(state)
    #print(state_sequence)
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
    while index < len(state_sequence):
        state = state_sequence[index] + '-'
        disjoint_count[state] += 1
        if index != len(state_sequence) - 1:
            next_state = state_sequence[index + 1] + '-'
            transition_count[state][next_state] += 1
        index += 1

    print(disjoint_count)
    print(transition_count)

    # calculate disjoint probability
    for state in disjoint_count:
        disjoint_prob[state] = disjoint_count[state] / len(state_sequence)
    # calculate transition probability
    state_transition = {}  # total transition count for each state
    for state in transition_count:
        state_transition[state] = 0
        for next_state in transition_count[state]:
            state_transition[state] += transition_count[state][next_state]

    for state in transition_count:
        temp = {}
        for next_state in transition_count[state]:
            temp[next_state] = transition_count[state][next_state] / \
                state_transition[state]
            transition_prob[state] = temp

    print(disjoint_prob)
    print(sum(disjoint_prob.values()))
    print(transition_prob)
    print(sum(disjoint_count.values()))
    print(len(state_sequence))

def viterbi(observed):


if __name__ == "__main__":
    load_sequence_data()
    load_cpg_data()
    calculate_probability()
