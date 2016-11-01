user_seq = raw_input("What is your DNA sequence?")
sort_nuc = ['A','C','G','T']
counts={'A':0,'C':0,'G':0,'T':0}

for nucleotide in user_seq:
    counts[nucleotide] +=1

for nuc in sort_nuc:
    print nuc, counts[nuc]
    