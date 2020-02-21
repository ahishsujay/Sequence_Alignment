#!/usr/bin/env python3

# Write your code here
import sys

seq1_fasta = sys.argv[1]                        #Storing the fasta file1 (inputted as argument) in seq1_fasta
seq2_fasta = sys.argv[2]                        #Storing the fasta file2 (inputted as argument) in seq2_fasta

seq1 = ""                                       #seq1 string is going to contain the sequence 1
seq2 = ""                                       #seq2 string is going to contain the sequence 2

#Storing the sequence 1 in seq1:
with open(seq1_fasta) as seq1_fh:
    for line in seq1_fh.readlines():
        if line.startswith(">"):
            continue
        else:
            seq1 += line
seq1 = seq1.rstrip("\n")                        #Stripping the trailing new line character

#Storing the sequence 2 in seq2:
with open(seq2_fasta) as seq2_fh:
    for line in seq2_fh.readlines():
        if line.startswith(">"):
            continue
        else:
            seq2 += line
seq2 = seq2.rstrip("\n")                        #Stripping the trailing new line character

m = len(seq1)                                   #Seq1 will be the vertical sequence to the left
n = len(seq2)                                   #Seq2 will be the horizontal sequence on top
init_mat = []                                   #Initialised matrix

#Scoring system for match, mismatch and gap:
match = +1
mismatch = -1
gap = -1

#Initialising the matrix to 0 (Part1):
for i in range(m+1):                            #Adding +1 as one extra column needed to hold the initialised values
    temp = []
    for j in range(n+1):                        #Adding +1 as one extra column needed to hold the initialised values
        temp.append(0)
    init_mat.append(temp)                       #init_mat is a matrix of len(seq1)+1 rows and len(seq2)+1 columns containing 0's


#Matrix filling (Part2):
for i in range(1,m+1):
    for j in range(1, n+1):
        if seq1[i-1] == seq2[j-1]:
            init_mat[i][j] = max(init_mat[i][j-1]+gap, init_mat[i-1][j]+gap, init_mat[i-1][j-1]+match, 0)
        else:
            init_mat[i][j] = max(init_mat[i][j-1]+gap, init_mat[i-1][j]+gap, init_mat[i-1][j-1]+mismatch,0)

'''
#Visualise as a matrix:
for row in init_mat:
    for element in row:
        print(element, end="\t")
    print("\n")
'''

#Finding the maximum value in the matrix and getting its index:
seq1_align = ""                                 #The aligned sequence (seq1) is going to be appended to this string
seq2_align = ""                                 #The aligned sequence (seq2) is going to be appended to this string
maximum = 0                                     #Maximum score of aligned sequence
for row in range(1, m+1):
    for column in range(1,n+1):
        if maximum < init_mat[row][column]:
            maximum = init_mat[row][column]     #Storing the maximum value
            i = row                             #Storing the row number of maximum value
            j = column                          #Storing the column numner of maximum value

#Backtracking (Part3):
while init_mat[i][j] != 0:
    if seq1[i-1] == seq2[j-1]:
        seq1_align += seq1[i-1]
        seq2_align += seq2[j-1]
        i -= 1
        j -= 1

    #If the sequence don't match:
    elif seq1[i-1] != seq2[j-1]:
        temp_list = [init_mat[i-1][j-1], init_mat[i-1][j], init_mat[i][j-1]]        #Creating a temp_list in order to find the maximum values from top, diagonal and left in order to backtrack
        #If the maximum value is the 0th indexed position, i.e., the diagonal value:
        if max(temp_list) == temp_list[0]:
            seq1_align += seq1[i-1]
            seq2_align += seq2[j-1]
            i -= 1
            j -= 1

        #If the maximum value is the 1st indexed position, i.e., the top value:
        elif max(temp_list) == temp_list[1]:
            seq1_align += seq1[i-1]
            seq2_align += "-"
            i -= 1

        #If the maximum value is the 2nd indexed position, i.e., the left vlaue:
        elif max(temp_list) == temp_list[-1]:
            seq1_align += "-"
            seq2_align += seq2[j-1]
            j-=1

    #If there is an error (somehow? just in case?), initialising the values of i and j in order for it to not turn into an infinite loop
    else:
        print("Error. Exit.")
        i=0
        j=0

seq1_align = seq1_align[::-1]                   #Reverse the string seq1_align
seq2_align = seq2_align[::-1]                   #Reverse the string seq2_align

#Storing the match, mismatch and gap symbols in match_string:
match_string = ""
for i in range(len(seq1_align)):
    if seq1_align[i] == seq2_align[i]:
        match_string += "|"
    elif seq1_align[i] != seq2_align[i]:
        if (seq1_align[i] == "-" or seq2_align[i] == "-"):
            match_string += " "
        else:
            match_string += "*"

#Calculating the alignment score:
alignment_score = 0
for i in range(len(match_string)):
    if match_string[i] == "|":
        alignment_score += 1
    elif (match_string[i] == "*" or match_string[i] == " "):
        alignment_score += -1

#Printing out the final result:
print(seq1_align)
print(match_string)
print(seq2_align)
print("Alignment score:", alignment_score)
