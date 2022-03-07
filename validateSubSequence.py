def isValidSubsequence(array, sequence):
	seqIdx = 0
	for num in array:
		if len(sequence) == seqIdx:
			break
		if num == sequence[seqIdx]:
			seqIdx += 1
	return seqIdx == len(sequence)
# O(n) time | O(1) space

def isValidSubsequence(array, sequence):
	for num in array:
		if (len(sequence) == 0):
			break
		if num == sequence[0]:
			sequence.pop(0)
	if (len(sequence) == 0):
			return True
	return False
# O(n) time | O(1) space

def isValidSubsequence(array, sequence):
	arrIdx = 0 
	seqIdx = 0
	while arrIdx < len(array) and seqIdx < len(sequence):
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx += 1
		arrIdx += 1
    return seqIdx == len(sequence)
# O(n) time | O(1) space
