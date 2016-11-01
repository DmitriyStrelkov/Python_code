from Bio.Seq import Seq
dna = raw_input("What is your DNA sequence?")
dna = Seq(dna)
print dna.reverse_complement()

