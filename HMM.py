import math

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
# transition_prob = {'C+': {'C+': 0.37023851904592386, 'C-': 3.5599857600569602e-34, 'A+': 0.19366322534709862, 'A-': 3.5599857600569602e-34, 'T-': 3.5599857600569602e-34, 'T+': 0.1968672125311499, 'G-': 3.5599857600569602e-34, 'G+': 0.2392310430758277}, 'C-': {'C+': 0.0002288015375463323, 'C-': 0.3457648835400174, 'A+': 4.576030750926646e-35, 'A-': 0.2658216263213289, 'T-': 0.28645952500800803, 'T+': 4.576030750926646e-35, 'G-': 0.10172516359309934, 'G+': 4.576030750926646e-35}, 'A+': {'C+': 0.3181076672104405, 'C-': 8.156606851549756e-34, 'A+': 0.16557911908646003, 'A-': 8.156606851549756e-34, 'T-': 8.156606851549756e-34, 'T+': 0.11745513866231648, 'G-': 8.156606851549756e-34, 'G+': 0.3988580750407831}, 'A-': {'C+': 0.00042475728155339805, 'C-': 0.22554611650485437, 'A+': 6.067961165048544e-35, 'A-': 0.24939320388349515, 'T-': 0.18216019417475726, 'T+': 6.067961165048544e-35, 'G-': 0.3424757281553398, 'G+': 6.067961165048544e-35}, 'T-': {'C+': 0.00011155111829996096, 'C-': 0.28043951140610185, 'A+': 5.577555914998049e-35, 'A-': 0.1246025991410564, 'T-': 0.2654358859947571, 'T+': 5.577555914998049e-35, 'G-': 0.3294104523397847, 'G+': 5.577555914998049e-35}, 'T+': {'C+': 0.3731117824773414, 'C-': 7.552870090634441e-34, 'A+': 0.0649546827794562, 'A-': 7.552870090634441e-34, 'T-': 7.552870090634441e-34, 'T+': 0.17220543806646527, 'G-': 7.552870090634441e-34, 'G+': 0.38972809667673713}, 'G-': {'C+': 0.00028767320324111806, 'C-': 0.2658579853286666, 'A+': 4.7945533873519686e-35, 'A-': 0.20736443400297264, 'T-': 0.1873232008438414, 'T+': 4.7945533873519686e-35, 'G-': 0.33916670662127824, 'G+': 4.7945533873519686e-35}, 'G+': {'C+': 0.3431178103927013, 'C-': 0.0027766759222530744, 'A+': 0.15589051963506545, 'A-': 0.0007933359777865926, 'T-': 0.0007933359777865926, 'T+': 0.15827052756842522, 'G-': 0.0035700119000396666, 'G+': 0.3347877826259421}}
transition_prob = {}
emission_prob = {
    'C+': {'A': 1e-30, 'C': 1.0, 'T': 1e-30, 'G': 1e-30},
    'C-': {'A': 1e-30, 'C': 1.0, 'T': 1e-30, 'G': 1e-30},
    'A+': {'A': 1.0, 'C': 1e-30, 'T': 1e-30, 'G': 1e-30},
    'A-': {'A': 1.0, 'C': 1e-30, 'T': 1e-30, 'G': 1e-30},
    'T-': {'A': 1e-30, 'C': 1e-30, 'T': 1.0, 'G': 1e-30},
    'T+': {'A': 1e-30, 'C': 1e-30, 'T': 1.0, 'G': 1e-30},
    'G-': {'A': 1e-30, 'C': 1e-30, 'T': 1e-30, 'G': 1.0},
    'G+': {'A': 1e-30, 'C': 1e-30, 'T': 1e-30, 'G': 1.0}}


def load_sequence_data():
    # read sequence data
    f = open(SEQUENCE_PATH, 'r')
    x = f.readlines()
    for line in x:
        for state in line:
            if state != '\n':
                state_sequence.append(state)
    # print(state_sequence)
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
        line = line.strip('\n')
        position = line.split(' ')
        cpg_islands.append((position[0], position[1]))
    # done reading island positions


