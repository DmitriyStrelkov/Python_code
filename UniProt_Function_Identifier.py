from Bio import ExPASy
from Bio import SwissProt
protein = raw_input("What is the UniProt ID of your protein?")
handle = ExPASy.get_sprot_raw(protein)
pro_func = SwissProt.read(handle)

print pro_func.keywords

