num_lines = sum(1 for _ in open('in.txt'))
with open('in.txt', 'r') as original: data = original.read()
with open('in.txt', 'w') as modified: modified.write(f"{num_lines}\n" + data)
    