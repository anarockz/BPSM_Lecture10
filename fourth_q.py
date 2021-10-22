hello="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
#first part
first_exon=hello[0:64]
second_exon=hello[92:]
print(first_exon)
print(second_exon)
coding_sequence=first_exon+second_exon
print(coding_sequence)

#second part
length=len(coding_sequence)
calc=(length/len(hello))*100
print(calc)

#third part
intron=hello[65:92]
intron_mod=intron.lower()
final_sequence=first_exon+intron_mod+second_exon
print(final_sequence)