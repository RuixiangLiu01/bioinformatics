exact_match = 2
transition = -5
transversion = -7
gap = -5
Purine = "AG"
Pyrimidine = "TC"
def alignment(base1, base2):
    if base1 == base2:
        return exact_match
    else:
        if (base1 in Purine and base2 in Purine) or (base1 in Pyrimidine and base2 in Pyrimidine):
            return transition
        else:
            return transversion

def Scoring(seq1, seq2):
    matrix = [[0] * (len(seq1) + 1) for i in range(len(seq2) + 1)]
    for i in range(len(matrix[0])):
        matrix[0][i] = -5 * i
    for j in range(len(matrix)):
        matrix[j][0] = -5 * j
    print(matrix)
        
    for i in range(1, len(seq2) + 1):
        for j in range(1, len(seq1) + 1):
            matrix[i][j] = max(matrix[i - 1][j - 1] + alignment(seq2[i - 1], seq1[j - 1]), 
                                       matrix[i - 1][j] + gap, 
                                       matrix[i][j - 1] + gap)
            
    return matrix

Matrix = Scoring(seq1, seq2)
i, j = len(seq2), len(seq1)
align_seq1 = ""
align_seq2 = ""
def traceback(seq1, seq2):
    global i, j, align_seq1, align_seq2
    while True:
        if i == 0 and j == 0:
            break
        if Matrix[i][j] == Matrix[i - 1][j - 1] + alignment(seq2[i - 1], seq1[j - 1]):
            align_seq1 += seq1[j - 1]
            align_seq2 += seq2[i - 1]
            i -= 1
            j -= 1
        elif Matrix[i][j] == Matrix[i - 1][j] + gap:
            align_seq1 += "-"
            align_seq2 += seq2[i - 1]
            i -= 1
        elif Matrix[i][j] == Matrix[i][j - 1] + gap:
            align_seq1 += seq1[j - 1]
            align_seq2 += "-"
            j -= 1
    print(align_seq1[::-1] + '\n' + align_seq2[::-1])
