RNA = ''
user_seq = raw_input("What is your DNA sequence?")
for nucleotide in user_seq:
    if nucleotide == 'T':
        RNA += 'U'
    else:
        RNA += nucleotide

print RNA