def add_label(index):
    for island in cpg_islands:
        if int(island[0]) <= index + 1 <= int(island[1]):
            return state_sequence[index] + '+'
    return state_sequence[index] + '-'


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
    for index in range(len(state_sequence) - 1):
        current_s = add_label(index)
        next_s = add_label(index + 1)

        disjoint_count[current_s] += 1
        transition_count[current_s][next_s] += 1
    disjoint_count[add_label(len(state_sequence) - 1)] += 1  # last member

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
            prob = transition_count[state][next_state] / \
                state_transition[state]
            if prob == 0:
                prob = 1e-30
            temp[next_state] = prob
            transition_prob[state] = temp

    print(disjoint_prob)
    print(sum(disjoint_prob.values()))
    print(transition_prob)
    for state in STATES:
        print(sum(transition_prob[state].values()))
    print(sum(disjoint_count.values()))
    print(len(state_sequence))


print('running viterbi')


def viterbi(observed_sequence):
    N = len(STATES)
    T = len(observed_sequence)
    v = [[0 for i in range(T)] for j in range(N)]  # float num for value
    # index of state in the STATES list
    backpointer = [[0 for i in range(T)] for j in range(N)]

    print(T, len(v[0]), len(backpointer[0]))

    # initialization
    for s in range(N):
        v[s][0] = math.log(disjoint_prob[STATES[s]]) + \
            math.log(emission_prob[STATES[s]][observed_sequence[0]])
        backpointer[s][0] = float('-inf')
    # done intialization

    # recursion step
    for t in range(1, T):
        for s in range(N):
            v_max = float("-inf")
            max_state = 0

            for ps in range(N):
                temp = v[ps][t-1] + math.log(transition_prob[STATES[ps]][STATES[s]]) + math.log(
                    emission_prob[STATES[s]][observed_sequence[t]])
                if temp > v_max:
                    v_max = temp
                    max_state = ps
            v[s][t] = v_max
            backpointer[s][t] = max_state
    # done iteration

    # print(backpointer)
    print(len(backpointer[0]))

    # termination step
    bestpath_prob = float('-inf')
    bestpath_pointer = 0
    for i in range(N):
        if v[i][T-1] > bestpath_prob:
            bestpath_prob = v[i][T-1]
            bestpath_pointer = i
    # done termination

    print(bestpath_pointer)
    print(bestpath_prob)

    # find best path
    bestpath_index = []
    bp_index = bestpath_pointer  # index of the last state of best path in STATES
    print(bp_index)

    position = T - 1
    # while position >= 0 and bp_index >= 0:
    while bp_index >= 0:
        bestpath_index.append(bp_index)
        #position -= 1
        # print(backpointer[bp_index][position])
        bp_index = backpointer[bp_index][position]
        # print(bp_index)
        position -= 1

    print(len(bestpath_index))

    bestpath_index.reverse()

    # print(bestpath_index)
    # print('\n')

    best_path = []
    for index in bestpath_index:
        best_path.append(STATES[index])
    # found

    # print(best_path)
    return best_path, bestpath_prob, v


def output(best_sequence):
    output_cpg = []
    start = 0
    while start < len(best_sequence) - 1:
        if (best_sequence[start].endswith('+')):
            end = start + 1
            while end <= len(best_sequence) - 1:
                if (best_sequence[end].endswith('-')):
                    break
            output_cpg.append([start, end - 1])
            start = end
        start += 1
    return output_cpg

def get_island_position(bestpath):
    on = []
    off = []

    if '+' in bestpath[0]:
        on.append(1)
    for i in range(len(bestpath) - 1):
        if '-' in bestpath[i] and '+' in bestpath[i + 1]:
            on.append(i + 2)
        if '+' in bestpath[i] and '-' in bestpath[i + 1]:
            off.append(i + 1)
    if '+' in bestpath[len(bestpath) - 1]:
        off.append(len(bestpath))
    
    assert len(on) == len(off)
    print('\n\n\n[RESULT] There are', len(on), 'CpG islands in total')
    for i in range(len(on)):
        print(on[i], off[i])

            


if __name__ == "__main__":
    load_sequence_data()
    load_test_data()
    load_cpg_data()
    calculate_probability()
    test = 'CGCGCGCGGGGGAAAGGGGCCCCGGCGCGGCATATCGCGCGGCGGCGCGCGCCCGCATATATATAATATTATATATATATATTTTATATTAGACGCGCGCGCGCCGCCCCGCGCGGCGGGGCGCGCGCCGCGCGCGCGCGCGCGCGCGCCCCGCGCG'
    print(len(test))
    bestpath, bestpath_prob, v = viterbi(state_sequence)
    # cpg = output(bestpath)
    # print(cpg)
    # print(bestpath)
    get_island_position(bestpath)
