#Justin Dulay
#DNA Mutator

sequence = input('Enter a DNA sequence: ')
pattern = input('Enter the pattern: ')

if pattern not in sequence:
  print(pattern, 'not in DNA sequence.')
  pattern = input('Enter a new pattern: ')

pattern_r = pattern[::-1] #reverse pattern


index_a = sequence.index(pattern)
index_b = index_a + len(pattern)
reverse_index = sequence.index(pattern_r, index_b)
reverse_index_b = reverse_index + len(pattern_r)

mutate_before = sequence[index_b:reverse_index]
mutate = mutate_before[::-1]
statement = 'Mutated DNA sequence: '

print(statement + sequence[:index_a] + pattern + mutate + pattern_r + sequence[reverse_index_b:])

 
