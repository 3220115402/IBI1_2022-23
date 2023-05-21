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
        if seq.endswith('TGA'):
            genes.append((gene_name, seq))

with open('TGA_genes.fa', 'w') as f:
    for gene in genes:
        f.write('>{}\n{}\n'.format(gene[0], gene[1]))