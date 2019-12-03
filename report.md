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

code excerpt showing some interesting part(s) of your Python code and some explanation of it;
brief description of what each team member learned in this project;
what you would like to add to your program if you had more time;
citations for any references you used in the project. This should include the names and URLs of any websites that you used and whose ideas or other resources were incorporated into your project. In each case, describe in a sentence what role that website played in your project and what you incorporated from it.
For 5 points of extra credit, include a section with a heading "Partners' Reflections" with two subsections, one for each partner. Each subsection should give the partner's name, main role(s) in the project, a description of the challenges and benefits of the partnership from that partner's perspective.
