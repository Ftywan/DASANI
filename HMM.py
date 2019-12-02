import math
import datetime
 
# constants
TRAINING_SEQUENCE_PATH = 'data/training.txt'
TRAINING_CPG_PATH = 'data/cpg_train.txt'
#TESTING_SEQUENCE_PATH = None
STATES = ['A+', 'G+', 'C+', 'T+', 'A-', 'G-', 'C-', 'T-']

# global variables
currentDT = datetime.datetime.now()
time = currentDT.strftime("%Y-%m-%d %H:%M:%S")
out_file = open('CpG-Island Results: '+ time, 'w')
state_sequence = []  # list of all training data
test_sequence = []  # list of testing data
cpg_islands = []  # list of tuples indicating positions of CpG islands in the training data
disjoint_prob = {}
transition_prob = {}
emission_prob = {
    'C+': {'A': 1e-30, 'C': 1.0, 'T': 1e-30, 'G': 1e-30},
    'C-': {'A': 1e-30, 'C': 1.0, 'T': 1e-30, 'G': 1e-30},
    'A+': {'A': 1.0, 'C': 1e-30, 'T': 1e-30, 'G': 1e-30},
    'A-': {'A': 1.0, 'C': 1e-30, 'T': 1e-30, 'G': 1e-30},
    'T-': {'A': 1e-30, 'C': 1e-30, 'T': 1.0, 'G': 1e-30},
    'T+': {'A': 1e-30, 'C': 1e-30, 'T': 1.0, 'G': 1e-30},
    'G-': {'A': 1e-30, 'C': 1e-30, 'T': 1e-30, 'G': 1.0},
    'G+': {'A': 1e-30, 'C': 1e-30, 'T': 1e-30, 'G': 1.0}
}

# def load_sequence_data():
#     # read sequence data
#     f = open(SEQUENCE_PATH, 'r')
#     x = f.readlines()
#     for line in x:
#         for state in line:
#             if state != '\n':
#                 state_sequence.append(state)
#     # print(state_sequence)
#     # done reading sequence data


# def load_test_data():
#     # read sequence data
#     f = open(TEST_SEQUENCE_PATH, 'r')
#     x = f.readlines()
#     for line in x:
#         for state in line:
#             if state != '\n':
#                 test_sequence.append(state)


def load_sequence_data(file_path, destination):
    f = open(file_path, 'r')
    x = f.readlines()
    for line in x:
        for state in line:
            if state != '\n':
                destination.append(state)
    f.close()


def load_cpg_data():
    # read cpg island positions
    f = open(TRAINING_CPG_PATH, 'r')
    x = f.readlines()
    for line in x:
        line = line.strip('\n')
        position = line.split(' ')
        cpg_islands.append((position[0], position[1]))
    # done reading island positions
    f.close()


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

    print('Disjoint counts:', disjoint_count)
    print('\n\n\nTransition counts:', transition_count)

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

    print('\n\n\nDisjoint Probability:', disjoint_prob)
    print('\n\n\nTransition Probability:', transition_prob)


def viterbi(observed_sequence):
    print('\nRunning Viterbi Algorithm...\n')
    N = len(STATES)
    T = len(observed_sequence)
    v = [[0 for i in range(T)] for j in range(N)]  # float num for value
    # index of state in the STATES list
    backpointer = [[0 for i in range(T)] for j in range(N)]

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

    # termination step
    bestpath_prob = float('-inf')
    bestpath_pointer = 0
    for i in range(N):
        if v[i][T-1] > bestpath_prob:
            bestpath_prob = v[i][T-1]
            bestpath_pointer = i
    # done termination

    # find best path
    bestpath_index = []
    bp_index = bestpath_pointer  # index of the last state of best path in STATES

    position = T - 1
    while bp_index >= 0:
        bestpath_index.append(bp_index)
        bp_index = backpointer[bp_index][position]
        position -= 1
    
    bestpath_index.reverse()

    best_path = []
    for index in bestpath_index:
        best_path.append(STATES[index])
    # found

    return best_path, bestpath_prob, v

# def output(best_sequence):
#     output_cpg = []
#     start = 0
#     while start < len(best_sequence) - 1:
#         if (best_sequence[start].endswith('+')):
#             end = start + 1
#             while end <= len(best_sequence) - 1:
#                 if (best_sequence[end].endswith('-')):
#                     break
#             output_cpg.append([start, end - 1])
#             start = end
#         start += 1
#     return output_cpg


def output(bestpath):
    out_file.write('Cpg-Islands prediction results:\n\n')
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
    print('\n\n\n[RESULT] There are', len(on), 'CpG-islands in total')
    for i in range(len(on)):
        print(on[i], off[i])
        out_file.write(' '.join((str(on[i]), '-', str(off[i]))) + '\n')
        for x in range(on[i]-1, off[i]):
            out_file.write(state_sequence[x])
        out_file.write('\n\n')
    out_file.write('source file: ' + TESTING_SEQUENCE_PATH)

# if __name__ == "__main__":
#     load_sequence_data(TRAINING_SEQUENCE_PATH, state_sequence)
#     load_sequence_data(TESTING_SEQUENCE_PATH, test_sequence)
#     load_cpg_data()
#     calculate_probability()
#     # test = 'CGCGCGCGGGGGAAAGGGGCCCCGGCGCGGCATATCGCGCGGCGGCGCGCGCCCGCATATATATAATATTATATATATATATTTTATATTAGACGCGCGCGCGCCGCCCCGCGCGGCGGGGCGCGCGCCGCGCGCGCGCGCGCGCGCGCCCCGCGCG'
#     # print(len(test))
#     bestpath, bestpath_prob, v = viterbi(test_sequence)
#     output(bestpath)

if __name__ == "__main__":
    print('Welcome to our CpG islands Detector!')
    print('Please choose one of the following two datasets: data/testing.txt ; data/testing-chr1.txt')
    user_input = input('Your input dataset: ')

    while user_input != 'data/testing.txt' and user_input != 'data/testing-chr1.txt':
        print('Please choose one of the following two datasets: data/testing.txt ; data/testing-chr1.txt')
        user_input = input('Your input dataset: ')

    if user_input == 'data/testing.txt':
        TESTING_SEQUENCE_PATH = 'data/testing.txt'
        load_sequence_data(TRAINING_SEQUENCE_PATH, state_sequence)
        load_sequence_data(TESTING_SEQUENCE_PATH, test_sequence)
        load_cpg_data()
        calculate_probability()
        bestpath, bestpath_prob, v = viterbi(test_sequence)
        output(bestpath)
    else:
        TESTING_SEQUENCE_PATH = 'data/testing-chr1.txt'
        load_sequence_data(TRAINING_SEQUENCE_PATH, state_sequence)
        load_sequence_data(TESTING_SEQUENCE_PATH, test_sequence)
        load_cpg_data()
        calculate_probability()
        bestpath, bestpath_prob, v = viterbi(test_sequence)
        output(bestpath)

