sequence = input('Enter a DNA sequence: ')
pattern = input('Enter the pattern: ')

if pattern not in sequence:
  print(pattern, 'not in DNA sequence.')
  pattern = input('Enter a new pattern: ')

opposite = pattern[::-1]

pieces = sequence.split(pattern)
chunk = ''.join(pieces[1])
chunk  = chunk.split(opposite)
mutation = ''.join(chunk[0])
mutation = mutation[::-1]

newChunk = ' '.join(chunk[1:])
newChunk = newChunk.replace(' ',opposite)
mutatedPiece = mutation+opposite+newChunk

pieces[1] = mutatedPiece
newSequence = ' '.join(pieces)
newSequence = newSequence.replace(' ',pattern)
print('Mutated DNA sequence:',newSequence)

    

    
