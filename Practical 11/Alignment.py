# Read Seq1 and Seq2 and Seq3
with open("ACE2_CAT.fa") as f:
    seq1_name = f.readline().strip()
    seq1 = f.readline().strip()
with open("ACE2_HUMAN.fa") as f:
    seq2_name = f.readline().strip()
    seq2 = f.readline().strip()
with open("ACE2_MOUSE.fa") as f:
    seq3_name = f.readline().strip()
    seq3 = f.readline().strip()

# Read BLOSUM62 matrix
blosum62 = {}
with open("BLOSUM.txt") as f:
    header = f.readline().strip().split()
    for line in f:
        row = line.strip().split()
        aa = row[0]
        blosum62[aa] = {}
        for i in range(1, len(row)):
            blosum62[aa][header[i-1]] = int(row[i])

# Compare each amino acid
scores = []
for i in range(len(seq1)):
    aa1 = seq1[i]
    aa2 = seq2[i]
    score = blosum62[aa1][aa2]
    scores.append(score)
print(seq1_name)
print(seq1)
print(seq2_name)
print(seq2)
print("BLOSUM score:", sum(scores))
print("Percentage identity:", sum([1 for s in scores if s > 0])/len(scores))
print('\n')

for i in range(len(seq1)):
    aa1 = seq1[i]
    aa3 = seq3[i]
    score = blosum62[aa1][aa3]
    scores.append(score)
print(seq1_name)
print(seq1)
print(seq3_name)
print(seq3)
print("BLOSUM score:", sum(scores))
print("Percentage identity:", sum([1 for s in scores if s > 0])/len(scores))
print('\n')
for i in range(len(seq1)):
    aa3 = seq3[i]
    aa2 = seq2[i]
    score = blosum62[aa3][aa2]
    scores.append(score)
print(seq3_name)
print(seq3)
print(seq2_name)
print(seq2)
print("BLOSUM score:", sum(scores))
print("Percentage identity:", sum([1 for s in scores if s > 0])/len(scores))
print('\n')