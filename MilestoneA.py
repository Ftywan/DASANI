#!/usr/bin/python3
'''MilestoneA.py
This runnable file will provide a representation of
answers to key questions about your project in CSE 415.

'''

# DO NOT EDIT THE BOILERPLATE PART OF THIS FILE HERE:

CATEGORIES=['Baroque Chess Agent','Wicked Problem Formulation and A* Search',\
  'Backgammon Agent that Learns','Hidden Markov Models: Algorithms and Applications']

class Partner():
  def __init__(self, lastname, firstname, uwnetid):
    self.uwnetid=uwnetid
    self.lastname=lastname
    self.firstname=firstname

  def __lt__(self, other):
    return (self.lastname+","+self.firstname).__lt__(other.lastname+","+other.firstname)

  def __str__(self):
    return self.lastname+", "+self.firstname+" ("+self.uwnetid+")"

class Who_and_what():
  def __init__(self, team, option, title, approach, workload_distribution, references):
    self.team=team
    self.option=option
    self.title=title
    self.approach = approach
    self.workload_distribution = workload_distribution
    self.references = references

  def report(self):
    rpt = 80*"#"+"\n"
    rpt += '''The Who and What for This Submission

Project in CSE 415, University of Washington, Autumn, 2019
Milestone A

Team: 
'''
    team_sorted = sorted(self.team)
    # Note that the partner whose name comes first alphabetically
    # must do the turn-in.
    # The other partner(s) should NOT turn anything in.
    rpt += "    "+ str(team_sorted[0])+" (the partner who must turn in all files in Catalyst)\n"
    for p in team_sorted[1:]:
      rpt += "    "+str(p) + " (partner who should NOT turn anything in)\n\n"

    rpt += "Option: "+str(self.option)+"\n\n"
    rpt += "Title: "+self.title + "\n\n"
    rpt += "Approach: "+self.approach + "\n\n"
    rpt += "Workload Distribution: "+self.workload_distribution+"\n\n"
    rpt += "References: \n"
    for i in range(len(self.references)):
      rpt += "  Ref. "+str(i+1)+": "+self.references[i] + "\n"

    rpt += "\n\nThe information here indicates that the following file will need\n"+\
     "to be submitted (in addition to code and possible data files):\n"
    rpt += "    "+\
     {'1':"Baroque_Chess_Agent_Report",'2':"Wicked_Problem_Forulation_Report",\
      '3':"Backgammon_Agent_That_Learns_Report", '4':"Hidden_Markov_Models_Report"}\
        [self.option]+".pdf\n"

    rpt += "\n"+80*"#"+"\n"
    return rpt

# END OF BOILERPLATE.

# Change the following to represent your own information:

maggie = Partner("Tianyuan", "Fu", "tyfu")
john = Partner("Jinghan", "Lu", "jinghanl")
team = [maggie, john]

OPTION = '4'
# Legal options are 1, 2, 4, and 4.
# TODO
title = "CpG Island Detector for DNA"

approach = '''Our approach will be to first do reseach on 
CpG defination and related bioinformatic techneques;
second determine the observation and state objects;
third, find and download dataset for this project;
fourth, design and implement both forward and Viterbi algorithms,
and finally test based on CLI ouputs and finally visualize the output.'''

workload_distribution = '''We did reseach and determined our application domain for HMM together.
Tianyuan Fu: Implement the forward algorithm and GUI with Tkinter.
Jinghan Lu: Implement the Viterbi algorithm and apply testing'''

reference1 = '''Wikipedia article on CpG Site;
    URL: https://en.wikipedia.org/wiki/CpG_site (accessed Nov. 19, 2019)'''

reference2 = '''"Introduction to Hidden Markov Models for Gene Prediction," by Drexel University ECE Dept.,
    available online at: https://faculty.coe.drexel.edu/gailr/ECE-S690-503/markov_models.ppt.pdf'''

reference3 = '''National Center for Biotechnology Information database;
    available online at: ftp://ftp.ncbi.nih.gov/genomes/Homo_sapiens/ARCHIVE/ANNOTATION_RELEASE.109/'''

our_submission = Who_and_what([maggie, john], OPTION, title, approach, workload_distribution, [reference1, reference2, reference3])

# You can run this file from the command line by typing:
# python3 who_and_what.py

# Running this file by itself should produce a report that seems correct to you.
if __name__ == '__main__':
  print(our_submission.report())
