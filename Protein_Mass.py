#Written in Python 3.5 by Dmitriy Strelkov
#Uses the Biopython module

from Bio.SeqUtils.ProtParam import ProteinAnalysis

def findProteinMass(sequence):
    protein = ProteinAnalysis(sequence)
    mass = protein.molecular_weight()
    print(mass)
    return(mass)

