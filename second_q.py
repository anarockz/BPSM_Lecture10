seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replace_char={'A':'T','T':'A','G':'C','C':'G'}
for key,value in replace_char.items():
   changed_seq=seq.replace(key,value)
print(changed_seq)
