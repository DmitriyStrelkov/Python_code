# Compute Hamming distance: the differences in two sequences.
# Written in Python 3.5 by Dmitriy Strelkov
from Bio.Seq import Seq

a = input("What is the first sequence?")
b = input("What is the second sequence?")
n = len(b)
Hamming_D = 0
for index in range(0,n):
    if a[index] != b[index]:
        Hamming_D += 1

print("Your computed Hamming distance is:")
print(Hamming_D)