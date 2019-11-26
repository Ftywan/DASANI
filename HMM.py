SEQUENCE_PATH = 'data/training.txt'

# read in data
state_sequence = []  # list of all training data
f = open(SEQUENCE_PATH, 'r')
x = f.readlines()
for line in x:
    for state in line:
        if state != '\n':
            state_sequence.append(state)
print('length of sequence')
print(len(state_sequence))
# done reading data

# calculate probability
# count
disjoint_count = {'A': 0, 'G': 0, 'C': 0, 'T': 0}
transition_count = {'A': {'A': 0, 'G': 0, 'C': 0, 'T': 0},
                    'G': {'A': 0, 'G': 0, 'C': 0, 'T': 0},
                    'C': {'A': 0, 'G': 0, 'C': 0, 'T': 0},
                    'T': {'A': 0, 'G': 0, 'C': 0, 'T': 0}
                    }
for i in range(len(state_sequence)):
    disjoint_count[state_sequence[i]] += 1
    if i != len(state_sequence) - 1:
        transition_count[state_sequence[i]][state_sequence[i + 1]] += 1
    # end count
print('disjoint_count')
print(disjoint_count)
print('transition_count')
print(transition_count)
# calculate prob
disjoint_prob = {}
for key in disjoint_count:
    disjoint_prob[key] = disjoint_count[key] / len(state_sequence)

transition_prob = {}
for condition_key, condition_counts in transition_count.items():
    temp = {}
    for key in condition_counts:
        temp[key] = condition_counts[key] / sum(condition_counts.values())
    transition_prob[condition_key] = temp

print('disjoint probability')
print(disjoint_prob)
print('transition_probability')
print(transition_prob)
