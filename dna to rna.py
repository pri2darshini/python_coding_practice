def dna_to_rna(dna):
    dna = dna.upper()
    rna = dna.replace('T','U')
    print(rna)

dna_to_rna('ATCGTACGT')
dna_to_rna('AtCGtACGT')
dna_to_rna('TTTTT')
dna_to_rna('tttttt')
