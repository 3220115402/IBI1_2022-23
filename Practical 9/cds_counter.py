seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
stop_codons = ['TAA', 'TAG', 'TGA']
count = 0
for i in range(len(seq)):
    if seq[i:i+3] == 'ATG':
        for j in range(i+3, len(seq)):
            if seq[j:j+3] in stop_codons:
                count += 1
print(count)