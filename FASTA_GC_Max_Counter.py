#problem with the fasta sequences is that they include multiple lines
#python doesn't like that, so we pull directly from clipboard, split fastas, remove linespaces except the first
#then we split into a list of lists, with the format being
#list_of_fasta = [[1,seq], [2,seq] ...[n,seq]]
#written in 3.5

from Bio.Seq import Seq #for easy manipulation of DNA
from tkinter import Tk #to pull fasta sequences from keyboard
r = Tk() #tk root
r.withdraw()

input("This program finds the highest GC content of your fasta sequences and displays the percentage. Press Enter to continue")
n = 0
n += int(input("How many sequences are you analyzing for GC content?"))
input("Copy your list of fasta sequences to your clipboard, then press Enter.")
all_seqs = r.selection_get(selection = "CLIPBOARD")


fasta_list = all_seqs.split('>')
del fasta_list[0] #deletes blank list element

#now remove all linespace

for m in range(0,n):
    fasta_list[m] = fasta_list[m].replace('\n','')

#make sequences
seq_list = []
for m in range(0,n):
    seq_list.append(Seq(fasta_list[m]))

#make list of GC contents
GC = []
for m in range(0,n):
    current = seq_list[m]
    GC.append(100*(float((current.count("G") + current.count("C"))) / (float((current.count("G") + current.count("C")+ current.count("A") + current.count("T"))))))

#print max GC content and which fasta sequence it corresponds to
print("Your max GC content is:")
print(max(GC))
print("The corresponding fasta sequence is sequence number:")
print(GC.index(max(GC)) + 1)





