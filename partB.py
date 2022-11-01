import partA
import sys

def commonWords(counts1, counts2):
    commonRes = 0
    for key in counts1:
        if key in counts2:
            commonRes += 1
    return commonRes
    



if __name__ == '__main__':
    file1, file2 = sys.argv[-1], sys.argv[-2]
    if file1[-4:] == '.txt' and file2[-4:] == '.txt':
        tokens1, tokens2 = partA.tokenize(file1), partA.tokenize(file2)
        counts1, counts2 = partA.countFrequencies(tokens1), partA.countFrequencies(tokens2)
        print(commonWords(counts1, counts2))

