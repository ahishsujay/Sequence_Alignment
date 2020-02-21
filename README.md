# Sequence_Alignment

Python scripts for Needleman-Wunsch (NW) and Smith-Waterman (SW) algorithm.

The algorithm can be divided into three steps:
1. Initialization: Construction of the matrix with the two sequences as each axis and selection of a suitable scoring system. For simplicity, there are three types of scores in this utiliztion:
a. Match = +1
b. Mismatch = -1
c. Gap = -1
2. Matrix filling: Filling the matrix based on the scoring system. This occurs one row at a time, starting from the topmost row. Each cell in the matrix derives the value from the adjacent cells located to the left, top-left or on top of the current cell. The match score is added or gap/mismatch penalty is subtracted from these adjacent cells and the maximum value is carried over to the current cell.
3. Backtracking: Once the matrix has been filled up, backtracking is done to compute the optimal alignment(s). The backtracking step starts from the very last cell filled in the matrix (the bottom-right cell) and proceeds to the first cell filled in matrix (the cell with 0 in the upper left corner of the matrices. This backtrack path is computed by moving through the adjacent cells (cells to the left, top-left and on top of the current cell) with the maximum score such that the path has the maximum total score. If multiple paths exist, then all of them are considered to be the optimal paths. This path is converted to an alignment by the following rule: the path moves diagonally to the left if there is a match or if the maximum score of the adjacent cells is present in the diagonal left cell. If either of these are true, the two corresponding characters from each sequence are aligned together. When the maximum score is obtained by moving horizontally, then a gap is introduced in the sequence on the vertical axis, and if the path moves vertically, then a gap is introduced in the sequence on the horizontal axis.

# Needleman-Wunsch Algorithm:
Needleman-Wunsch is a popular algorithm used in Bioinformatics for sequence comparison. It is used for global alignment which attempts to align every residue in two sequences. It is most useful when the two query sequences are similar and roughly equal in size.
### Input:
1. FASTA file 1
2. FASTA file 2

### Syntax:
/nwAlign.py <input FASTA file 1> <input FASTA file 2>

### Example usage:
./nwAlign.py seq1.fa seq2.fa

seq1.fa contains:
'>seq1.fa
ATTGCC'

seq2.fa contains:
>seq2.fa
AGTCC

### Output:
ATTGCC
|*| ||
AGT-CC
Alignment score: 2

where, "|" represents a match and "*" represents a mismatch

# Smith-Waterman Algorithm:
Another widely used algorithm in Bioinformatics for sequence comparison is the Smith-Waterman algorithm. It performs local sequence alignment which is used for indentifying regions of similarity within very long sequences that are usually divergent overall.
### Input:
1. FASTA file 1
2. FASTA file 2

##$ Syntax:
/swAlign.py <input FASTA file 1> <input FASTA file 2>

### Example usage:
./nwAlign.py seq1.fa seq2.fa

seq1.fa contains:
>seq1.fa
TGTTACGG

seq2.fa contains:
>seq2.fa
GGTTGACTA

### Output:
GTT-AC
 ||| ||
 GTTGAC
 Alignment score: 1
