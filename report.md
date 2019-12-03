## Report for CpG Island Detector Using HMM and Viterbi Algorithm

#### Team Member and Job Description
Jinghan Lu: implemented the Viterbi Algorithm
Tianyuan Fu: implemented algorithms for probability, finished up the implementation of Viterbi Algorithm

#### Functionality of CpG Island Detector
This program is supposed to identify the potential CpG Islands in a given input DNA sequence. CpG island is defined as a subsequence of a long DNA sequence, which is rich in C and G. According to biological probabilistic researches, DNA regions with high reichness in C and G are more likely to carry gene information. Therefore, this approach to detect CpG Islands can be useful in real-time biological researches.

The input format should be a file describing the composition of a DNA sequence, comprised with A, G, C, T, 4 kinds of nucleotide acids.
The output will be starting and ending position pairs displayed to the console, along with a file containing the whole CpG Island subsequence and more details.

#### Technical Details
//TODO 
technique used and brief description (half a page) of how that technique works. If you use multiple AI techniques then describe each one but with somewhat less detail for each one;
either a screen shot or a transcript of an interesting sample session;


#### Demo Instructions
1. Unzip the zip file and put the decompressed folder in a directory that you are familiar with
1. Open up a shell window (Linux) / terminal window (macOS) and change the directory into the upzipped folder
1. Check the content of the folder: 
    1. There is a folder called `result/`. This will be where the output files locate
    1. There is a `data/` folder. Inside `data/`, there should be 3 text files and a `test/` folder containing two text files. These are the training and testing data for this program.
1. Back to the console. Try with the command:
`python3 HMM.py`
1. Seeing the prompted message, choose a testing file from the message and type in the console. Hit `enter` to continue.
1. Intermediate results, such as disjoint probability, transition probability would be prinred in the console. 
1. The final results would be in two parts: a message in the console showing the starting and ending position pairs of the CpG Islands; a file in the result folder have whole sequences of islands and some other details.
> You can also add your own DNA sequence files to the `test\` folder and choose it to be executed as the program begins.

#### code excerpt showing some interesting part(s) of your Python code and some explanation of it;
brief description of what each team member learned in this project;

#### Possible Add-ons
- Input side: support to more biological data format like FASTA.
- Processing side: the current method for calculating the probability can be improved to have less complexity
- Output side: a graphical user interface (GUI) can be implemented to display the results.

#### *References*
1. GitHub Repository: https://github.com/devanshdalal/cpg-island-prediction-HMM
A smaple implementation of CpG Island Detector with HMM and Viterbi Algorithm. We have our training data set from this project, but different concepts of implementing the program.
2. HMM slides from CMU: https://www.cs.cmu.edu/~02710/Lectures/HMMs.pdf
Provided some hint and insights to HMM.
3. TODO

For 5 points of extra credit, include a section with a heading "Partners' Reflections" with two subsections, one for each partner. Each subsection should give the partner's name, main role(s) in the project, a description of the challenges and benefits of the partnership from that partner's perspective.

#### Partners' Reflections
Tianyuan Fu: Implemented the probability algorithms, output method and debugging Viterbi.
HMM is a model that is not formally taught in class, and that is the point of chanllenges and attractiveness. Understanding the model is not the easy thing, involing many concepts from statistics. But during the process of accepting the concepts, I am happy to see that I can apply concepts previously learnt in lectures, most of which are high-level views, and that eased the carryout of the whole project. It would be so helpful to have such an experience since new models of AI and ML are emerging. Having the experience of this project makes me confident to confront projects with more difficulty in the future.

Jinghan Lu: