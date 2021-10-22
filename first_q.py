dna_seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
number_of_a = dna_seq.count('A')
print(number_of_a)
number_of_t = dna_seq.count('T')
print(number_of_t)
adding_a_t = (number_of_a+number_of_t)/len(dna_seq)
print(adding_a_t)
