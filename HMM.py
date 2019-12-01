# constant
SEQUENCE_PATH = 'data/training.txt'
CPG_POSITION_PATH = 'data/cpg_train.txt'
TEST_SEQUENCE_PATH = 'data/testing.txt'
STATES = ['A+', 'G+', 'C+', 'T+', 'A-', 'G-', 'C-', 'T-']
OBSERVATIONS = ['A', 'G', 'C', 'T']

# global variable
state_sequence = []  # list of all training data
test_sequence = []
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
                 'T-': {'A': 0.0, 'G': 0.0, 'C': 0.0, 'T': 1.0}}

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
def load_test_data():
    # read sequence data
    f = open(TEST_SEQUENCE_PATH, 'r')
    x = f.readlines()
    for line in x:
        for state in line:
            if state != '\n':
                test_sequence.append(state)

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
        # start_index = int(island[0]) - 1
        # end_index = int(island[1]) - 1
                
        start_index = int(island[0])
        end_index = int(island[1])
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
            temp[next_state] = transition_count[state][next_state] / state_transition[state]
            transition_prob[state] = temp

    print(disjoint_prob)
    print(sum(disjoint_prob.values()))
    print(transition_prob)
    print(sum(disjoint_count.values()))
    print(len(state_sequence))

def viterbi(observed_sequence):
    N = len(STATES)
    T = len(observed_sequence)
    v = [ [0 for i in range(T)] for j in range(N) ] # float num for value
    backpointer = [ [0 for i in range(T)] for j in range(N) ] # index of state in the STATES list

    # initialization
    for s in range(N):
        v[s][0] = disjoint_prob[STATES[s]] * emission_prob[STATES[s]][observed_sequence[0]]
        #backpointer[s][0] = 0
        backpointer[s][0] = None
    # done intialization

    for s in range(N):
        print(v[s][0])
    print('\n')

    # recursion step
    for t in range(1, T):
        for s in range(N):
            v_max = float("-inf")
            max_state = None
            # v_temp = []  # all states at only one time point

            for ps in range(N):
                temp = v[ps][t-1] * transition_prob[STATES[ps]][STATES[s]] * emission_prob[STATES[s]][observed_sequence[t]]
                if temp > v_max:
                    v_max = temp
                    max_state = ps
            v[s][t] = v_max
            backpointer[s][t] = max_state
    # done iteration
    # print(v)
    # print(backpointer)

    # termination step
    bestpath_prob = 0
    bestpath_pointer = None
    for i in range(N):
        if v[i][T-1] > bestpath_prob:
            bestpath_prob = v[i][T-1]
            bestpath_pointer = i
    # done termination

    # find best path
    bestpath_index = []
    bp_index = bestpath_pointer  # index of the last state of best path in STATES
    position = T - 1
    while bp_index:
        bestpath_index.append(bp_index)
        position -= 1
        bp_index = backpointer[bp_index][position]
    bestpath_index.reverse()

    best_path = []
    for index in bestpath_index:
        best_path.append(STATES[index])
    # found

    print(best_path)
    return best_path, bestpath_prob, v


if __name__ == "__main__":
    load_sequence_data()
    load_test_data()
    load_cpg_data()
    calculate_probability()
    bestpath, bp_prob, v = viterbi(test_sequence)
