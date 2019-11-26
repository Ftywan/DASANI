# UW CSE415 Project
## OPTION 4: Hidden Markov Model Applications.
### Names and Roles of Each Teammate:
Jinlin Xiang (data collection and HMM algorithm)
Yuhan Gao (Tkinter implementation)

### What the Program is Supposed to do:
The background of this program is here: Anthony’ girlfriend (Tina)came to Seattle from May to October last year. So, they began long-distance relationship but they will talk each other by the line. Anthony could know what Tina will do every day, but could not know the weather of Seattle. So we solve this problem by the Hidden Markov Model. This states is the weather of Seattle and the observation is what Tian did every day. By knowing this thing, we can know a-posteriori probability distribution over the set of possible states and determine the most likely state sequence when given take a sequence of observations.

#### Weather_data.py:
This script builds the weather data in a dictionary by python. The raw data are from the weather channel, starting from 2018.5 to 2018.10. and learn the start probability and the transition probability from this raw data.

#### HMM.py:
Based on the weather data, finish the Forward Algorithm and Viterbi Algorithm, and return the calculated probability and states based on different observation.

#### GUI.py:
Visualization the HMM.py’s result.

#### Test.py:
From the last time and it is a test for this final code.

### Brief Description of Technique:
For the project, we choose the option 4: Implementation and application of Hidden Markov Models. So, the main techniques we are featuring in our project is the Forward Algorithm and Viterbi Algorithm of HMM. The Forward Algorithm could solve the filter problem in three canonical HMM problems. The Forward Algorithm is used to calculate a ‘belief state’: the probability of a state at a certain time, given the history of evidence. And the Viterbi Algorithm usually be used to solve the decoding problem. The decoding problem asks about the joint probability of the entire sequence of hidden states that generated a particular sequence of observations.
For the implementation of these algorithm, we choose the weather model to implement the Forward Algorithm. In our weather model, we assume there are possible weather condition. And four possible operation: Walking, Shopping, Cleaning and Boating. Each weather condition has a certain probability to cause a certain operation. The operation is observable, but weather condition is hidden. And we also know the transition probability of weather condition and emission probability of weather and operation. Our goal is to calculate the probability of happening a certain sequence of operation by given all the information above. For implementation of Viterbi Algorithm, we still use the same model and information in Forward Algorithm, but our goal now changes to calculate the probability of certain weather condition sequence by given the certain operation sequence.
