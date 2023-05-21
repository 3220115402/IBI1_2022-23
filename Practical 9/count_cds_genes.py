stop_codon = input('Enter stop codon (TAA, TAG, or TGA): ')
filename = '{}_stop_genes.fa'.format(stop_codon)

with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as f:
    lines = f.readlines()

genes = []
for i in range(len(lines)):
    if lines[i].startswith('>'):
        gene_name = lines[i].split()[0][1:]
        seq = ''
        for j in range(i+1, len(lines)):
            if lines[j].startswith('>'):
                break
            seq += lines[j].strip()
        if seq.endswith(stop_codon):
            count = 0
            for k in range(len(seq)):
                if seq[k:k+3] == 'ATG':
                    for l in range(k+3, len(seq), 3):
                        if seq[l:l+3] == stop_codon:
                            count += 1
                            break
            genes.append((gene_name, count, seq))

with open(filename, 'w') as f:
    for gene in genes:
        f.write('>{}_{}\n{}\n'.format(gene[0], gene[1], gene[2]))